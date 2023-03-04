import json
from note import Note

class JsonFileStorage:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def save_notes(self, notes):
        with open(self.file_path, 'w') as f:
            notes_json = json.dumps([note.__dict__ for note in notes], default=str)
            f.write(notes_json)

    def load_notes(self):
        try:
            with open(self.file_path, 'r') as f:
                notes_json = f.read()
                notes_data = json.loads(notes_json)
                notes = [Note(**note_data) for note_data in notes_data]
                return notes
        except FileNotFoundError:
            return []