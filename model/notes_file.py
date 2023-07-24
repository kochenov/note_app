import datetime
import json
from typing import List
from model.abstract_note import AbstractNote


class NotesFile:
    """
    Класс для работы с хранилищем заметок.

    Этот класс отвечает за сохранение, чтение, добавление, редактирование
    и удаление заметок в файле.
    """

    def __init__(self, file_path: str):
        """
        Конструктор класса NotesFile.

        Args:
            file_path (str): Путь к файлу хранения заметок.
        """
        self._file_path = file_path

    def _read_notes_from_file(self) -> List[AbstractNote]:
        """
        Приватный метод для чтения заметок из файла.

        Returns:
            List[AbstractNote]: Список объектов заметок.
        """
        try:
            with open(self._file_path, "r") as file:
                data = json.load(file)

                notes = []
                for note_data in data:
                    note = AbstractNote(
                        note_data["id"],
                        note_data["title"],
                        note_data["body"]
                    )
                    note._created_at = datetime.datetime.fromisoformat(note_data["created_at"])
                    note._updated_at = datetime.datetime.fromisoformat(note_data["updated_at"])

                    notes.append(note)
                return notes
        except FileNotFoundError:
            # Если файл не найден, возвращаем пустой список
            return []

    def save_notes(self, notes: List[AbstractNote]) -> None:
        data = []
        for note in notes:
            note_data = {
                "id": note.get_id(),
                "title": note.get_title(),
                "body": note.get_body(),
                "created_at": note.get_created_at().isoformat(),
                "updated_at": note.get_updated_at().isoformat()
            }
            data.append(note_data)
        with open(self._file_path, "w") as file:
            json.dump(data, file, indent=4)

    def load_notes(self) -> List[AbstractNote]:
        """
        Загрузить заметки из файла.

        Returns:
            List[AbstractNote]: Список объектов заметок.
        """
        return self._read_notes_from_file()

