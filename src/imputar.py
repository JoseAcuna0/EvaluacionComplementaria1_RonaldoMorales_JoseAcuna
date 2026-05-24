import os
import pandas as pd


def imputar_datos(input_path: str, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.read_csv(input_path)

    df["nota1"] = df["nota1"].fillna(df["nota1"].median())
    df["nota2"] = df["nota2"].fillna(df["nota2"].median())
    df["nota3"] = df["nota3"].fillna(df["nota3"].median())

    media_asistencia = round(df["asistencia"].mean())
    df["asistencia"] = df["asistencia"].fillna(media_asistencia).astype(int)

    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    imputar_datos("data/interim/validado.csv", "data/interim/imputado.csv")