from morse.const import MORSE_TO_JP


def decode_morse(morse_code: str) -> str:
    
    """
    和文モールス符号を日本語にデコードする

    :param morse_code: 和文モールス符号 (例: '・－・－・ ・・－')
    """

    # 両端の空白を削除
    morse_code = morse_code.strip()
    if not morse_code:
        return ''

    morse_code = morse_code.replace('  ', ' ')
    words = morse_code.split(' ')

    decode_text = ''
    for word in words:
        decode_text += MORSE_TO_JP.get(word, '')

    return decode_text
