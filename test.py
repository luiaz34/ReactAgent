def get_text_length(text: str) -> int:
    """Returns the length of a text by characters"""
    print(f"get_text_length enter with {text=}")
    # Remove specific characters
    text = text.replace("'", "").replace("\n", "").replace('"', "")
    # Strip leading and trailing whitespace
    text = text.replace(" ", "")
    return len(text)


print(get_text_length("khaing myal htike"))
