# test_world.py

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
build_dir = ROOT / "build" 

release_dir = build_dir / "Release"  # En Windows, las compilaciones suelen ir en una carpeta "Release"

if release_dir.exists():
    build_dir = release_dir

sys.path.insert(0, str(build_dir))

import cppdemo

w = cppdemo.World(10, 5)
print("width =", w.width, "height =", w.height)

w.randomize(0.3)

print("Estado inicial:")
for y in range(w.height):
    fila = "".join("#" if w.get_cell(x, y) else "." for x in range(w.width))
    print(fila)

w.step()

print("\nDespues de una generacion:")
for y in range(w.height):
    fila = "".join("#" if w.get_cell(x, y) else "." for x in range(w.width))
    print(fila)
