import oracledb

class LargeTransformer:
    def __init__(self, conn):
        self.conn = conn
        self.cur = self.conn.cursor()

    def local_transform(self, sql, switch=False):
        """
        Realiza transformaciones de datos directamente en la base de datos.

        """
        if switch == False:
            self.cur.execute(sql)
            self.conn.commit()
        elif switch == True:
            pass
        else:
            return Exception