import pandas as pd
import os

class Transformer:
    def __init__(self):
        pass

    def read_csv(self,nombre):
        """
        Lee un archivo CSV y lo convierte en un DataFrame de Pandas.

        """

        return pd.read_csv(nombre, index_col=False, dtype=str, delimiter='|', low_memory=True)

    def transform(self, dataframe):
        """
        Realiza transformaciones en un DataFrame de Pandas.

        """
        dataframe['log_date'] = pd.Timestamp.today().strftime('%Y-%m-%d %H:%M:%S')
        return dataframe