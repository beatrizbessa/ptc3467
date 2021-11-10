import pandas as pd
import pyarrow as pa
import  pyarrow.parquet as pq

df = pd.read_csv("MICRODADOS_ENEM_2019_SAOPAULO.csv",encoding="ISO-8859-1",sep=";")


table = pa.Table.from_pandas(df)

pq.write_to_dataset(
    table,
    root_path='MICRODADOS_ENEM_2019_SAOPAULO.parquet',
    #partition_cols=['CO_PROVA_CN','CO_PROVA_CH','CO_PROVA_LC','CO_PROVA_MT']
)