import os
import valohai
import pandas as pd

# Preparar Valohai
print("Preparando Valohai...")
valohai.prepare(
    step="train-in-out",
    default_parameters={"exponente": 2}
)

# Obtener parámetro
exponente = valohai.parameters('exponente').value
print(f"Exponente configurado: {exponente}")

# Obtener path del dataset
print("Obteniendo path del dataset...")
input_paths = list(valohai.inputs('dataset').paths())

if not input_paths:
    raise ValueError("No se ha proporcionado dataset.")

dataset_path = input_paths[0]
print(f"Dataset encontrado en: {dataset_path}")

# Leer CSV
print(f"Leyendo dataset en: {dataset_path}")
df = pd.read_csv(dataset_path)
print(f"Datos leídos. Primeras filas del dataset:\n{df.head()}")

# Procesar: elevar cada valor a la potencia indicada
print("Procesando datos...")
processed_df = df.applymap(lambda x: x**exponente if isinstance(x, (int, float)) else x)
print("Datos procesados.")

# Obtener output path y especificar nombre del archivo
print("Obteniendo path para guardar el archivo procesado...")
output_file = valohai.outputs('result').path('processed_positions.csv')  # Especificar el archivo

# Crear directorio de salida si no existe
print(f"Guardando archivo procesado en: {output_file}...")
processed_df.to_csv(output_file, index=False)
print(f"Archivo procesado guardado en: {output_file}")
