from morse.decode import decode_morse
from morse.input import get_key_info


if __name__ == '__main__':
    print('start morse code decoder...')
    morse_code = get_key_info()
    print('morse_code:', morse_code)
    result = decode_morse(morse_code)
    print('result:', result)
