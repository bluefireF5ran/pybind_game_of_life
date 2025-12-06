# benchmark.py
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
build_dir = ROOT / "build" / "Release"  # o "build" / "Debug" si compilas en debug
sys.path.append(str(build_dir))

import time
import numpy as np
import cppdemo

WIDTH = 200
HEIGHT = 200
STEPS = 50

# --- Implementacion Python pura -------------------------
def step_python(state: np.ndarray) -> np.ndarray:
    """Aplica una generacion del Game of Life en Python puro."""
    h, w = state.shape
    new_state = np.zeros_like(state)

    for y in range(h):
        for x in range(w):
            alive_neighbors = 0
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < w and 0 <= ny < h:
                        alive_neighbors += state[ny, nx]

            if state[y, x] == 1:
                if 2 <= alive_neighbors <= 3:
                    new_state[y, x] = 1
                else:
                    new_state[y, x] = 0
            else:
                if alive_neighbors == 3:
                    new_state[y, x] = 1
                else:
                    new_state[y, x] = 0

    return new_state

# --- Benchmark Python puro ------------------------------
np.random.seed(0)
state_py = (np.random.rand(HEIGHT, WIDTH) < 0.3).astype(np.uint8)

t0 = time.perf_counter()
for _ in range(STEPS):
    state_py = step_python(state_py)
t1 = time.perf_counter()

time_python = t1 - t0
print(f"Python puro: {time_python:.3f} s para {STEPS} pasos")

# --- Benchmark C++ via pybind11 -------------------------
w = cppdemo.World(WIDTH, HEIGHT)
# Reutilizamos el mismo estado inicial que usamos en Python
w.set_state((np.random.rand(HEIGHT, WIDTH) < 0.3).astype(np.uint8))

t0 = time.perf_counter()
for _ in range(STEPS):
    w.step()
    # opcional: state = w.get_state()  # si quisieras leerlo
t1 = time.perf_counter()

time_cpp = t1 - t0
print(f"C++ (World): {time_cpp:.3f} s para {STEPS} pasos")

# --- Comparacion ----------------------------------------
if time_cpp > 0:
    speedup = time_python / time_cpp
    print(f"Speedup (Python / C++): x{speedup:.1f}")
