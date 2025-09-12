# CAPTCHA Generator

This Python script generates a CAPTCHA image with random text and distorted characters.

## Features

- Random text (letters and digits)
- Character distortion (rotation, random position)
- Noise (lines and dots)
- Optional Gaussian blur for extra difficulty

## Requirements

- Python 3.x
- [Pillow](https://python-pillow.org/) library

Install dependencies:
```bash
pip install pillow
```

## Usage

1. Place a TTF font file (e.g. `arial.ttf`) in the script directory, or the script will fall back to a default font.
2. Run the script:
    ```bash
    python generate_captcha.py
    ```
3. The script will generate a file named `captcha.png` in the current directory and print the generated CAPTCHA text.

## Customization

- Change the `length` argument in `generate_captcha()` to set the number of characters in the CAPTCHA.
- Change the output filename by setting the `filename` parameter.

## Example

Generated image:

![Example CAPTCHA](captcha.png)

## License

MIT License
