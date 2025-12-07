"""Note data type"""

from dataclasses import dataclass
from guwendao.article import WordExplanation


@dataclass
class GuwendaoNote:
    """Guwendao note"""

    deck_name = "guwendao"
    model_name = "guwendao"

    sentence: str
    word: str
    explanation: str
    start: str

    @staticmethod
    def from_word_explanation(word: WordExplanation) -> "GuwendaoNote":
        """Generate note from WordExplanation"""
        return GuwendaoNote(word.sentence, word.word, word.explanation, word.start)

    def to_param(self) -> dict:
        """Convert this note in to a dictionary object that can be used in anki connect's api
        Returns:
            dict: converted dict
        """
        return {
            "deckName": self.deck_name,
            "modelName": self.model_name,
            "fields": {
                "sentence": self.word + "<br>" + self.sentence,
                "explanation": self.explanation,
            },
        }
