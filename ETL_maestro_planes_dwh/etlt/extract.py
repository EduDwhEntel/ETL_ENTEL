import os
import pandas as pd

class Extractor:
    def __init__(self, conn):
        self.conn = conn
        self.cur = self.conn.cursor()

    def extract(self, sql):
        """
        Extrae datos de una base de datos usando una consulta SQL.

        """
        self.cur.execute(sql)
        column_names = [col[0] for col in self.cur.description]
        data = self.cur.fetchall()
        return pd.DataFrame(data, columns=column_names)

    def dump_csv(self, dataframe, nombre):
        """
        Guarda un DataFrame de Pandas en un archivo CSV.

        """

        dataframe.to_csv(nombre, sep='|', index=False, header=True)