import valohai
import pandas as pd
import os

# Preparamos para que valohai entienda el paso
valohai.prepare(step="hello-job")

# Buscamos el dataset de input
input_paths = valohai.inputs('dataset').paths()

if input_paths:
    dataset_path = input_paths[0]
    print(f"Usando dataset en: {dataset_path}")

    # Leer el CSV
    df = pd.read_csv(dataset_path)
    print("Contenido del dataset:")
    print(df)
else:
    print("No se ha proporcionado un dataset.")

print("Hello world desde Valohai!")
