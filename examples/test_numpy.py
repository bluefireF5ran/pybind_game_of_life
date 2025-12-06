# test_numpy.py
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
build_dir = ROOT / "build" 

release_dir = build_dir / "Release"  # En Windows, las compilaciones suelen ir en una carpeta "Release"

if release_dir.exists():
    build_dir = release_dir

sys.path.insert(0, str(build_dir))

import cppdemo
import numpy as np

w = cppdemo.World(10, 5)
w.randomize(0.3)

print("World size:", w.width, "x", w.height)

# Obtener el estado como numpy.ndarray
state = w.get_state()
print("state type:", type(state))
print("state dtype:", state.dtype)
print("state shape:", state.shape)
print("state array:\n", state)

# Crear un nuevo estado en NumPy y enviarlo a C++
new_state = np.zeros((w.height, w.width), dtype=np.uint8)
# Dibujamos una "línea" viva en medio
new_state[w.height // 2, :] = 1

print("\nSending new_state to C++...")
w.set_state(new_state)
state2 = w.get_state()
print("state after set_state:\n", state2)

# Avanzar una generación
w.step()
state3 = w.get_state()
print("\nstate after one step:\n", state3)
