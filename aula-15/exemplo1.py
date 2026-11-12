import polars as pl
from datetime import datetime
import numpy as np

ENDERECO_DADOS = "./../DADOS/auxiliobrasil.parquet"

pl.Config.set_float_precision(2)
pl.Config.set_thousands_separator(".")
pl.Config.set_tbl_rows(-1)


try:
    print("Obtendo os dados...")
    inicio = datetime.now()

    df_lazy_plan = (
        pl.scan_parquet(ENDERECO_DADOS)
        .select(["NOME MUNICÍPIO", "VALOR PARCELA"])
        .with_columns(
            pl.col("NOME MUNICÍPIO").cast(pl.Categorical)
        )
        .filter(pl.col("VALOR PARCELA") > 2000)
        .group_by('NOME MUNICÍPIO')
        .agg(pl.col("VALOR PARCELA").sum())
        .sort("VALOR PARCELA", descending=True)
    )
    
    df_auxilio = df_lazy_plan.collect()

    print(df_auxilio.head())
    fim = datetime.now()
    print(f"Tempo Decorrido: {fim - inicio}")

except Exception as e:
    print(f"Erro ao obter dados {e}")

#obtendo medidas estasticas do dataframe
try:
    array = np.array(df_auxilio["VALOR PARCELA"])
    media = np.mean(array)
    mediana = np.median(array)
    #distancia percentual entre a mediana e a média
    distancia_percentual = abs((media - mediana) / mediana) * 100





except Exception as e:
    print(f"Erro ao obter medidas estatísticas {e}")