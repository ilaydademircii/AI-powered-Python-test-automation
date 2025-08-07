'''
Created on 3 Ağu 2024

@author: zehra
'''
import requests
######################################################


def comment_first_triple_quote_python(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if lines and lines[0].strip().startswith("'''python"):
        lines[0] = f"# {lines[0]}"

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)


# Kullanım örneği
file_path = 'path/to/your/script.py'  # Burada dosya yolunu belirtin
comment_first_triple_quote_python(file_path)
