import mysql.connector
from mysql.connector import errorcode


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

    def makeRequest(self, query):
        try:
            conn = mysql.connector.connect(**self.config)
            cur = conn.cursor()
            cur.execute(query)
            for answer in cur:
                print(answer)
            conn.commit()

        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
        finally:

            conn.close()
