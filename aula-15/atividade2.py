import polars as pl

ENDERECO_DADOS = "./../DADOS/auxiliobrasil.parquet"

try:
    print("Obtendo os dados...")

    df_auxilio = pl.scan_parquet(ENDERECO_DADOS)

    df_auxilio = df_auxilio.collect()

    print(df_auxilio.head())

except Exception as e:
    print(f"Erro ao obter dados {e}") 