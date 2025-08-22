import streamlit as st

def createPage():
    st.subheader("📝 Teacher Notes")
    notes = st.text_area("Use this space for class notes or preparation:", height=300)

    # Download button always shown, but disabled if empty
    st.download_button(
        label="📥 Download Notes",
        data=notes,
        file_name="teacher_notes.txt",
        mime="text/plain",
        disabled=(notes.strip() == "")
    )

    st.info("Note: Your input will remain only for this session unless connected to a persistent user system.")