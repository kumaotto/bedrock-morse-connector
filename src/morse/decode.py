from morse.const import MORSE_CODE_JP


def decode_morse(morse_code: str) -> str:
    """
    Decode morse code to text.
    """
    morse_code = morse_code.strip()
    if not morse_code:
        return ''

    morse_code = morse_code.replace('  ', ' ')
    words = morse_code.split(' ')
    text = ''
    for word in words:
        if word:
            text += MORSE_CODE_JP.get(word, '')

    return text
