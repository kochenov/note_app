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