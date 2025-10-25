import os


def ensure_dir(path: str):

    os.makedirs(path, exist_ok=True)


def save_markdown(content: str, filepath: str):

    ensure_dir(os.path.dirname(filepath))
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Saved documentation to {filepath}")