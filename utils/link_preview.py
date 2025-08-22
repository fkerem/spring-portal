import re
import json
import html as ihtml
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from textwrap import dedent
from typing import Optional  # <-- add this
import streamlit as st

UA = {"User-Agent": "Mozilla/5.0 (compatible; SPRING-Preview/1.0)"}

@st.cache_data(show_spinner=False, ttl=60 * 60)
def fetch_link_meta(url: str) -> dict:
    """Fetch Open Graph / Twitter Card metadata with sensible fallbacks."""
    try:
        if not re.match(r"^https?://", url, re.I):
            url = "https://" + url
        r = requests.get(url, headers=UA, timeout=8)
        r.raise_for_status()
    except Exception as e:
        return {"error": f"Fetch failed: {e}", "url": url}

    soup = BeautifulSoup(r.text, "html.parser")

    # Canonical URL if provided
    try:
        canonical_link = soup.find("link", rel=lambda v: v and "canonical" in v.lower())
        if canonical_link and canonical_link.get("href"):
            r_url = urljoin(r.url, canonical_link["href"])  # prefer canonical
        else:
            r_url = r.url
    except Exception:
        r_url = r.url

    def meta(name, attr="property"):
        tag = soup.find("meta", attrs={attr: name})
        return (tag.get("content") or "").strip() if tag else None

    def _clean_text(s: str) -> str:
        if not s:
            return s
        s = ihtml.unescape(s)
        s = s.replace("[…]", "…")
        s = re.sub(r"\s+", " ", s).replace("\xa0", " ")
        return s.strip()

    # Try extracting some JSON-LD metadata up-front
    ld_title = None
    ld_desc = None
    ld_img = None
    try:
        for script in soup.find_all("script", attrs={"type": re.compile(r"application/ld\+json", re.I)}):
            try:
                data = json.loads(script.string or "{}")
            except Exception:
                continue

            def get_first(*keys):
                for k in keys:
                    v = data.get(k)
                    if isinstance(v, str) and v.strip():
                        return v
            # Support @graph lists
            if isinstance(data, dict) and "@graph" in data and isinstance(data["@graph"], list):
                graph = data["@graph"]
                for node in graph:
                    if not isinstance(node, dict):
                        continue
                    ld_title = ld_title or node.get("headline") or node.get("name")
                    ld_desc = ld_desc or node.get("description") or node.get("abstract")
                    img_val = node.get("image") or node.get("thumbnailUrl")
                    if isinstance(img_val, str):
                        ld_img = ld_img or img_val
                    elif isinstance(img_val, dict):
                        ld_img = ld_img or img_val.get("url") or img_val.get("contentUrl")
                    elif isinstance(img_val, list) and img_val:
                        first = img_val[0]
                        if isinstance(first, str):
                            ld_img = ld_img or first
                        elif isinstance(first, dict):
                            ld_img = ld_img or first.get("url") or first.get("contentUrl")
            else:
                ld_title = ld_title or data.get("headline") or data.get("name")
                ld_desc = ld_desc or data.get("description") or data.get("abstract")
                img_val = data.get("image") or data.get("thumbnailUrl")
                if isinstance(img_val, str):
                    ld_img = ld_img or img_val
                elif isinstance(img_val, dict):
                    ld_img = ld_img or img_val.get("url") or img_val.get("contentUrl")
                elif isinstance(img_val, list) and img_val:
                    first = img_val[0]
                    if isinstance(first, str):
                        ld_img = ld_img or first
                    elif isinstance(first, dict):
                        ld_img = ld_img or first.get("url") or first.get("contentUrl")
    except Exception:
        pass

    title = meta("og:title") or meta("twitter:title", "name") or (ld_title and _clean_text(ld_title))
    if not title:
        # Prefer on-page H1 for articles
        h1 = soup.find("h1")
        if h1 and h1.get_text(strip=True):
            title = _clean_text(h1.get_text(" ", strip=True))
    if not title:
        title = soup.title.string.strip() if soup.title and soup.title.string else None

    desc = meta("og:description") or meta("twitter:description", "name") or meta("description", "name") or (ld_desc and _clean_text(ld_desc))
    if not desc:
        # Try first paragraph inside article/main
        container = soup.find("article") or soup.find("main") or soup.find(attrs={"role": "main"})
        p = container.find("p") if container else soup.find("p")
        if p:
            desc = _clean_text(p.get_text(" ", strip=True))

    # Prefer secure og:image, then regular, then twitter
    img = (
        meta("og:image:secure_url")
        or meta("og:image")
        or meta("twitter:image", "name")
    )
    img = urljoin(r.url, img) if img else None

    # Favicon
    icon_link = soup.find("link", rel=lambda v: v and "icon" in v.lower())
    if icon_link and icon_link.get("href"):
        ico = urljoin(r.url, icon_link["href"])
    else:
        parsed = requests.utils.urlparse(r.url)
        ico = f"{parsed.scheme}://{parsed.netloc}/favicon.ico"

    site = meta("og:site_name")
    if not site:
        site = re.sub(r"^https?://(www\.)?", "", requests.utils.urlparse(r.url).netloc)

    # ─── Fallback image detection when no OG/Twitter image ───────────────
    if not img:
        # 1) Try JSON-LD (Article/NewsArticle/etc.)
        try:
            if ld_img:
                img = urljoin(r.url, ld_img)
        except Exception:
            pass

        # 2) Try to find an <article> image, then a reasonable first image
        if not img:
            article = soup.find("article") or soup.find("main") or soup.find(attrs={"role": "main"})
            candidate = None
            if article:
                candidate = article.find("img", src=True)
            if not candidate:
                # Fallback to first non-trivial image on the page
                for im in soup.find_all("img", src=True):
                    src = im.get("src", "")
                    if not src or src.startswith("data:"):
                        continue
                    low = src.lower()
                    # Skip logos/icons/sprites
                    if any(k in low for k in ["sprite", "icon", "favicon", "logo"]):
                        continue
                    candidate = im
                    break
            if candidate:
                img = urljoin(r.url, candidate.get("src"))

    return {
        "url": r_url,
        "title": title or site or r.url,
        "description": _clean_text(desc or ""),
        "image": img,
        "favicon": ico,
        "site": site,
    }


def _ensure_link_preview_css(theme: str = "auto"):
    """Inject CSS once per theme; dark-mode aware; no underlines; fixed media box."""
    if theme == "auto":
        theme = st.context.theme.type  # "light" | "dark"

    if st.session_state.get("_lp_css_theme") == theme:
        return

    if theme == "dark":
        BG = "#0f131a"
        FG = "#e5e7eb"
        SUB= "#9aa0a6"
        BR = "#22262e"
        HOVER = "rgba(255,255,255,0.06)"
        SHADOW = "0 1px 10px rgba(0,0,0,0.35)"
        LINK = "#a5b4fc"
    else:
        BG = "#ffffff"
        FG = "#111827"
        SUB= "#4b5563"
        BR = "#e5e7eb"
        HOVER = "rgba(0,0,0,0.03)"
        SHADOW = "0 1px 6px rgba(0,0,0,0.06)"
        LINK = "#2563eb"

    css = f"""
    <style>
      .lp-card {{
        background:{BG};
        color:{FG};
        border:1px solid {BR};
        border-radius:14px;
        box-shadow:{SHADOW};
        transition: background 120ms ease, border-color 120ms ease;
      }}

      /* Make whole card clickable but never underlined */
      .lp-a, .lp-a:link, .lp-a:visited, .lp-a:hover, .lp-a:active {{
        text-decoration: none !important;
        color: inherit;
        display:flex;
        gap:12px;
        padding:12px;
        align-items:flex-start;
      }}
      .lp-a *, .lp-a *:link, .lp-a *:visited, .lp-a *:hover, .lp-a *:active {{
        text-decoration: none !important;
      }}
      .lp-a:focus-visible {{ outline: 2px solid {LINK}; outline-offset: 2px; }}
      .lp-a:hover {{ background:{HOVER}; }}

      /* Media box is fixed-size (width/height set inline); never grows */
      .lp-thumb, .lp-thumb--sm {{
        flex:0 0 auto;
        border-radius:10px;
        overflow:hidden;
        background:#1112;
      }}
      .lp-thumb img {{
        width:100%; height:100%;
        object-fit:cover; display:block;
      }}

      .lp-text {{ display:flex; flex-direction:column; gap:6px; min-width:0; }}
      .lp-site {{
        display:flex; align-items:center; gap:8px;
        font-size:12px; color:{SUB};
        white-space:nowrap; overflow:hidden; text-overflow:ellipsis;
      }}
      .lp-ico {{ width:14px; height:14px; border-radius:3px; flex:0 0 14px; }}
      .lp-title {{ font-size:15px; font-weight:600; line-height:1.35; color:{FG}; }}
      .lp-desc  {{
        font-size:13px; color:{SUB}; line-height:1.45;
        display:-webkit-box; -webkit-line-clamp:3; -webkit-box-orient:vertical; overflow:hidden;
      }}
      .lp-url {{
        font-size:12px; color:{LINK};
        white-space:nowrap; overflow:hidden; text-overflow:ellipsis;
        text-decoration: none !important;
      }}
    </style>
    """
    st.markdown(dedent(css), unsafe_allow_html=True)
    st.session_state["_lp_css_theme"] = theme


def render_link_card(
    meta: dict,
    theme: str = "auto",
    compact: bool = True,
    media_px: Optional[int] = None,   # <-- Python 3.9-friendly
):
    """Render a minimal, non-ad-looking link preview card with clamped image.

    Note: We inject CSS once, but also inline critical styles for layout so the card
    still looks correct if global CSS injection is blocked by container context.
    """
    if "error" in meta:
        st.warning(meta["error"])
        return

    _ensure_link_preview_css(theme)

    title = meta["title"]
    desc  = meta["description"][:180] + ("…" if len(meta["description"]) > 180 else "")
    site  = meta["site"]
    href  = meta["url"]
    img   = meta.get("image")
    ico   = meta.get("favicon")

    # Fixed media size (override with media_px if desired)
    if compact:
        w = media_px or 84
        h = w  # square
        thumb_class = "lp-thumb--sm"
    else:
        w = media_px or 220
        h = int(round(w * 9/16))  # 16:9
        thumb_class = "lp-thumb"

    # Palette for inline styles (mirrors _ensure_link_preview_css)
    if theme == "auto":
        theme_eff = st.context.theme.type
    else:
        theme_eff = theme

    if theme_eff == "dark":
        BG = "#0f131a"; FG = "#e5e7eb"; SUB = "#9aa0a6"; BR = "#22262e"; SHADOW = "0 1px 10px rgba(0,0,0,0.35)"; LINK = "#a5b4fc"; HOVER = "rgba(255,255,255,0.06)"
    else:
        BG = "#ffffff"; FG = "#111827"; SUB = "#4b5563"; BR = "#e5e7eb"; SHADOW = "0 1px 6px rgba(0,0,0,0.06)"; LINK = "#2563eb"; HOVER = "rgba(0,0,0,0.03)"

    thumb_html = ""
    if img:
        thumb_html = (
            f'<div class="{thumb_class}" style="width:{w}px;height:{h}px;flex:0 0 auto;border-radius:10px;overflow:hidden;background:#1112;">'
            f'  <img src="{img}" alt="preview" loading="lazy" decoding="async" style="width:100%;height:100%;object-fit:cover;display:block;"/>'
            f'</div>'
        )

    ico_html = (
        f'<img class="lp-ico" src="{ico}" alt="" onerror="this.style.display=\'none\'" style="width:14px;height:14px;border-radius:3px;flex:0 0 14px;">'
        if ico else ""
    )

    html = f"""
    <div class="lp-card" style="background:{BG};color:{FG};border:1px solid {BR};border-radius:14px;box-shadow:{SHADOW};">
      <a class="lp-a" href="{href}" target="_blank" rel="noopener" style="text-decoration:none;color:inherit;display:flex;gap:12px;padding:12px;align-items:flex-start;border-radius:14px;transition:background 120ms ease;" onmouseenter="this.style.background='{HOVER}';" onmouseleave="this.style.background='transparent';">
        {thumb_html}
        <div class="lp-text" style="display:flex;flex-direction:column;gap:6px;min-width:0;">
          <div class="lp-site" style="display:flex;align-items:center;gap:8px;font-size:12px;color:{SUB};white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{ico_html}<span>{site}</span></div>
          <div class="lp-title" style="font-size:15px;font-weight:600;line-height:1.35;color:{FG};">{title}</div>
          {f"<div class='lp-desc' style='font-size:13px;color:{SUB};line-height:1.45;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;'>{desc}</div>" if desc else ""}
          <div class="lp-url" style="font-size:12px;color:{LINK};white-space:nowrap;overflow:hidden;text-overflow:ellipsis;text-decoration:none !important;">{href}</div>
        </div>
      </a>
    </div>
    """
    st.markdown(dedent(html), unsafe_allow_html=True)