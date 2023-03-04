# Информация о проекте
# Необходимо написать проект, содержащий функционал работы с заметками. Программа должна уметь создавать заметку, сохранять её, читать список заметок, редактировать заметку, удалять заметку.

# Как сдавать проект
# Для сдачи проекта необходимо создать отдельный общедоступный репозиторий (Github, gitlub, или Bitbucket). Разработку вести в этом репозитории, использовать пул реквесты на изменения. Программа должна запускаться и работать, ошибок при выполнении программы быть не должно.

# Критерии оценки
# Приложение должно запускаться без ошибок, должно уметь сохранять данные в файл, уметь читать данные из файла, делать выборку по дате, выводить на экран выбранную запись, выводить на экран весь список записок, добавлять записку, редактировать ее и удалять.



# Для реализации проекта по управлению заметками на языке Python, вам нужно использовать следующие шаги:

# Создать класс Note, который будет представлять заметку.
#  Класс должен иметь следующие атрибуты: id - уникальный идентификатор заметки, text - текст заметки, date_created - дата создания заметки, date_modified - дата последнего изменения заметки.
# Пример:

import datetime

class Notebook:
    def __init__(self, storage):
        self.storage = storage
        self.notes = self.load_notes()
        
    def get_next_id(self):
        if len(self.notes) == 0:
            return 1

        max_note_id = max([x.id for x in self.notes])
        return max_note_id + 1

    def add_note(self, note):
        self.notes.append(note)
        self.save_notes()

    def modify_note(self, note_id, text):
        note = self.find_note_by_id(note_id)
        note.text = text
        note.date_modified = datetime.datetime.now()
        self.save_notes()

    def delete_note(self, note_id):
        note = self.find_note_by_id(note_id)
        self.notes.remove(note)
        self.save_notes()

    def find_notes_by_text(self, text):
        matching_notes = []
        for note in self.notes:
            if text in note.text:
                matching_notes.append(note)
        return matching_notes

    def find_notes_by_date(self, date_start, date_end):
        matching_notes = []
        for note in self.notes:
            if date_end is None and date_start <= note.date_created:
                matching_notes.append(note)
                continue

            if date_start is None and note.date_created <= date_end:
                matching_notes.append(note)
                continue

            if date_start <= note.date_created <= date_end:
                matching_notes.append(note)
                continue

        return matching_notes

    def __len__(self):
        return len(self.notes)

    def get_all_notes(self):
        return self.notes

    def find_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note

    def save_notes(self):
        return self.storage.save_notes(self.notes)

    def load_notes(self):
        return self.storage.load_notes()
