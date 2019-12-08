import mysql.connector
import os 

class MySQL():

    def __init__(self):
        self.conn = mysql.connector.connect(
            host='mysql',
            port=3306,
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASSWORD'],
            database=os.environ['MYSQL_DATABASE'])
        
    def __del__(self):
        self.conn.close()

    def insert(self, word):
        self.conn.ping(reconnect=True)
        cur = self.conn.cursor()

        try:
            cur.execute('INSERT INTO KEYWORD (word) VALUES (%s)', [(word)])
            self.conn.commit()
            success = True
        except:
            self.conn.rollback()
            success = False
            raise

        result = {
            "word": word,
            "success" : success
        }

        return result


    def select_all(self):

        self.conn.ping(reconnect=True)
        cur = self.conn.cursor()
        cur.execute('SELECT * FROM KEYWORD')
        sql_result = cur.fetchall()

        result = []

        for item in sql_result :
            result.append(item[0])

        return result

    def check_existance(self, word):
        """単語の存在確認
        
        Arguments:
            word {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """

        self.conn.ping(reconnect=True)
        cur = self.conn.cursor()
        cur.execute('SELECT * FROM KEYWORD WHERE word = %s', [(word)])
        sql_result = cur.fetchall()

        return len(sql_result) > 0 


    def delete(self, word):

        self.conn.ping(reconnect=True)
        cur = self.conn.cursor()
        try:
            sql = 'DELETE FROM KEYWORD WHERE word = %s'
            cur.execute(sql, (word,))
            self.conn.commit()
            success = True
        except:
            self.conn.rollback()
            raise
            success = False

        result = {
            "word": word,
            "success" : success
        }

        return result
