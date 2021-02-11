from source.manage_database.connect_db import connect_db


class ManageDatabase:

    def __init__(self):

        self.con = connect_db()
        self.cursor = self.con.cursor()

    def read_data(self):

        self.cursor.execute("SELECT image FROM images")
        query_result = self.cursor.fetchall()

        return query_result
