import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

def createPage():
    st.subheader("📘 Teacher Module Guide")
    st.write("""
    This guide includes everything educators need to successfully teach the IoT4Ag modules:
    
    - ✅ Step-by-step lesson plans  
    - 🛠️ Classroom-ready lesson materials  
    - 🎥 Linked tutorials to demonstrate setup and usage
    
    Download or preview the PDF below:
    """)

    # Replace with actual file path or URL to your PDF
    pdf_path = "documents/spring-module.pdf"  # Can also be a URL or bytes

    # Add a download button
    with open(pdf_path, "rb") as file:
        st.download_button(
            label="📥 Download Teacher Module (PDF)",
            data=file,
            file_name="spring-module.pdf",
            mime="application/pdf",
            key="download-pdf-teacher-guide"
        )

    pdf_viewer(pdf_path, 
        zoom_level="auto",                    # 120% zoom
        viewer_align="center",             # Center alignment
        #width=700,
        height=1000,
        show_page_separator=True           # Show separators between pages)
        )