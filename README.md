### Clase: `Extractor`
- **Descripción:** Extrae datos desde una fuente.
- **Métodos:**
  - `extract(self, sql)`: Ejecuta un query SQL y devuelve los resultados como un DataFrame de pandas.
  - `dumpCsv(self, dataframe, nombre)`: Exporta un DataFrame a un archivo CSV.

### Clase: `Loader`
- **Descripción:** Responsable de cargar datos en la base de datos.
- **Métodos:**
  - `dropTable(self, name)`: Borra una tabla en la base de datos.
  - `load(self, dataframe, table_name, tipo='create')`: Carga un DataFrame en una tabla especificada, con la opción de crear la tabla.

### Clase: `Transformer`
- **Descripción:** Aplica transformaciones a los datos en memoria local.
- **Métodos:**
  - `readCsv(self, nombre)`: Lee un archivo CSV y lo convierte en un DataFrame.
  - `transform(self, dataframe)`: Agrega una nueva columna de fecha y hora actual a un DataFrame.

### Clase: `LargeTransformer`
- **Descripción:** Realiza transformaciones de datos en la BD, con los recursos de la BD.
- **Métodos:**
  - `localTransform(self, sql)`: Ejecuta un comando SQL para transformar datos en la BD.

### Config.py:
- **archivo de configuracion:** hay que crearlo y moverlo a la carpeta principal

## main.py

El script `main.py` integra las operaciones del ETLT usando las clases, siguiendo estos pasos:
1. Conexión a las bases de datos de origen y destino.
2. Configuración e instancia de las clases `Extractor`, `Transformer`, `Loader`, y `LargeTransformer`.
<<<<<<< Updated upstream
3. Extracción, transformación (básica y avanzada), y carga de datos D: D:
=======
3. Extracción, transformación (básica y avanzada), y carga de datos :D :D
>>>>>>> Stashed changes
