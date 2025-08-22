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

def render_module_nav(session_state, all_modules):
    # Button styling
    st.markdown(
        """
        <style>
        div.stButton > button {
            background-color: #0e1117;
            color: white;
            border: 1px solid #444;
            border-radius: 10px;
            width: 100%;
            height: 90px;
            white-space: normal;
            padding: 10px;
            font-size: 14px;
            line-height: 1.2;
            overflow-wrap: break-word;
        }
        div.stButton > button:hover {
            background-color: #1a1e24;
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    for _, modules in all_modules.items():
        # Split into rows of 5
        for row_start in range(0, len(modules), 5):
            row = modules[row_start:row_start + 5]

            # Dynamically adapt to number of modules (use len(row) not 5)
            cols = st.columns(len(row))

            for col, m in zip(cols, row):
                label = m["label"]
                key = m["key"]
                target = m["target"]

                with col:
                    if st.button(f'📚 {label}', key=key):
                        session_state.selected_module_path = f"views.{target}"
                        session_state.selected_module_key = key
                        navigate_to(
                            session_state,
                            user=st.query_params.get("user", "student"),
                            page="lessons",
                            module=key
                        )