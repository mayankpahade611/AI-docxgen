from git import Repo
import os

def collect_git_history(repo_path):
    repo = Repo(repo_path)
    # git_data = []

    # for root, _, files in os.walk(repo_path):
    #     for file in files:
    #         file_path  = os.path.join(root, file)
    #         try:

    #             commits = list(repo.iter_commits(paths = file_path, max_count=20))
    #             commit_data = []
    #             for c in commits:
    #                 commit_data.append({
    #                     "hash": c.hexsha,
    #                     "author": c.author.name,
    #                     "date": c.committed_datetime.strftime("%Y-%m-%d %H:%M:%S"),
    #                     "message": c.message.strip()
    #                 })

    #             git_data.append({
    #                 "file": file_path,
    #                 "commits": commit_data
    #             })
            
    #         except Exception as e:
    #             print(f"Could not fetch commits for {file_path}: {e}")

    # return git_data
    commits_data = []


    for commit in repo.iter_commits():
        for file_path in commit.stats.files.keys():
            commits_data.append({
                "file": os.path.relpath(file_path, repo_path),
                "commit_hash": commit.hexsha,
                "author": commit.author.name,
                "date": commit.committed_datetime.isoformat(),
                "message": commit.message.strip()
            })

    return commits_data