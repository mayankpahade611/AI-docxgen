import os 
import re
from collections import defaultdict

def extract_code_entities(base_path: str):

    collected_data = defaultdict(list)
    supported_extensions = (".py", ".js", ".java", ".cpp", ".ts", ".cs")

    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(supported_extensions):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        code = f.read()

                    functions = re.findall(r"def\s+(\w+)\s*\(", code)
                    classes = re.findall(r"class\s+(\w+)\s*[:\(]", code)

                    collected_data[file_path] = {
                        "functions": functions,
                        "classes": classes
                    }
                
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    return collected_data


