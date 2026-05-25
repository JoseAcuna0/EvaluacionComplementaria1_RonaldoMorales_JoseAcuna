import os

import pandas as pd


def validar_datos(input_path: str, output_csv: str, output_txt: str) -> None:
    """
    Valida el dataset de estudiantes.csv detectando valores faltantes y guardando un reporte detallado de la validación.
    """
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    os.makedirs(os.path.dirname(output_txt), exist_ok=True)

    df = pd.read_csv(input_path)

    df["tiene_faltantes"] = df.isnull().any(axis=1)

    df.to_csv(output_csv, index=False)

    with open(output_txt, "w", encoding="utf-8") as f:
        f.write("REPORTE DE VALIDACIÓN DE DATOS\n")
        f.write("==============================\n\n")
        f.write("1. Valores faltantes por columna:\n")
        for col in df.columns:
            if col != "tiene_faltantes":
                nulos = int(df[col].isnull().sum())
                f.write(f"   - {col}: {nulos} valores faltantes\n")

        f.write("\n2. Detalle de filas con valores faltantes:\n")
        filas_con_nulos = df[df["tiene_faltantes"]]
        for idx, row in filas_con_nulos.iterrows():
            f.write(f"   - Fila {idx + 1}: Estudiante {row['nombre']}\n")


if __name__ == "__main__":
    validar_datos(
        "data/raw/estudiantes.csv",
        "data/interim/validado.csv",
        "data/interim/reporte_validacion.txt",
    )
