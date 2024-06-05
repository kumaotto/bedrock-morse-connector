from morse.const import JP_TO_MORSR


def encode_morse(message):
    
    if not message:
        return ''
    
    char_list = list(message)
    
    morse_code_message = ''
    for char in char_list:
        morse_code_message += JP_TO_MORSR.get(char, '')
        morse_code_message += ' '

    return morse_code_message.strip()
