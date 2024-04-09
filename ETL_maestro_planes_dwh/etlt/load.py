import oracledb
import pandas as pd
import time



class Loader:
    def __init__(self, conn):
        self.conn = conn
        self.cur = self.conn.cursor()

    def drop_table(self, name):
        """
        Elimina una tabla de la base de datos.

        """
        try:
            self.cur.execute(f"DROP TABLE {name}")
        except oracledb.DatabaseError as e:
            print(f"Alerta ->Error al eliminar la tabla {name} ->El proceso continuara")

    def load(self, dataframe, table_name, tipo='create'):
        """
        Carga un DataFrame de Pandas en una tabla de la base de datos.

        """
        dataframe= dataframe.astype(str)
        
        if tipo not in ('no_create', 'create'):
            print("Operación inválida")
            return
        columns = [f'{i} VARCHAR(250)' for i in dataframe.columns]
        columns_str = ','.join(columns)
        placeholders = ','.join([f':{i+1}' for i in range(len(dataframe.columns))])

        if tipo == 'create':
            self.drop_table(table_name)
            create_table_query = f"CREATE TABLE {table_name} ({columns_str})"
            self.cur.execute(create_table_query)
        
        time.sleep(45)

        insert_data_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        data = [tuple(row) for row in dataframe.values]
     
        self.cur.executemany(insert_data_query, data)
        self.conn.commit()