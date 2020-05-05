import sqlite3


class Access:
    def __init__(self, db_name):
        self.db = db_name
        try:
            self.conn = sqlite3.connect(self.db)
            self.cursor = self.conn.cursor()
            print("Data Base:\t", self.db)
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            print("SQlite version:\t %s" % self.data)
        except sqlite3.Error:
            print("Data Base Error Opening.")

    def close_db(self):
        self.conn.close()
        print("Close Connection")

    def commit_on_db(self):
        self.conn.commit()


class ClientDB(Access):
    def __init__(self, db_name):
        super().__init__(db_name)


if __name__ == '__main__':
    db = ClientDB("SilverPOS.db")
    db.close_db()
else:
    Exception("Execution Error")
