def clean_linked_data(linked_data):

    cleaned_data = []

    for entry in linked_data:
        functions = [f for f in entry.get("functions", []) if f]
        classes = [c for c in entry.get("classes", []) if c]
        commits = [
            {
                "hash": c["hash"],
                "author": c.get("author", "Unknown").strip(),
                "message": c.get("message", "").strip(),
                "files": c.get("files", [])
            } for c in entry.get("commits", [])
        ]
        cleaned_data.append({
            "file": entry.get("file"),
            "functions": functions,
            "classes": classes,
            "commits": commits
        })

    return cleaned_data