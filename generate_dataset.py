import os
import json
import valohai
from PIL import Image
import numpy as np

# Directorio de imágenes (output con nombre mi_ejemplo_output_carpeta)
output_dir = valohai.outputs().path('mi_ejemplo_output_carpeta')
os.makedirs(output_dir, exist_ok=True)

output_files = []
for i in range(1):
    img = Image.fromarray(np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8))
    file_name = f"imagen2_colores_random.png"
    path = os.path.join(output_dir, file_name)
    img.save(path)
    output_files.append(f"mi_ejemplo_output_carpeta/{file_name}")

# Crear metadata del dataset
"""metadata = {
    file_name: {
        "valohai.dataset-versions": ["dataset://agranado-dataset/v2"]
    }
    for file_name in output_files
}"""



# SI QUEREMOS QUE LA SIGUIENTE VERSION TENGA LO DE LA ANTERIOR + LO NUEVO:
# Ruta relativa del archivo dentro de outputs
relative_path = f"mi_ejemplo_output_carpeta/{file_name}"

# Crear metadata con herencia desde v1
metadata = {
    relative_path: {
        "valohai.dataset-versions": [{
            'uri': "dataset://agranado-dataset/v4",
            'from': "dataset://agranado-dataset/v1",
            'start_fresh': False
        }]
    }
}


metadata_path = valohai.outputs().path("valohai.metadata.jsonl")
with open(metadata_path, "w") as f:
    for file_name, meta in metadata.items():
        json.dump({"file": file_name, "metadata": meta}, f)
        f.write("\n")
