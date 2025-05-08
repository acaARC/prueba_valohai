import os
import json
import valohai
from PIL import Image
import numpy as np

# Crear carpeta de outputs
output_dir = valohai.outputs().path('mi_ejemplo_output_carpeta')
os.makedirs(output_dir, exist_ok=True)

# Generar archivos de ejemplo
output_files = []
for i in range(2):
    img_array = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    img = Image.fromarray(img_array)
    filename = f"imagen{i+1}_colores_random.png"
    path = os.path.join(output_dir, filename)
    img.save(path)
    output_files.append(f"mi_ejemplo_output_carpeta/{filename}")

# Crear metadatos del dataset
metadata = {
    file_name: {
        "valohai.dataset-versions": ["dataset://mi-dataset-generado/v1"]
    }
    for file_name in output_files
}

metadata_path = valohai.outputs().path("valohai.metadata.jsonl")
with open(metadata_path, "w") as f:
    for file_name, meta in metadata.items():
        json.dump({"file": file_name, "metadata": meta}, f)
        f.write("\n")
