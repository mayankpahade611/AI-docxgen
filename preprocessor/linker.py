def link_commits_to_files(code_data, git_data):

    linked_data = []

    for file_entry in code_data:
        file_path = file_entry.get("file")
        affected_commits = [
            c for c in git_data if file_path in c.get("files", [])
        ]
        linked_data.append({
            "file": file_path,
            "functions": file_entry.get("functions", []),
            "classes": file_entry.get("classes", []),
            "commits": affected_commits
        })
        return linked_data
    