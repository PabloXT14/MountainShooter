import sqlite3


class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(
            self.db_name
        )  # open if db file exists, otherwise create a new one automatically

        # create a cursor (cursor allows us to execute SQL commands)
        self.cursor = self.connection.cursor()

        # CREATE TABLE
        self.cursor.execute(
            """
              CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                score INTEGER NOT NULL,
                date TEXT NOT NULL
              )
            """
        )

        self.connection.commit()  # save changes

    def save(self, score_dict: dict):
        self.cursor.execute(
            "INSERT INTO players (name, score, date) VALUES (:name, :score, :date)",
            score_dict,
        )

        self.connection.commit()

    def get_top_10_players(self) -> list:
        top_10_players = self.cursor.execute(
            "SELECT * FROM players ORDER BY score DESC LIMIT 10"
        ).fetchall()

        return top_10_players

    def close_connection(self):
        self.connection.close()
