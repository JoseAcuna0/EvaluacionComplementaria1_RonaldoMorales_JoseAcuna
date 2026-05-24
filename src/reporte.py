from datetime import datetime
import os
import pandas as pd


def generar_reporte(
    csv_path: str, resumen_path: str, output_md: str
) -> None:
    os.makedirs(os.path.dirname(output_md), exist_ok=True)

    df = pd.read_csv(csv_path)
    with open(resumen_path, "r", encoding="utf-8") as f:
        resumen_contenido = f.read()

    df_val = pd.read_csv("data/interim/validado.csv")
    total_imputados = int(df_val["tiene_faltantes"].sum())
    lista_imputados = df_val[df_val["tiene_faltantes"]]["nombre"].tolist()

    with open(output_md, "w", encoding="utf-8") as f:
        f.write("# Reporte Final de Rendimiento Academico\n\n")
        f.write(
            f"**Fecha de generacion:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )

        f.write("## 1. Resumen Estadistico del Curso\n")
        f.write("```text\n")
        f.write(resumen_contenido)
        f.write("```\n\n")

        f.write("## 2. Detalle de Alumnos y Calificaciones\n")
        f.write(
            "| nombre | nota1 | nota2 | nota3 | asistencia | promedio | categoria |\n"
        )
        f.write(
            "| :--- | :---: | :---: | :---: | :---: | :---: | :--- |\n"
        )

        for idx, row in df.iterrows():
            f.write(
                f"| {row['nombre']} | {row['nota1']} | {row['nota2']} | {row['nota3']} | {row['asistencia']} | {row['promedio']} | {row['categoria']} |\n"
            )
        f.write("\n")

        f.write("## 3. Observations sobre Datos Imputados\n")
        f.write(
            f"Se detectaron y corrigieron un total de **{total_imputados}** registros con valores faltantes.\n\n"
        )
        f.write("Estudiantes afectados por el proceso de imputacion:\n")
        for est in lista_imputados:
            f.write(f"- {est}\n")


if __name__ == "__main__":
    generar_reporte(
        "data/processed/transformado.csv",
        "data/processed/resumen.txt",
        "reports/reporte_final.md",
    )