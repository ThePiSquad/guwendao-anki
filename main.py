"""Guwendao Anki integration"""

from guwendao import Client
from anki import AnkiClient
from anki.note import GuwendaoNote


def main():
    """Main function"""
    guwendao = Client()
    article = guwendao.get_article_from_url(
        "https://www.gushiwen.cn/shiwenv_e0022a7b82a0.aspx"
    )
    words = article.get_world_explanations()

    anki = AnkiClient()
    notes = [GuwendaoNote.from_word_explanation(word) for word in words]
    anki.add_notes(notes)


if __name__ == "__main__":
    main()
