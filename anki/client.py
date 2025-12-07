"""AnkiClient that connects the the api exposed by the Anki-connect plugin"""

import requests
from . import error
from .note import GuwendaoNote


class AnkiClient:
    """AnkiClient"""

    address: str

    def __init__(self, address="http://127.0.0.1:8765"):
        self.address = address

    def get_version(self) -> int:
        """Gets the version of the API exposed by anki connect"""
        response = requests.post(
            self.address, timeout=1000, json={"action": "version", "version": 6}
        )
        if response.status_code != 200:
            raise error.RequestError()
        return response.json()["result"]

    def add_note(self, note: GuwendaoNote):
        """Add single note"""
        response = requests.post(
            self.address,
            json={
                "action": "addNote",
                "version": 6,
                "params": {
                    "note": note.to_param(),
                },
            },
            timeout=1000,
        )
        print(response.text)
        print(response.json())

    def add_notes(self, notes: list[GuwendaoNote]):
        """Add notes
        Args:
            notes (list[GuwendaoNote]): notes to be added
        """
        for note in notes:
            self.add_note(note)
