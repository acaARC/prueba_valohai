import os
import shutil
import json
import valohai

# Ruta origen donde están montados los datos reales (ajusta si es necesario)
source_dir = '/data/360mip'

print("Archivos en el origen:")
for root, _, files in os.walk(source_dir):
    for f in files:
        print(os.path.join(root, f))

# Ruta destino en outputs de Valohai
output_dir = valohai.outputs().path('mi_dataset_descomprimido')
os.makedirs(output_dir, exist_ok=True)

output_files = []

# Copiar todos los archivos desde el origen al output
for root, _, files in os.walk(source_dir):
    for f in files:
        src_path = os.path.join(root, f)
        rel_path = os.path.relpath(src_path, start=source_dir)
        dest_path = os.path.join(output_dir, rel_path)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.copy2(src_path, dest_path)
        # Valohai usa rutas relativas desde el root del output
        output_files.append(f"mi_dataset_descomprimido/{rel_path.replace(os.sep, '/')}")


# Crear metadatos para asociar archivos al dataset
metadata = {
    file_name: {
        "valohai.dataset-versions": ["dataset://360mip-real/v1"]
    }
    for file_name in output_files
}

# Guardar metadatos en el archivo requerido por Valohai
metadata_path = valohai.outputs().path("valohai.metadata.jsonl")
with open(metadata_path, "w") as f:
    for file_name, meta in metadata.items():
        json.dump({"file": file_name, "metadata": meta}, f)
        f.write("\n")

print(f"✅ {len(output_files)} archivos copiados y registrados en el dataset '360mip-real/v1'")
