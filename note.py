from datetime import datetime

class Note:
    def __init__(self, id, text, date_created=None, date_modified=None):
        self.id = id
        self.text = text
        self.date_created = datetime.fromisoformat(date_created) if date_created else datetime.now()
        self.date_modified = datetime.fromisoformat(date_modified) if date_modified else datetime.now()