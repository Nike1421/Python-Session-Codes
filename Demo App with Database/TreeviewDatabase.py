import sqlite3

class Database:
    def __init__(self, db) -> None:
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS student
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                age INTEGER,
                email TEXT
            )
            """
        )
        self.conn.commit()
    
    def queryAll(self):
        self.cur.execute(
            """
            SELECT * FROM student    
            """
        )
        result = self.cur.fetchall()
        return result
    

    def insertEntry(self, row):
        self.cur.execute(
            """
            INSERT INTO student VALUES
            (NULL, :first_name, :last_name, :age, :email)
            """,
            {
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'email': row['email'],
            }
        )
        self.conn.commit()

    def updateEntry(self, row):
        self.cur.execute(
            """
            UPDATE student
            SET 
            first_name = :first_name,
            last_name = :last_name,
            age = :age,
            email = :email
            WHERE id = :id
            """,
            {
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'email': row['email'],
                'id' : row['id']
            }
        )
        self.conn.commit()

    def deleteEntry(self, row):
        self.cur.execute(
            """
            DELETE FROM student 
            WHERE id = :id
            """,
            {
                'id': row['id']
            }
        )
        # self.conn.commit()

    def __del__(self):
        self.conn.close()
