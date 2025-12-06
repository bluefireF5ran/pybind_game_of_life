# demo_patterns.py
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
import matplotlib.pyplot as plt

WIDTH = 50
HEIGHT = 30
STEPS = 200

def empty_world():
    w = cppdemo.World(WIDTH, HEIGHT)
    w.clear()
    return w

def pattern_glider(w, x0, y0):
    """Coloca un 'glider' empezando en (x0, y0)."""
    coords = [
        (x0+1, y0),
        (x0+2, y0+1),
        (x0,   y0+2),
        (x0+1, y0+2),
        (x0+2, y0+2),
    ]
    for x, y in coords:
        if 0 <= x < w.width and 0 <= y < w.height:
            w.set_cell(x, y, 1)

def pattern_blinker(w, x0, y0):
    """Oscilador básico de periodo 2."""
    coords = [
        (x0,   y0),
        (x0+1, y0),
        (x0+2, y0),
    ]
    for x, y in coords:
        if 0 <= x < w.width and 0 <= y < w.height:
            w.set_cell(x, y, 1)

def pattern_block(w, x0, y0):
    """Bloque estático 2x2."""
    coords = [
        (x0,   y0),
        (x0+1, y0),
        (x0,   y0+1),
        (x0+1, y0+1),
    ]
    for x, y in coords:
        if 0 <= x < w.width and 0 <= y < w.height:
            w.set_cell(x, y, 1)

def main():
    w = empty_world()

    # Colocamos unos cuantos patrones
    pattern_glider(w, 2, 2)
    pattern_glider(w, 10, 5)
    pattern_blinker(w, 25, 10)
    pattern_block(w, 35, 5)

    plt.ion()
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title("Game of Life - patrones (C++ via pybind11)")

    img = ax.imshow(w.get_state(), interpolation="nearest")
    ax.set_axis_off()

    for step in range(STEPS):
        w.step()
        img.set_data(w.get_state())
        ax.set_title(f"Step {step}")
        plt.pause(0.03)

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    main()
