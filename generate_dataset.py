import os
import json
import valohai
from PIL import Image
import numpy as np

# Directorio de imágenes (output con nombre mi_ejemplo_output_carpeta)
output_dir = valohai.outputs().path('mi_ejemplo_output_carpeta')
os.makedirs(output_dir, exist_ok=True)

# Crear imagen nueva
file_name = "imagen2_colores_random.png"
path = os.path.join(output_dir, file_name)
img = Image.fromarray(np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8))
img.save(path)

# Ruta relativa del archivo dentro de outputs
relative_path = f"mi_ejemplo_output_carpeta/{file_name}"

# Crear metadata con herencia desde v1
metadata = {
    relative_path: {
        "valohai.dataset-versions": [{
            'uri': "dataset://agranado-dataset/v3",
            'from': "dataset://agranado-dataset/v1",
            'start_fresh': False
        }]
    }
}

# Guardar metadata
metadata_path = valohai.outputs().path("valohai.metadata.jsonl")
with open(metadata_path, "w") as f:
    json.dump({"file": relative_path, "metadata": metadata[relative_path]}, f)
    f.write("\n")
