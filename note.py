# Импорт классов NoteController и NoteCLI из соответствующих модулей
from controller.note_controller import NoteController
from view.note_cli import NoteCLI

# Основная точка входа в программу
if __name__ == "__main__":
    notes_file_path = "./notes.json"  # путь к файлу хранения заметок

    # Создание объекта контроллера NoteController с указанием пути к файлу хранения заметок
    controller = NoteController(notes_file_path)

    # Создание объекта пользовательского интерфейса NoteCLI, связанного с контроллером
    view = NoteCLI(controller)

    # Запуск пользовательского интерфейса для работы с заметками
    view.run()
