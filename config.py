import os

HOST_ORIGEN = os.environ['vsys_host_bi']
PORT_ORIGEN = '1521'
SERVICE_NAME_ORIGEN = os.environ['vsys_servname_bi']
USERNAME_ORIGEN = 'OPE_WRK'
PASSWORD_ORIGEN = os.environ['vsys_dbu_password_bi']


HOST_DESTINO = os.environ['vsys_host_sdw']
PORT_DESTINO = '1521'
SERVICE_NAME_DESTINO = os.environ['vsys_servname_sdw']
USERNAME_DESTINO = 'CVM_INF'
PASSWORD_DESTINO = os.environ['vsys_dbu_password_sdw']

FILE_PATH = 'D:/13_GIT_REPO/DUMP_CSV/df_extract.csv'
SQL_ORI = 'select * from bta_dw.ref_trff_plan'
TABLE_DEST = 'cvm_inf.tb_dwh_trff_plan'
SQL_step1 = f'truncate table {TABLE_DEST}'
SQL_step2 = f"SELECT 1 FROM DUAL" ##se usa doble corchete para poder usar el where con ''
TIPO_CARGA = 'no_create' ##create -> no_create

