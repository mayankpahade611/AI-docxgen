from git import Repo

def collect_git_history(repo_path, file_path):
    repo = Repo(repo_path)
    commits = list(repo.iter_commits(paths=file_path))
    history = []
    for commit in commits:
        history.append({
            'commit_hash': commit.hexsha,
            'author': commit.author.name,
            'date': commit.committed_datetime.isoformat(),
            'message': commit.message.strip()
        })
    return history