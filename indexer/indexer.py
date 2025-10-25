from utils.nlp_utils import preprocess_text

def build_index(code_data, git_data):
    """
    Combine and organize data from different collectors into a unified structure.
    Returns a list of dictionaries — each representing a file summary.
    """
    indexed_data = []

    for file_path, details in code_data.items():
        file_info = {
            "file": file_path,
            "classes": details.get("classes", []),
            "functions": details.get("functions", []),
            "commits": []
        }

        # Link commit messages related to this file
        related_commits = []
        for commit in git_data:
            msg = clean_text(commit["message"])
            if any(name in msg for name in details.get("functions", [])):
                related_commits.append(msg)

        file_info["commits"] = related_commits or ["No direct commit references found."]
        indexed_data.append(file_info)

    return indexed_data