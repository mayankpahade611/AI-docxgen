from git import Repo
import os

def extract_git_data(repo_path: str):

    git_data = []
    if not os.path.exists(os.path.join(repo_path, ".git")):
        print("⚠️ No .git directory found. Skipping git analysis.")
        return git_data
    
    try:
        repo = Repo(repo_path)
        for commit in repo.iter_commits():
            git_data.append({
                "author": commit.author.name,
                "message": commit.message.strip(),
                "date": commit.committed_datetime.strftime("%Y-%m-%d")
            })
    except Exception as e:
        print(f"⚠️ Git data extraction failed: {e}")

    return git_data