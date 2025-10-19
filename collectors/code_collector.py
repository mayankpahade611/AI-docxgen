import os
import ast

def collect_code_data(repo_path):
    code_data = []
    
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        file_content = f.read()
                        tree = ast.parse(file_content)
                        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
                        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
                        
                        code_data.append({
                            'file_path': file_path,
                            'functions': functions,
                            'classes': classes
                        })
                    except (SyntaxError, UnicodeDecodeError):
                        continue
    return code_data