import os


def generate_text_file(content, filename="generated_notes.txt"):

    os.makedirs("generated_files", exist_ok=True)

    filepath = os.path.join("generated_files", filename)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

    return filepath