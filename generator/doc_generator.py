# from transformers import pipeline
# import os
# from utils.file_utils import save_markdown

# def generate_docs(code_data, git_data):

#     summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

#     summary_text = "Project Documentation\n\n"

#     summary_text += "## Code Overview\n"
#     for file_path, details in code_data.items():
#         summary_text += f"### `{file_path}`\n"
#         if details["classes"]:
#             summary_text += f"**Classes:** {', '.join(details['classes'])}\n\n"
            
#         if details["functions"]:
#             summary_text += f"**Funcitons:** {', '.join(details['functions'])}\n\n"


#     summary_text += "## Git Commit History\n"
#     commit_text = " ".join(item["message"] for item in git_data[:30])
#     if commit_text:
#         summary = summarizer(commit_text, max_length=100, min_length=10, do_sample=False)[0]['summary_text']
#         summary_text += f"{summary}\n"

#     else:
#         summary_text += "No commit found.\n"

#     save_markdown(summary_text, "output/docs/documentation.md")


import os
from transformers import BartForConditionalGeneration, BartTokenizer
from tqdm import tqdm

def generate_summary(text, model, tokenizer, max_length=150):
    input = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(
        input["input_ids"],
        num_beams=4,
        max_length=max_length,
        min_length=40,
        length_penalty=2.0,
        early_stopping=True
    )
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

def generate_docs(code_data, git_data):
    print("Generating documentation using AI model")

    tokenizer = BartTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
    model = BartForConditionalGeneration.from_pretrained("sshleifer/distilbart-cnn-12-6")


    output_dir = os.path.join("output", "data")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "documentation.md")

    with open(output_path, "w", encoding="utf-8") as doc_file:
        doc_file.write("# Project Documentation\n\n")

        doc_file.write("## Code Overview\n\n")

        for file_path, details in tqdm(code_data.items(), desc="Processing code files"):
            doc_file.write(f"### File: `{file_path}`\n\n")

            functions = details.get("functions", [])
            classes = details.get("classes", [])

            doc_file.write(f"**Functions:** {', '.join(functions) if functions else 'None'}\n\n")
            doc_file.write(f"**Classes:** {', '.join(classes) if classes else 'None'}\n\n")


            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    code_text = f.read()

                combined_text = (
                    f"This code file defines functions: {functions}, and classes: {classes}. "
                    f"Here is the main code content:\n{code_text[:3000]}"  # limit to avoid long input
                )

                summary = generate_summary(combined_text, model, tokenizer)
                doc_file.write(f"**AI Summary:** {summary}\n\n")

            except Exception as e:
                doc_file.write(f"Error reading file content: {e}\n\n")


            doc_file.write("\n## Git Commit History\n")
        if git_data:
            for item in git_data[:30]:
                message = item.get("message", "No message")
                author = item.get("author", "Unknown")
                date = item.get("date", "Unknown date")
                doc_file.write(f"- **{author}** ({date}): {message}\n")
        else:
            doc_file.write("No commit history found.\n")

    print(f"Documentation successfully generated at: {output_path}")