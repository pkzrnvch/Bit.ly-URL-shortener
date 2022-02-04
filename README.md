# Bitly url shortener

The script allows you to shorten links using the [Bit.ly](https://bitly.com) service, and also to find out how many times your shortened Bit.ly link has been used.

## How to install

- Create a [Bit.ly](https://bitly.com) account and generate your token.

- Program fetches token from the environment variable BITLY_TOKEN, so you should set it by creating an .env file containing:
```bash
BITLY_TOKEN=YOUR_TOKEN
```
- Python3 should already be installed. Use pip (or pip3, in case of conflict with Python2) to install dependencies:

```bash
$pip install -r requirements.txt
```

```bash
$python3 main.py "Long URL to shorten or Bit.ly url to get a clicks count"
```

## Usage examples

```python
>python main.py https://www.spacex.com
https://bit.ly/3J5tV3G

>python main.py https://bit.ly/3J5tV3G
По вашей ссылке прошли: 2 раз(а)
```

## Project Goals

The code is written for educational purposes on online-course for web-developers [Devman](https://dvmn.org).
