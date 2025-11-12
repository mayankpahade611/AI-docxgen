import streamlit as st
import os
import zipfile
import tempfile
from collectors.code_collector import extract_code_entities
from collectors.git_collector import extract_git_data
from generator.doc_generator import generate_docs

st.set_page_config(page_title="AI Documentation Generator", page_icon="📘")

st.title("📘 AI Documentation Generator")
st.write("Upload a ZIP file of your project to generate documentation using AI.")

# File upload section
uploaded_file = st.file_uploader("📁 Upload your project ZIP file", type=["zip"])

if uploaded_file is not None:
    with tempfile.TemporaryDirectory() as tmpdir:
        zip_path = os.path.join(tmpdir, uploaded_file.name)
        
        # Save the uploaded zip file temporarily
        with open(zip_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Extract zip file contents
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(tmpdir)

        st.info("✅ Project files extracted successfully.")

        if st.button("Generate Documentation"):
            with st.spinner("Analyzing and generating documentation..."):
                # Use the extracted folder as repo_path
                repo_path = tmpdir

                code_data = extract_code_entities(repo_path)
                git_data = extract_git_data(repo_path)
                generate_docs(code_data, git_data)

                st.success("✅ Documentation generated successfully!")

                output_path = os.path.join("output", "data", "documentation.md")
                with open(output_path, "r", encoding="utf-8") as f:
                    content = f.read()

                st.download_button(
                    label="📥 Download Documentation",
                    data=content,
                    file_name="documentation.md",
                    mime="text/markdown"
                )
