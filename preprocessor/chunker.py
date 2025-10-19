def chunk_code(file_entry, max_lines=50):

    chunks = []

    for func in file_entry.get("functions", []):
        start = func.get("linenp", 0)

        end = start + max_lines
        chunks.append({
            "file": file_entry.get["file"],
            "type": "function",
            "name": func.get["name"],
            "start_line": start,
            "end_line": end
        })

        for cls in file_entry.get("classes", []):

            chunks.append({
                "file": file_entry.get["file"],
                "type": "class",
                "name": cls["name"],
                "start_line": None,
                "end_line": None
            })

    return chunks
