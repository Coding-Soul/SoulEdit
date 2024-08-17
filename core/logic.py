import os


def save_note(path: str, text):
    with open(path, 'w') as file:
        file.write(text)
        file.close()


def open_note(path: str):
    with open(path, 'r') as file:
        text = file.read()
        filename = os.path.basename(path)
        filename_without_ext = os.path.splitext(filename)[0]

        value = [filename_without_ext, text]

        return value
