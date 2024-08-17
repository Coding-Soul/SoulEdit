def save_note(path: str, text):
    with open(path, 'w') as file:
        file.write(text)
        file.close()


def open_note(path: str):
    with open(path, 'r') as file:
        text = file.read()
        return text
