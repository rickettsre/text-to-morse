"""
A Simple text to morse code converter.
"""

from ghost_logo import logo
from morse import morse
from os import system, name


def clear():
    """Clear the Screen Output"""
    # for Windows
    if name == "nt":
        _ = system("cls")
    # for Mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def morse_to_text(text: str):
    """A function that takes a sentence and converts it to morse code
    Args:
        text (str): String to convert to morse code

    Returns:
        string: Message as morse code

    Raises:
        KeyError: If message contains an unknown symbol.
    """
    message = []
    words = [word for word in text.upper().split(" ")]
    for word in words:
        try:
            for letter in word:
                message.append((morse[letter] + " "))
        except KeyError:
            print(f"{letter} removed from string")
            message.append("_ ")
        code = "".join(message).rstrip("_ ")
    return code


def main():
    encode_msg = True
    while encode_msg:
        clear()
        print(logo)
        text = input("Please enter text to convert to morse\n\n")
        output = morse_to_text(text)
        print(f"\n{text} - as morse code is:\n")
        print(f"{output}\n\n")
        start_again = input(
            f"Would you like to encode another message? 'y' press any other key to exit\n\n"
        ).lower()
        if start_again != "y":
            encode_msg = False


if __name__ == "__main__":
    main()
