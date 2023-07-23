from datetime import datetime

from model.note import AbstractNote
from model.notes_file import NotesFile
from typing import List


class NoteController:
    """
    Класс-контроллер для работы с заметками.

    Этот класс связывает модель (заметки) с представлением (консольный интерфейс).
    Он отвечает за добавление, удаление, редактирование, чтение и управление заметками.
    """

    def __init__(self, notes_file_path: str):
        """
        Конструктор класса NoteController.

        Args:
            notes_file_path (str): Путь к файлу хранения заметок.
        """
        self._notes_file = NotesFile(notes_file_path)
        self._notes = self._notes_file.load_notes()

    def add_note(self, title: str, body: str) -> None:
        """
        Добавить новую заметку.

        Args:
            title (str): Заголовок заметки.
            body (str): Тело заметки.
        """
        note_id = self._generate_note_id()
        new_note = AbstractNote(note_id, title, body)
        self._notes.append(new_note)
        self._notes_file.save_notes(self._notes)

    def delete_note(self, note_id: int) -> None:
        """
        Удалить заметку по ее идентификатору.

        Args:
            note_id (int): Идентификатор заметки.
        """
        self._notes = [note for note in self._notes if note.get_id() != note_id]
        self._notes_file.save_notes(self._notes)

    def edit_note_title(self, note_id: int, new_title: str) -> None:
        """
        Редактировать заголовок заметки.

        Args:
            note_id (int): Идентификатор заметки.
            new_title (str): Новый заголовок заметки.
        """
        for note in self._notes:
            if note.get_id() == note_id:
                note.set_title(new_title)
                note._updated_at = datetime.now()
                break
        self._notes_file.save_notes(self._notes)

    def edit_note_body(self, note_id: int, new_body: str) -> None:
        """
        Редактировать тело заметки.

        Args:
            note_id (int): Идентификатор заметки.
            new_body (str): Новое тело заметки.
        """
        for note in self._notes:
            if note.get_id() == note_id:
                note.set_body(new_body)
                note._updated_at = datetime.now()
                break
        self._notes_file.save_notes(self._notes)

    def get_note_by_id(self, note_id: int) -> AbstractNote:
        """
        Получить заметку по ее идентификатору.

        Args:
            note_id (int): Идентификатор заметки.

        Returns:
            AbstractNote: Объект заметки.
        """
        for note in self._notes:
            if note.get_id() == note_id:
                return note
        return None

    def get_all_notes(self) -> List[AbstractNote]:
        """
        Получить все заметки.

        Returns:
            List[AbstractNote]: Список объектов заметок.
        """
        return self._notes

    def _generate_note_id(self) -> int:
        """
        Сгенерировать уникальный идентификатор для заметки.

        Returns:
            int: Уникальный идентификатор заметки.
        """
        max_id = max(self._notes, key=lambda note: note.get_id()).get_id() if self._notes else 0
        new_id = max_id + 1
        while any(note.get_id() == new_id for note in self._notes):
            new_id += 1
        return new_id

    def get_all_notes_sorted_by_created_at(self, sort=True) -> List[AbstractNote]:
        """
        Получить список всех заметок, отсортированных по дате создания.

        Returns:
            List[AbstractNote]: Список объектов заметок, отсортированных по дате создания.
        """
        return sorted(self._notes, key=lambda note: note.get_created_at(), reverse=sort)