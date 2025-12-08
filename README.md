This is a tool that allows you to fetch word explanations from guwendao(古文岛) and import then into your anki deck

## Preparation
### Anki
1. Install the [anki-connect](https://ankiweb.net/shared/info/2055492159) plugin
2. Create a model with the following fields
   1. sentence: the front of the card, which will contain the word and the sentence
   2. explanation: the back of the card, which will contain the explanation
3. Keep you anki open while using this script
### Guwendao
- You need to copy the url to the article you are hoping to translate and use it as an argument.
- You need to login first for the script to load the detailed part of the translation. 
- You may also need an VIP account for unlimited API usage

## Usage
```
# clone this reo
git clone https://github.com/ThePiSquad/guwendao-anki
cd guwendao-anki
```

```
# dry-run
uv run python main.py <url> 
# create notes
# dry-run
uv run python main.py <url> -c
```