import os

replacements = {
    'static': 'progblog/static',
    'media': 'progblog/media',
    'posts': 'progblog/posts',
    'tags': 'progblog/tags',
    'pages': 'progblog/pages'
}

current_dir = os.getcwd()
for root, dirs, files in os.walk(current_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            updated_content = content
            for old_string, new_string in replacements.items():
                if old_string in updated_content:
                    updated_content = updated_content.replace(old_string, new_string)

            if updated_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"Изменения внесены в файл: {file_path}")
