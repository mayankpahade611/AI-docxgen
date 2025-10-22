import os
import re
import ast

SUPPORTED_EXTENSIONS = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".java": "java",
    ".cpp": "cpp",
    ".h": "cpp",
    ".hpp": "cpp",
}

def extract_python_elements(code):
    try:
        tree = ast.parse(code)
        functions = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
        classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
        return functions, classes
    except Exception:
        return [], []
    

def extract_js_ts_elements(code):
    func_pattern = r'(?:function\s+(\w+)|(\w+)\s*=\s*\([^)]*\)\s*=>)'
    class_pattern = r'class\s+(\w+)'
    functions = [m[0] or m[1] for m in re.findall(func_pattern, code)]
    classes = re.findall(class_pattern, code)
    return functions, classes


def extract_java_elements(code):
    func_pattern = r'(?:public|private|protected)?\s+(?:static\s+)?[A-Za-z0-9_<>,\[\]]+\s+(\w+)\s*\([^)]*\)\s*\{'
    class_pattern = r'class\s+(\w+)'
    functions = re.findall(func_pattern, code)
    classes = re.findall(class_pattern, code)
    return functions, classes

def extract_cpp_elements(code):
    func_pattern = r'[A-Za-z_][A-Za-z0-9_:<>,\[\]\s*&]*\s+(\w+)\s*\([^)]*\)\s*\{'
    class_pattern = r'class\s+(\w+)'
    functions = re.findall(func_pattern, code)
    classes = re.findall(class_pattern, code)
    return functions, classes

def extract_elements_by_language(ext, code):
    lang = SUPPORTED_EXTENSIONS.get(ext, None)
    if not lang:
        return [], []

    if lang == "python":
        return extract_python_elements(code)
    elif lang in ["javascript", "typescript"]:
        return extract_js_ts_elements(code)
    elif lang == "java":
        return extract_java_elements(code)
    elif lang == "cpp":
        return extract_cpp_elements(code)
    else:
        return [], []

def collect_code_data(repo_path):
    code_data = []
    
    for root, _, files in os.walk(repo_path):
        for file in files:
           ext = os.path.splitext(file)[1].lower()
           if ext not in SUPPORTED_EXTENSIONS:
               continue
           
           file_path = os.path.join(root, file)
           try:
               with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                   code = f.read()

               functions, classes = extract_elements_by_language(ext, code)

               code_data.append({
                    "file": file_path,
                    "language": SUPPORTED_EXTENSIONS[ext],
                    "functions": functions,
                    "classes": classes,
                    "commits": []  # placeholder for linking git data later
                })

           except Exception as e:
               print(f"Error processing file {file_path}: {e}")

    return code_data