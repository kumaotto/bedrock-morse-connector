import RPi.GPIO as GPIO
import time

from bedrock.connect import execute_bedrock_api
from morse.decode import decode_morse
from morse.encode import encode_morse

# bedrock settings
MODEL_ID = 'anthropic.claude-3-sonnet-20240229-v1:0'
MAX_TOKENS = 1000

# raspberry pi settings
GPIO.setmode(GPIO.BCM)

PUSH_SWICH_PIN = 17
LED_PIN = 18

GPIO.setup(PUSH_SWICH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)


def convert_to_morse(time_in_seconds):

    if time_in_seconds < 0.3:
        return '.'
    
    else:
        return '-'


def debounce(pin, debounce_time=0.02):
    
    start = time.time()

    while time.time() - start < debounce_time:
        if GPIO.input(pin) != GPIO.LOW:
            return False
    
    return True


def blink_morse_code(message):

    dot_delay = 0.25

    try:
        for symbol in message:

            if symbol == '.':
                GPIO.output(LED_PIN, GPIO.HIGH)
                time.sleep(dot_delay)
            
            elif symbol == '-':
                GPIO.output(LED_PIN, GPIO.HIGH)
                time.sleep(dot_delay * 3)
            
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(dot_delay)
        
        time.sleep(dot_delay * 2)
        
    finally:
        GPIO.cleanup()


def input_morse():
    
    morse_code = ''
    release_time = None
    
    try:
        
        while True:
            
            if GPIO.input(PUSH_SWICH_PIN) == GPIO.LOW and debounce(PUSH_SWICH_PIN):
            
                start_time = time.time()
                end_time = 0
                release_time = time.time()
                                                                
                while GPIO.input(PUSH_SWICH_PIN) == GPIO.LOW:
                    time.sleep(0.01)
                
                if GPIO.input(PUSH_SWICH_PIN) == GPIO.HIGH:
                    end_time = time.time()
                
                press_duration = end_time - start_time
                
                morse_code += convert_to_morse(press_duration)
                print('morse code: ', morse_code)
                            
            else:
                
                if release_time is None:
                    continue
                    
                release_duration = time.time() - release_time
                
                if release_duration > 1.5 and (not morse_code.endswith(' ')):
                    morse_code += ' '
                    print('morse code: ', morse_code)
                
                if release_duration > 3.0 and morse_code.endswith(' '):
                    break
            
            time.sleep(0.1)
                
        return morse_code
        
    except Exception as e:
        print(f'error occuerd: {e}')
    
    finally:
        GPIO.cleanup()


def main():

    morse_code = input_morse()
    print('Received morse codes:', morse_code)
    message = decode_morse(morse_code)
    print('message:', message)
    bedrock_message = execute_bedrock_api(message)
    print('response message from bedrock: ', bedrock_message)
    encode_message = encode_morse(bedrock_message)
    print('encode_message: ', encode_message)
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    blink_morse_code(encode_message)


if __name__ == '__main__':
    main()
