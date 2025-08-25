import streamlit as st
from streamlit.components.v1 import html

def navigate_to(session_state, user: str, page: str, module: str = None):
    """
    Navigate to a page with user role and optional module via query params.
    """

    session_state["_scroll_to_top"] = True  # Flag to scroll on next load

    st.query_params.clear()
    st.query_params["user"] = user
    st.query_params["page"] = page

    # Only include module if navigating to 'lessons'
    if user == "student" and page == "lessons" and module:
        st.query_params["lesson"] = module

    st.rerun()


def render_back_forth_nav_old(session_state, current_module_key, all_modules, position=""):
    flat_modules = []
    for level, modules in all_modules.items():
        for m in modules:
            flat_modules.append({"level": level[2:].split("(")[0][:-1], **m})

    current_index = next((i for i, m in enumerate(flat_modules) if m["key"] == current_module_key), None)
    if current_index is None:
        st.warning("Navigation key not found.")
        return

    prev_link = flat_modules[current_index - 1] if current_index > 0 else None
    next_link = flat_modules[current_index + 1] if current_index < len(flat_modules) - 1 else None

    col1, col2, col3 = st.columns([1, 4, 1])

    with col1:
        if prev_link and st.button(
            f"⬅️ {prev_link['level']} | {prev_link['label']}",
            key=f"prev_{position}"
        ):
            session_state.selected_module_path = f"views.{prev_link['target']}"
            session_state.selected_module_key = prev_link["key"]
            navigate_to(
                session_state,
                user=st.query_params.get("user", "student"),
                page="lessons",
                module=prev_link["key"]
            )

    with col3:
        if next_link and st.button(
            f"{next_link['level']} | {next_link['label']} ➡️",
            key=f"next_{position}"
        ):
            session_state.selected_module_path = f"views.{next_link['target']}"
            session_state.selected_module_key = next_link["key"]
            navigate_to(
                session_state,
                user=st.query_params.get("user", "student"),
                page="lessons",
                module=next_link["key"]
            )


def render_back_forth_nav(session_state, current_module_key, all_modules, position=""):
    flat_modules = []
    for _, modules in all_modules.items():
        for m in modules:
            flat_modules.append({**m})

    current_index = next((i for i, m in enumerate(flat_modules) if m["key"] == current_module_key), None)
    if current_index is None:
        st.warning("Navigation key not found.")
        return

    prev_link = flat_modules[current_index - 1] if current_index > 0 else None
    next_link = flat_modules[current_index + 1] if current_index < len(flat_modules) - 1 else None

    col1, col2, col3 = st.columns([1, 4, 1])

    with col1:
        if prev_link and st.button(
            f"⬅️ {prev_link['label']}",
            key=f"prev_{position}"
        ):
            session_state.selected_module_path = f"views.{prev_link['target']}"
            session_state.selected_module_key = prev_link["key"]
            navigate_to(
                session_state,
                user=st.query_params.get("user", "student"),
                page="lessons",
                module=prev_link["key"]
            )

    with col3:
        if next_link and st.button(
            f"{next_link['label']} ➡️",
            key=f"next_{position}"
        ):
            session_state.selected_module_path = f"views.{next_link['target']}"
            session_state.selected_module_key = next_link["key"]
            navigate_to(
                session_state,
                user=st.query_params.get("user", "student"),
                page="lessons",
                module=next_link["key"]
            )

def render_module_nav_old(session_state, all_modules):
    col1, col2, col3 = st.columns(3)
    level_cols = [col1, col2, col3]

    for i, (level, modules) in enumerate(all_modules.items()):
        with level_cols[i]:
            with st.expander(level, expanded=False):
                for m in modules:
                    if st.button(f'📚 {m["label"]}', key=m["key"]):
                        session_state.selected_module_path = f"views.{m['target']}"
                        session_state.selected_module_key = m["key"]
                        navigate_to(session_state, user=st.query_params.get("user", "student"), page="lessons", module=m["key"])

import streamlit as st
from urllib.parse import urlencode
from utils.navigation import navigate_to  # keep for fallback mode

import streamlit as st
from urllib.parse import urlencode
from utils.navigation import navigate_to  # used when mode="button"

import streamlit as st
from urllib.parse import urlencode
from utils.navigation import navigate_to  # used when mode="button"

def render_module_nav(session_state, all_modules, per_row: int = 5, mode: str = "button"):
    """
    Uniform, centered lesson cards that don't open a new tab.

    mode:
      - "button" (default): uses st.button + navigate_to (same tab)
      - "link": styled <a href="..."> (also same tab)
    """

    # Robust, centered styling for both st.button and our <a> link
    st.markdown("""
    <style>
      .stButton, [data-testid="stButton"] { width: 100%; }

      /* Shared card look & centering */
      .stButton button,
      [data-testid="stButton"] button,
      .lesson-link {
        display: flex !important;
        align-items: center !important;   /* vertical center */
        justify-content: center !important; /* horizontal center */
        width: 100% !important;
        height: 90px !important;
        box-sizing: border-box !important;

        background-color: #0e1117 !important;
        color: #ffffff !important;
        border: 1px solid #444 !important;
        border-radius: 10px !important;

        padding: 10px !important;
        font-size: 14px !important;
        line-height: 1.2 !important;
        text-align: center !important;
        text-decoration: none !important;

        white-space: normal !important;
        overflow-wrap: break-word !important;
        word-break: break-word !important;
        gap: 0.5rem !important; /* nice spacing if you keep the emoji */
      }

      .stButton button:hover,
      [data-testid="stButton"] button:hover,
      .lesson-link:hover {
        background-color: #1a1e24 !important;
        cursor: pointer !important;
      }

      /* Keep last row height when it's not full */
      .lesson-card-spacer { height: 90px; }
    </style>
    """, unsafe_allow_html=True)

    def _url_with(**updates) -> str:
        params = dict(st.query_params)
        params.setdefault("user", "student")
        params.update(updates)
        return "?" + urlencode(params, doseq=True)

    for _, modules in all_modules.items():
        for start in range(0, len(modules), per_row):
            row = modules[start:start + per_row]
            cols = st.columns(per_row)

            for i in range(per_row):
                with cols[i]:
                    if i < len(row):
                        m = row[i]
                        label = m["label"]
                        key = m["key"]
                        target = m["target"]

                        if mode == "button":
                            # Same-tab navigation via Python
                            if st.button(f"📚 {label}", key=key, use_container_width=True):
                                session_state.selected_module_path = f"views.{target}"
                                session_state.selected_module_key = key
                                navigate_to(
                                    session_state,
                                    user=st.query_params.get("user", "student"),
                                    page="lessons",
                                    module=key
                                )
                        else:  # mode == "link"
                            # Same-tab URL navigation (styled anchor, not link_button)
                            url = _url_with(page="lessons", lesson=key)
                            st.markdown(
                                f'<a class="lesson-link" href="{url}">📚 {label}</a>',
                                unsafe_allow_html=True
                            )
                    else:
                        st.markdown("<div class='lesson-card-spacer'></div>", unsafe_allow_html=True)