# Bedrock Morse Connector

This project is a Morse code translator that uses a Raspberry Pi and the Bedrock API. It allows users to input Morse code using a push button connected to the Raspberry Pi, and then translates the Morse code into text using the Bedrock API.

## Setup

1. Clone this repository to your local machine.
2. Install the required dependencies.

## Hardware Requirements

- Raspberry Pi
- Push button
- LED

## Software Requirements

- Python 3
- RPi.GPIO library
- Bedrock API

## Usage

1. Connect the push button to the GPIO 17 pin and the LED to the GPIO 18 pin on the Raspberry Pi.
2. Run the `main.py` script.
3. Input Morse code using the push button. The LED will blink according to the Morse code input.
4. The translated text will be printed to the console.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.# bedrock-morse-connector