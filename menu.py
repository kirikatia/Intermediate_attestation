from datetime import datetime

class Menu:
    def main_menu(self):
        print('Выберите команду меню:')
        print('1. Показать все заметки')
        print('2. Добавить заметку')
        print('3. Изменить заметку')
        print('4. Удалить заметку')
        print('5. Найти заметку по тексту')
        print('6. Найти заметку по дате')
        print('0. Выйти из приложения\n')
        return self.input_menu()

    def input_menu(self):
        while True:
            try:
                choice = int(input('Введите пункт меню: '))
                if choice in range (1, 7) or choice == 0: 
                    return choice
                else:
                    print('Такого пункта меню нет. Внимательнее, пожалуйста')
            except:
                print('Ошибка ввода. Введите корректный пункт меню')

    def print_notebook(self, notes):
        print()
        if len(notes) < 1:
            print('Заметок нет\n')
            print()
            return

        for note in notes:
            print(f'{note.id} {note.text} (Created: {note.date_created.strftime("%Y-%m-%d %H:%M:%S")}, Modified: {note.date_modified.strftime("%Y-%m-%d %H:%M:%S")})')
        print()

    def input_new_note(self):
        text = input('Введите заметку: ')
        print()
        return text

    def input_remove_note(self):
        id = int(input('Введите ID заметки, которую стоит удалить: '))
        return id

    def input_search(self):
        return input('Введите строку для поиска заметки: ')

    def parse_date(self, date_str):
        formats = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d', '%Y-%m-%dT%H:%M:%SZ']
        date = None
        for fmt in formats:
            try:
                date = datetime.strptime(date_str, fmt)
            except ValueError:
                pass
        return date

    def input_search_by_date(self):
        date_start = self.parse_date(input('Введите дату начала интервала: '))
        date_end = self.parse_date(input('Введите дату конца интервала: '))
        
        return date_start, date_end

    def print_not_found(self):
        print('Не найдено заметок подходящих под заданный запрос')

    def input_edit_note_id(self):
        id = int(input('Введите ID заметки для редактирования: '))
        return id

    def input_edit_note_data(self, current_note):
        print('Задайте новый текст заметки, пусто - оставить без редактирования')
        text = input(f'Введите новый текст заметки ({current_note.text}): ')
        print()
        return text

    def print_error_not_in_book(self,id):
        print(f'Введенный идентификатор {id} отсуствует \n')

