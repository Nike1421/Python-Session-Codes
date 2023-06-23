# Import SQLite

import sqlite3


class Database:
    # Define Constructor
    def __init__(self, db) -> None:
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS employee
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT
            )
            """
        )
        self.conn.commit()

    # Method for Retrieving data

    def queryAll(self):
        self.cursor.execute(
            """
            SELECT * FROM employee
            """
        )
        result = self.cursor.fetchall()
        self.conn.commit()
        return result

    # Method for Inserting data

    def insertEntry(self, row):
        self.cursor.execute(
            """
            INSERT INTO employee VALUES
            (NULL, :first_name, :last_name)
            """,
            {
                'first_name': row['first_name'],
                'last_name' : row['last_name']
            }
        )

        self.conn.commit()

    # Method for Deleting data 

    # Method for Updating data

    # Define Destructor
    def __del__():
        pass