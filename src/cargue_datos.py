"""
cargue_datos.py

Carga los dos conjuntos de datos de las Olimpiadas (athlete_events.csv y
noc_regions.csv), los une por NOC y crea las variables IMC y medalla.
Los archivos originales deben estar en la carpeta data/ (ver data/README.md).
"""

from pathlib import Path

import pandas as pd

CARPETA_DATA = Path(__file__).resolve().parent.parent / "data"


def cargar_datos(carpeta=CARPETA_DATA):
    """Devuelve (df_atletas, df_regiones) leídos desde la carpeta indicada."""
    df_atletas = pd.read_csv(Path(carpeta) / "athlete_events.csv")
    df_regiones = pd.read_csv(Path(carpeta) / "noc_regions.csv")
    return df_atletas, df_regiones


def preparar_datos(df_atletas, df_regiones):
    """Crea IMC, une con las regiones (left) y crea la variable binaria medalla."""
    df = df_atletas.copy()
    df["IMC"] = df["Weight"] / ((df["Height"] / 100) ** 2)
    df = pd.merge(df, df_regiones, on="NOC", how="left")
    df["medalla"] = df["Medal"].notna().astype(int)
    return df


if __name__ == "__main__":
    atletas, regiones = cargar_datos()
    datos = preparar_datos(atletas, regiones)
    print("Filas:", len(datos), "| Columnas:", datos.shape[1])