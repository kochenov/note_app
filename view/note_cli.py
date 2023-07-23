from utils.logger import AppLogger


class NoteCLI:
    """
    Класс для консольного интерфейса заметок.

    Этот класс обрабатывает команды пользователя и вызывает соответствующие методы
    для работы с заметками.
    """

    def __init__(self, controller):
        """
        Конструктор класса NoteCLI.

        Args:
            controller: Объект класса NoteController для управления заметками.
        """
        self._controller = controller

        # Создаем экземпляр класса AppLogger для настройки логирования
        self._app_logger = AppLogger("note_app.log")
        self._logger = self._app_logger.get_logger()

    def run(self):
        """
        Запустить консольный интерфейс заметок.
        """
        print("Команда {help} выводит список команд")
        while True:
            try:
                command = input("Введите команду: ")
                self._logger.info(f"Получена команда: {command}")
                if command == "add":
                    title = input("Введите заголовок заметки: ")
                    body = input("Введите тело заметки: ")
                    self._controller.add_note(title, body)
                    print("Заметка успешно сохранена")
                elif command == "delete":
                    note_id = int(input("Введите идентификатор заметки для удаления: "))
                    self._controller.delete_note(note_id)
                    print(f"Заметка с идентификатором {note_id} успешно удалена")
                elif command == "edit":
                    self._edit_note()
                elif command == "read":
                    self._read_note()
                elif command == "list":
                    self._print_notes_list()
                elif command == "help":
                    self.print_commands_list()
                elif command == "exit":
                    break
                else:
                    print("Неверная команда. Попробуйте снова.")
            except Exception as e:
                print(f"Произошла ошибка: {str(e)}")

    def print_commands_list(self):
        """
        Вывести список доступных команд.
        """
        print("Список доступных команд:")
        print("add - Добавить новую заметку")
        print("delete - Удалить заметку")
        print("edit - Редактировать заметку")
        print("read - Просмотреть заметку")
        print("list - Вывести список всех заметок")
        print("exit - Выйти из приложения")

    def _edit_note(self):
        """
        Обработать команду редактирования заметки.
        """
        note_id = int(input("Введите идентификатор заметки для редактирования: "))
        note = self._controller.get_note_by_id(note_id)
        if note is None:
            print(f"Заметка с идентификатором {note_id} не найдена")
            return

        print(f"Выбрана заметка с идентификатором {note_id}")
        print("1. Редактировать заголовок")
        print("2. Редактировать тело")
        choice = int(input("Выберите номер действия: "))

        if choice == 1:
            new_title = input("Введите новый заголовок: ")
            self._controller.edit_note_title(note_id, new_title)
            print("Заголовок успешно изменен")
        elif choice == 2:
            new_body = input("Введите новое тело заметки: ")
            self._controller.edit_note_body(note_id, new_body)
            print("Тело заметки успешно изменено")
        else:
            print("Неверный выбор")

    def _read_note(self):
        """
        Обработать команду чтения заметки.
        """
        note_id = int(input("Введите идентификатор заметки для просмотра: "))
        note = self._controller.get_note_by_id(note_id)
        if note is None:
            print(f"Заметка с идентификатором {note_id} не найдена")
            return

        print(f"Заметка с идентификатором {note_id}:")
        print(f"Заголовок: {note.get_title()}")
        print(f"Тело: {note.get_body()}")
        print(f"Дата создания: {note.get_created_at_fr()}")
        print(f"Дата последнего изменения: {note.get_updated_at_fr()}")

    def _print_notes_list(self):
        """
        Вывести список всех заметок, отсортированных по дате создания.
        """
        print(f"Выберите условия сортировки:")
        print("1. Сначала новые заметки")
        print("2. Сначала старые заметки")
        choice = int(input("Выберите номер действия: "))
        if choice == 1:
            notes = self._controller.get_all_notes_sorted_by_created_at()
        elif choice == 2:
            notes = self._controller.get_all_notes_sorted_by_created_at(sort=False)
        else:
            print("Неверный выбор")

        if not notes:
            print("Список заметок пуст.")
        else:
            for note in notes:
                print(f"[ID: {note.get_id()}] {note.get_title()} ({note.get_created_at_fr()})")
