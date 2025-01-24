def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text: The input text (must be a string).

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize result string
    result = ""

    # Loop through the text
    i = 0
    while i < len(text):
        char = text[i]
        result += char

        # Add 2 new lines after a punctuation mark
        if char in ".:?":
            result += "\n\n"
            # Skip all spaces after punctuation
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    # Strip unnecessary spaces for each line and remove extra trailing newlines
    lines = [line.strip() for line in result.splitlines()]
    final_result = "\n".join(lines)

    print(final_result)
