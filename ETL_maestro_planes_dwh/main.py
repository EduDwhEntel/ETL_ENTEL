from etlt.extract import Extractor
from etlt.transform import Transformer
from etlt.load import Loader
from etlt.transform_large import LargeTransformer

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config
import oracledb

##pruebas git4

def main(debug_mode=False):
    with oracledb.connect(user=config.USERNAME_ORIGEN, password=config.PASSWORD_ORIGEN,
                          host=config.HOST_ORIGEN, port=config.PORT_ORIGEN,
                          service_name=config.SERVICE_NAME_ORIGEN) as conn_extract, \
         oracledb.connect(user=config.USERNAME_DESTINO, password=config.PASSWORD_DESTINO,
                          host=config.HOST_DESTINO, port=config.PORT_DESTINO,
                          service_name=config.SERVICE_NAME_DESTINO) as conn_load:

        print("--configurando clases ---")
        
        extractor = Extractor(conn_extract)
        transformer = Transformer()
        loader = Loader(conn_load)
        large_transformer = LargeTransformer(conn_load)

        print("--extraccion datos ---")
        df = extractor.extract(config.SQL_ORI)

        print("--add log_date ---")
        transformer.transform(df)

        print("--dump csv ---")
        extractor.dump_csv(df,config.FILE_PATH)

        print("--read csv ---")
        df_processed = transformer.read_csv(config.FILE_PATH)

        print("--sql transform ---")
        large_transformer.local_transform(config.SQL_step1, switch=False)

        print("--sql insert ---")
        loader.load(df_processed, table_name=config.TABLE_DEST, tipo=config.TIPO_CARGA)

        print("--sql transform ---")
        large_transformer.local_transform(config.SQL_step2, switch=True)

        print("--proceso terminado--")

if __name__ == '__main__':
    main(True) #para usar el debug mode pasar True/False como argumento en funcion main