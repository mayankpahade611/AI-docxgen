import os
import re
import ast

# SUPPORTED_EXTENSIONS = {
#     ".py": "python",
#     ".js": "javascript",
#     ".ts": "typescript",
#     ".java": "java",
#     ".cpp": "cpp",
#     ".h": "cpp",
#     ".hpp": "cpp",
# }

# def extract_python_elements(code):
#     try:
#         tree = ast.parse(code)
#         functions = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
#         classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
#         return functions, classes
#     except Exception:
#         return [], []
    

# def extract_js_ts_elements(code):
#     func_pattern = r'(?:function\s+(\w+)|(\w+)\s*=\s*\([^)]*\)\s*=>)'
#     class_pattern = r'class\s+(\w+)'
#     functions = [m[0] or m[1] for m in re.findall(func_pattern, code)]
#     classes = re.findall(class_pattern, code)
#     return functions, classes


# def extract_java_elements(code):
#     func_pattern = r'(?:public|private|protected)?\s+(?:static\s+)?[A-Za-z0-9_<>,\[\]]+\s+(\w+)\s*\([^)]*\)\s*\{'
#     class_pattern = r'class\s+(\w+)'
#     functions = re.findall(func_pattern, code)
#     classes = re.findall(class_pattern, code)
#     return functions, classes

# def extract_cpp_elements(code):
#     func_pattern = r'[A-Za-z_][A-Za-z0-9_:<>,\[\]\s*&]*\s+(\w+)\s*\([^)]*\)\s*\{'
#     class_pattern = r'class\s+(\w+)'
#     functions = re.findall(func_pattern, code)
#     classes = re.findall(class_pattern, code)
#     return functions, classes

# def extract_elements_by_language(ext, code):
#     lang = SUPPORTED_EXTENSIONS.get(ext, None)
#     if not lang:
#         return [], []

#     if lang == "python":
#         return extract_python_elements(code)
#     elif lang in ["javascript", "typescript"]:
#         return extract_js_ts_elements(code)
#     elif lang == "java":
#         return extract_java_elements(code)
#     elif lang == "cpp":
#         return extract_cpp_elements(code)
#     else:
#         return [], []

# def collect_code_data(repo_path):
#     code_data = []
    
#     for root, _, files in os.walk(repo_path):
#         for file in files:
#            ext = os.path.splitext(file)[1].lower()
#            if ext not in SUPPORTED_EXTENSIONS:
#                continue
           
#            file_path = os.path.join(root, file)
#            try:
#                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
#                    code = f.read()

#                functions, classes = extract_elements_by_language(ext, code)

#                code_data.append({
#                     "file": file_path,
#                     "language": SUPPORTED_EXTENSIONS[ext],
#                     "functions": functions,
#                     "classes": classes,
#                     "commits": []  # placeholder for linking git data later
#                 })

#            except Exception as e:
#                print(f"Error processing file {file_path}: {e}")

#     return code_data

# import re
# import os

# def extract_code_entities(code):
#     """Extract function and class names from Python, JS, TS, or similar languages."""
#     function_patterns = [
#         r'def\s+(\w+)\s*\(',                     # Python
#         r'function\s+(\w+)\s*\(',                # JavaScript/TypeScript
#         r'const\s+(\w+)\s*=\s*\(.*?\)\s*=>',     # JS/TS arrow functions
#         r'(\w+)\s*=\s*function\s*\(',            # JS assigned functions
#         r'(?:(?:public|private|protected)\s+)?(?:static\s+)?(\w+)\s*\(.*?\)\s*\{',  # Java/C++
#     ]

#     class_patterns = [
#         r'class\s+(\w+)',                        # Python / JS / TS / Java / C++
#     ]

#     functions, classes = set(), set()
#     for pattern in function_patterns:
#         functions.update(re.findall(pattern, code))
#     for pattern in class_patterns:
#         classes.update(re.findall(pattern, code))

#     return list(functions), list(classes)


import os
import re
from collections import defaultdict

def extract_code_entities(code: str):
    """
    Extract function and class names from Python, JS, TS, Java, or C++ code.
    Handles async, arrow, and export patterns.
    """
    function_patterns = [
        r'def\s+(\w+)\s*\(',                            # Python
        r'function\s+(\w+)\s*\(',                       # JS/TS normal functions
        r'export\s+function\s+(\w+)\s*\(',               # exported functions
        r'const\s+(\w+)\s*=\s*(?:async\s*)?\(.*?\)\s*=>', # arrow functions with async
        r'(\w+)\s*=\s*\(.*?\)\s*=>',                    # arrow functions
        r'(\w+)\s*=\s*function\s*\(',                   # JS assigned functions
        r'(?:(?:public|private|protected)\s+)?(?:static\s+)?(\w+)\s*\(.*?\)\s*\{',  # Java/C++
    ]

    class_patterns = [
        r'class\s+(\w+)',                               # Python / JS / TS / Java / C++
    ]

    functions, classes = set(), set()

    for pattern in function_patterns:
        for match in re.findall(pattern, code):
            if match not in {"if", "for", "while", "switch"}:
                functions.add(match)

    for pattern in class_patterns:
        classes.update(re.findall(pattern, code))

    return list(functions), list(classes)



def collect_code_data(project_path: str, summary: bool = True):
    """
    Traverse the given project directory, read source files,
    and extract functions & classes for supported languages.
    If summary=True, also returns a summary of language usage and modularity.
    """
    supported_extensions = {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.ts': 'TypeScript',
        '.tsx': 'TypeScript (React)',
        '.java': 'Java',
        '.cpp': 'C++',
        '.h': 'C/C++ Header',
        '.hpp': 'C++ Header'
    }

    collected_data = []
    language_stats = defaultdict(lambda: {'files': 0, 'functions': 0, 'classes': 0})

    for root, _, files in os.walk(project_path):
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext in supported_extensions:
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        code = f.read()

                    functions, classes = extract_code_entities(code)

                    collected_data.append({
                        'file': file_path,
                        'language': supported_extensions[ext],
                        'functions': functions,
                        'classes': classes,
                        'commits': []
                    })

                    # Update summary stats
                    lang = supported_extensions[ext]
                    language_stats[lang]['files'] += 1
                    language_stats[lang]['functions'] += len(functions)
                    language_stats[lang]['classes'] += len(classes)

                except Exception as e:
                    print(f"⚠️ Error reading {file_path}: {e}")

    if not summary:
        return collected_data

    # Generate summary
    summary_data = {
        'total_files': sum(lang['files'] for lang in language_stats.values()),
        'total_functions': sum(lang['functions'] for lang in language_stats.values()),
        'total_classes': sum(lang['classes'] for lang in language_stats.values()),
        'languages': dict(language_stats)
    }

    return collected_data, summary_data





