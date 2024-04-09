import os

HOST_ORIGEN = os.environ['vsys_host_bi']
PORT_ORIGEN = '1521'
SERVICE_NAME_ORIGEN = os.environ['vsys_servname_bi']
USERNAME_ORIGEN = 'OPE_WRK'
PASSWORD_ORIGEN = os.environ['vsys_dbu_password_bi']


HOST_DESTINO = os.environ['vsys_host_sdw']
PORT_DESTINO = '1521'
SERVICE_NAME_DESTINO = os.environ['vsys_servname_sdw']
USERNAME_DESTINO = 'DBU_EGONZALESP'
PASSWORD_DESTINO = os.environ['vsys_dbu_password_sdw']

FILE_PATH = 'C:/Users/EDUARDO/Desktop/04_GIT/RepoPtyhon_steps/ETLT/df_extract.csv'
SQL_ORI = 'select * from bta_dw.ref_trff_plan'
TABLE_DEST = 'cvm_inf.tb_dwh_trff_plan'
SQL_step1 = f'truncate table {TABLE_DEST}'
SQL_step2 = f"SELECT 5 FROM DUAL" ##se usa doble corchete para poder usar el where con ''
TIPO_CARGA = 'no_create' ##create -> no_create

