import valohai
import os

# Preparar el entorno
valohai.prepare(step="leer-dataset", default_inputs={"dataset": "dataset://agranado-dataset/v6"})

# Obtener la ruta al input y convertir en lista
dataset_paths = list(valohai.inputs('dataset').paths())

print(f"✅ Dataset cargado: {len(dataset_paths)} archivos encontrados:\n")
for path in dataset_paths:
    print(f"- {os.path.basename(path)}")
