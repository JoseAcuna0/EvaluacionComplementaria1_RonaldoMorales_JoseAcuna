import os

import pandas as pd


def transformar_datos(input_path: str, output_path: str) -> None:
    """
    Transforma los datos del dataset imputado.csv calculando el promedio de las notas, asignando la categoria de cada alumno y guardando el resultado en transformado.csv.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.read_csv(input_path)

    df["promedio"] = df[["nota1", "nota2", "nota3"]].mean(axis=1).round(2)

    df["aprobado"] = df["promedio"] >= 4.0

    def asignar_categoria(promedio: float) -> str:
        if promedio >= 6.0:
            return "Destacado"
        elif promedio >= 4.0:
            return "Aprobado"
        else:
            return "Reprobado"

    df["categoria"] = df["promedio"].apply(asignar_categoria)

    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    transformar_datos("data/interim/imputado.csv", "data/processed/transformado.csv")
