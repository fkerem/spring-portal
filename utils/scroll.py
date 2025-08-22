import streamlit.components.v1 as components


def force_scroll_to_top():
    components.html("""
        <script>
        function waitForScrollTarget(attempts = 10) {
            const target = window.parent.document.querySelector('section.main');
            if (target) {
                target.scrollTo({ top: 0, behavior: "auto" });
            } else if (attempts > 0) {
                setTimeout(() => waitForScrollTarget(attempts - 1), 100);
            }
        }
        waitForScrollTarget();
        </script>
    """, height=0)