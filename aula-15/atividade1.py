import polars as pl
import os

ENDEREÇO_DADOS =  "./../DADOS/"   

try:
    print("Obtendo os dados")

    lista_arquivos = [
        arquivo
        for arquivo in os.listdir(ENDEREÇO_DADOS)
        if arquivo.endswith("AuxilioBrasil.csv")
    ]

    dfs = []

    for arquivo in lista_arquivos:
        print(f"Processando Arquivo {arquivo}")

        df = pl.read_csv(
            os.path.join(ENDEREÇO_DADOS, arquivo),
            separator=";",
            encoding="iso8859-1",
            infer_schema=False,       
        ).with_columns(
            pl.col("VALOR PARCELA")
            .str.replace_all(r"\.", "")   
            .str.replace(",", ".")
            .cast(pl.Float64)
        )

        dfs.append(df)

    df_auxilio = pl.concat(dfs)
    print(df_auxilio.head(10))

    df_auxilio.write_parquet(os.path.join(ENDEREÇO_DADOS, "auxiliobrasil.parquet"))
    print("Arquivo convertido")

except Exception as e:
    print(f"Erro ao obter dados {e}")