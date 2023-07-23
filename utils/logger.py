import logging


class AppLogger:
    """
    Класс для настройки логирования приложения.
    """

    def __init__(self, log_file="app.log"):
        """
        Конструктор класса AppLogger.

        Args:
            log_file (str): Имя файла для записи логов.
        """
        self._logger = logging.getLogger("NoteApp")
        self._logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        formatter = logging.Formatter(log_format)
        file_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)

    def get_logger(self):
        """
        Получить объект логгера.

        Returns:
            logging.Logger: Объект логгера.
        """
        return self._logger
