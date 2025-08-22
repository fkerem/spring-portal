import streamlit as st
import math
from pathlib import Path
from PIL import Image
from streamlit_scroll_to_top import scroll_to_here

# Center-crop to a target aspect ratio (e.g., 16:9, 4:3, 1:1)
@st.cache_data(show_spinner=False)
def load_thumb(path: str, ratio_w: int, ratio_h: int, base_width: int = 400):
    img = Image.open(path).convert("RGB")
    w, h = img.size
    target_ratio = ratio_w / ratio_h
    cur_ratio = w / h

    if cur_ratio > target_ratio:
        # Too wide -> crop width
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:
        # Too tall -> crop height
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        img = img.crop((0, top, w, top + new_h))

    # Light resize for faster rendering/caching
    new_h = int(base_width * ratio_h / ratio_w)
    img = img.resize((base_width, new_h), Image.LANCZOS)
    return img

def createPage():

    if st.session_state.pop("_scroll_to_top", False):  # NEW
        scroll_to_here(0, key="header")

    st.subheader("🖼️ Photos from Purdue Research Farm")

    photos_dir = Path("photos")
    images = [{"url": str(photos_dir / f"p{i}.jpg"), "caption": f"Photo {i+1}"} for i in range(32)]

    # Keep selected index valid
    if "gallery_selected" not in st.session_state or st.session_state.gallery_selected >= len(images):
        st.session_state.gallery_selected = 0

    # Controls
    cols_per_row = st.slider("Thumbnails per row", 2, 6, 4, help="Adjust the gallery layout")
    #ratio_label = st.selectbox("Thumbnail aspect ratio", ["16:9", "4:3", "1:1"], index=0)
    ratio_label = "16:9"
    ratio_w, ratio_h = map(int, ratio_label.split(":"))

    # Big (uncropped) preview
    sel = st.session_state.gallery_selected
    with st.container(border=True):
        st.image(images[sel]["url"], caption=images[sel]["caption"], use_container_width=True)

    st.markdown("### Gallery")

    total = len(images)
    rows = math.ceil(total / cols_per_row)

    for r in range(rows):
        cols = st.columns(cols_per_row, gap="small")
        for c in range(cols_per_row):
            i = r * cols_per_row + c
            if i >= total:
                break
            with cols[c]:
                thumb = load_thumb(images[i]["url"], ratio_w, ratio_h)
                st.image(thumb, use_container_width=True)  # uniform size since aspect is fixed
                if st.button("View", key=f"view_{i}", use_container_width=True):
                    st.session_state.gallery_selected = i
                    st.session_state._scroll_to_top = True
                    st.rerun()