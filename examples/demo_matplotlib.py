# demo_matplotlib.py
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
build_dir = ROOT / "build" / "Release"  # o "build" / "Debug" si compilas en debug
sys.path.append(str(build_dir))

import cppdemo
import numpy as np
import matplotlib.pyplot as plt

# Tamaño del mundo y pasos de simulacion
WIDTH = 100
HEIGHT = 60
STEPS = 500

w = cppdemo.World(WIDTH, HEIGHT)
w.randomize(0.3)

# Configuramos la figura
plt.ion()  # modo interactivo
fig, ax = plt.subplots()
fig.canvas.manager.set_window_title("Game of Life (C++ via pybind11)")

img = ax.imshow(
    w.get_state(),
    interpolation="nearest"
)
ax.set_axis_off()

for step in range(STEPS):
    w.step()
    state = w.get_state()
    img.set_data(state)
    ax.set_title(f"Step {step}")
    plt.pause(0.03)  # tiempo entre frames (segundos)

print("Simulacion terminada. Cierra la ventana para salir.")
plt.ioff()
plt.show()
