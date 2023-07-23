from abc import ABC, abstractmethod
import datetime


class Note(ABC):
    """
    Интерфейс для заметки.

    Этот интерфейс определяет обязательные методы для получения и установки
    заголовка, тела заметки, даты/времени и других свойств заметки.
    """

    @abstractmethod
    def get_id(self) -> int:
        """
        Получить идентификатор заметки.

        Returns:
            int: Идентификатор заметки.
        """
        pass

    @abstractmethod
    def get_title(self) -> str:
        """
        Получить заголовок заметки.

        Returns:
            str: Заголовок заметки.
        """
        pass

    @abstractmethod
    def set_title(self, title: str) -> None:
        """
        Установить заголовок заметки.

        Args:
            title (str): Новый заголовок заметки.
        """
        pass

    @abstractmethod
    def get_body(self) -> str:
        """
        Получить тело заметки.

        Returns:
            str: Тело заметки.
        """
        pass

    @abstractmethod
    def set_body(self, body: str) -> None:
        """
        Установить тело заметки.

        Args:
            body (str): Новое тело заметки.
        """
        pass

    @abstractmethod
    def get_created_at(self) -> datetime:
        """
        Получить дату/время создания заметки.

        Returns:
            datetime: Дата/время создания заметки.
        """
        pass

    @abstractmethod
    def get_updated_at(self) -> datetime:
        """
        Получить дату/время последнего изменения заметки.

        Returns:
            datetime: Дата/время последнего изменения заметки.
        """
        pass


class AbstractNote(Note):
    """
    Абстрактный класс для заметки.

    Этот класс реализует общую функциональность для всех заметок.
    """

    def __init__(self, note_id: int, title: str, body: str):
        """
        Конструктор класса AbstractNote.

        Args:
            note_id (int): Идентификатор заметки.
            title (str): Заголовок заметки.
            body (str): Тело заметки.
        """
        self._id = note_id
        self._title = title
        self._body = body
        self._created_at = datetime.datetime.now()
        self._updated_at = self._created_at

    def get_id(self) -> int:
        """
        Получить идентификатор заметки.

        Returns:
            int: Идентификатор заметки.
        """
        return self._id

    def get_title(self) -> str:
        """
        Получить заголовок заметки.

        Returns:
            str: Заголовок заметки.
        """
        return self._title

    def set_title(self, title: str) -> None:
        """
        Установить заголовок заметки.

        Args:
            title (str): Новый заголовок заметки.
        """
        self._title = title

    def get_body(self) -> str:
        """
        Получить тело заметки.

        Returns:
            str: Тело заметки.
        """
        return self._body

    def set_body(self, body: str) -> None:
        """
        Установить тело заметки.

        Args:
            body (str): Новое тело заметки.
        """
        self._body = body

    def get_created_at(self) -> datetime.datetime:
        return self._created_at

    def get_updated_at(self) -> datetime.datetime:
        return self._updated_at

    def get_created_at_fr(self) -> str:
        return self._created_at.strftime("%d.%m.%Y %H:%M:%S")

    def get_updated_at_fr(self) -> str:
        return self._updated_at.strftime("%d.%m.%Y %H:%M:%S")

