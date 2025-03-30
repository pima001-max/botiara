import sqlite3


class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """
        Создаём подключение к базе данных.
        """
        try:
            self.connection = sqlite3.connect(self.db_path)
            print(f"Подключение к базе {self.db_path} успешно.")
        except sqlite3.Error as e:
            print(f"Ошибка подключения к базе данных: {e}")
            raise

    def execute_query(self, query, params=None):
        """
        Выполняем SQL-запрос.
        """
        if not self.connection:
            self.connect()
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Ошибка при выполнении запроса: {e}")
            raise

    def fetchall(self, query, params=None):
        """
        Получаем все данные из запроса.
        """
        if not self.connection:
            self.connect()
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Ошибка выполнения SELECT-запроса: {e}")
            raise

    def close(self):
        """
        Закрываем соединение с базой данных.
        """
        if self.connection:
            self.connection.close()
            print("Соединение с базой данных закрыто.")
