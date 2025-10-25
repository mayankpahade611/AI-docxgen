from collectors.code_collector import extract_code_entities
from collectors.git_collector import extract_git_data
from generator.doc_generator import generate_docs


def main():
    repo_path = "C:/Projects/MyApp"  # 👈 change to your repo path

    print("Collecting code information...")
    code_data = extract_code_entities(repo_path)

    print("Extracting git history...")
    git_data = extract_git_data(repo_path)

    print("Generating documentation using AI model...")
    generate_docs(code_data, git_data)

    print("Documentation generation complete! Check the 'output/docs' folder.")


if __name__ == "__main__":
    main()