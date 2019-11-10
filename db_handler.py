import mysql.connector
from mysql.connector import errorcode


def wrappMake(func):
    def handler(*args, **kwargs):
        try:
            return func(args[0], args[1])
        except mysql.connector.Error as err:
            print(err)
            args[0].conn.rollback()
        finally:
            args[0].conn.close()
    return handler


class DataBase:

    def __init__(
        self,
        host='localhost',
        user='root',
        pw='NUnCvHGw7iPBstfY3k24',
        port='3306',
        db='rpgproject'
    ):
        self.config = {
            'host': host,
            'user': user,
            'passwd': pw,
            'port': port,
            'db': db
        }

    def _buildConn(self):
        try:
            self.conn = mysql.connector.connect(**self.config)
            return self.conn.cursor()
        except mysql.connector.Error as err:
            raise mysql.connector.Error(err)

    @wrappMake
    def makeRequest(self, query):
        cur = self._buildConn()
        cur.execute(query)
        return dict(zip(cur.column_names, cur.fetchone()))

    @wrappMake
    def makeInsert(self, query):
        cur = self._buildConn()
        cur.execute(query)
        self.conn.commit()
