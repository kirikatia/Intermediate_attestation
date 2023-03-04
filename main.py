
from notebook import Notebook
from note import Note
from storage import JsonFileStorage
from menu import Menu

notebook = Notebook(JsonFileStorage('notes.json'))
menu = Menu()

while True:
    choice = menu.main_menu()

    if choice == 0:
        break

    elif choice == 1:
        menu.print_notebook(notebook.get_all_notes())

    elif choice == 2:
        text = menu.input_new_note()
        notebook.add_note(Note(notebook.get_next_id(), text))

    elif choice == 3:
        id = menu.input_edit_note_id()
        current_note = notebook.find_note_by_id(id)
        if current_note is None:
            menu.print_error_not_in_book()
            continue
        notebook.modify_note(id, menu.input_edit_note_data(current_note))

    elif choice == 4:
        id = menu.input_remove_note()
        current_note = notebook.find_note_by_id(id)
        if current_note is None:
            menu.print_error_not_in_book()
            continue
        notebook.delete_note(id)

    elif choice == 5:
        text = menu.input_search()
        notes = notebook.find_notes_by_text(text)
        menu.print_notebook(notes)

    elif choice == 6:
        date_start, date_end = menu.input_search_by_date()
        notes = notebook.find_notes_by_date(date_start, date_end)
        menu.print_notebook(notes)

