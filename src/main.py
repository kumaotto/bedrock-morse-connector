from bedrock.connect import execute_bedrock_api
from morse.decode import decode_morse
from morse.input import get_key_info


if __name__ == '__main__':
    print('モールス符号を入力してください。escキーで終了します。')
    morse_code = get_key_info()
    print('morse_code:', morse_code)
    result = decode_morse(morse_code)
    print('result:', result)
    bedrock_result = execute_bedrock_api(result)
    print('bedrock_result:', bedrock_result)
