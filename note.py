from controller.note_controller import NoteController
from view.note_cli import NoteCLI

if __name__ == "__main__":
    notes_file_path = "notes.json"  # Задайте путь к файлу хранения заметок
    controller = NoteController(notes_file_path)
    view = NoteCLI(controller)
    view.run()
