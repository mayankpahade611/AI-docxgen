from transformers import pipeline
import os
from utils.file_utils import save_markdown

def generate_docs(code_data, git_data):

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    summary_text = "Project Documentation\n\n"

    summary_text += "## Code Overview\n"
    for file_path, details in code_data.items():
        summary_text += f"### `{file_path}`\n"
        if details["classes"]:
            summary_text += f"**Classes:** {', '.join(details['classes'])}\n\n"
            
        if details["functions"]:
            summary_text += f"**Funcitons:** {', '.join(details['functions'])}\n\n"


    summary_text += "## Git Commit History\n"
    commit_text = " ".join([item["message"]] for item in git_data[:30])
    if commit_text:
        summary = summarizer(commit_text, max_length=100, min_length=10, do_sample=False)[0]['summary_text']
        summary_text += f"{summary}\n"

    else:
        summary_text += "No commit found.\n"

    save_markdown(summary_text, "output/docs/documentation.md")
