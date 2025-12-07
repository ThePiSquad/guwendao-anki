"""Guwendao Anki integration"""

import argparse
# from loguru import logger
from guwendao import Client
from anki import AnkiClient
from anki.note import GuwendaoNote

# logger.disable("guwendao")

parser = argparse.ArgumentParser(
    description="A tool that generate anki notes from guwendao"
)
parser.add_argument("url", type=str, help="Url to the article page")
parser.add_argument("-c", action="store_true", help="Run without create anki notes")

args = parser.parse_args()


guwendao = Client()
article = guwendao.get_article_from_url(args.url)
words = article.get_world_explanations()

if args.c:
    anki = AnkiClient()
    notes = [GuwendaoNote.from_word_explanation(word) for word in words]
    anki.add_notes(notes)
