import os

import pandas as pd


def resumir_datos(input_path: str, output_txt: str) -> None:
    """
    Calcula y guarda un resumen estadístico del curso en un archivo de texto.
    """
    os.makedirs(os.path.dirname(output_txt), exist_ok=True)
    df = pd.read_csv(input_path)

    total = len(df)
    promedio_curso = float(df["promedio"].mean().round(2))
    nota_min = float(df[["nota1", "nota2", "nota3"]].min().min())
    nota_max = float(df[["nota1", "nota2", "nota3"]].max().max())
    pct_aprobados = float((df["aprobado"].sum() / total * 100).round(2))

    conteos = df["categoria"].value_counts()
    destacados = int(conteos.get("Destacado", 0))
    aprobados = int(conteos.get("Aprobado", 0))
    reprobados = int(conteos.get("Reprobado", 0))

    promedio_asistencia = float(df["asistencia"].mean().round(2))

    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(f"Total de estudiantes procesados: {total}\n")
        f.write(f"Promedio general del curso: {promedio_curso}\n")
        f.write(f"Nota minima individual: {nota_min}\n")
        f.write(f"Nota maxima individual: {nota_max}\n")
        f.write(f"Porcentaje de estudiantes aprobados: {pct_aprobados}%\n")
        f.write("Conteo por categoria:\n")
        f.write(f"  - Destacado: {destacados}\n")
        f.write(f"  - Aprobado: {aprobados}\n")
        f.write(f"  - Reprobado: {reprobados}\n")
        f.write(f"Promedio de asistencia del curso: {promedio_asistencia}%\n")


if __name__ == "__main__":
    resumir_datos("data/processed/transformado.csv", "data/processed/resumen.txt")
