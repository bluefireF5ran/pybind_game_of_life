# examples/spaceship_119P4H1V0.py
import sys
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
build_dir = ROOT / "build" 

release_dir = build_dir / "Release"  # En Windows, las compilaciones suelen ir en una carpeta "Release"

if release_dir.exists():
    build_dir = release_dir

sys.path.insert(0, str(build_dir))

import cppdemo  # type: ignore

WIDTH = 80
HEIGHT = 40
STEPS = 300

SPACESHIP_PATTERN = """
.................................O.
................O...............O.O
......O.O......O.....OO........O...
......O....O....O.OOOOOO....OO.....
......O.OOOOOOOO..........O..O.OOO.
.........O.....O.......OOOO....OOO.
....OO.................OOO.O.......
.O..OO.......OO........OO..........
.O..O..............................
O..................................
.O..O..............................
.O..OO.......OO........OO..........
....OO.................OOO.O.......
.........O.....O.......OOOO....OOO.
......O.OOOOOOOO..........O..O.OOO.
......O....O....O.OOOOOO....OO.....
......O.O......O.....OO........O...
................O...............O.O
.................................O.
""".strip().splitlines()


def place_world(world, x0, y0, PATTERN):
    """Coloca el patrón 119P4H1V0 con su esquina superior izquierda en (x0, y0)."""
    for dy, row in enumerate(PATTERN):
        for dx, c in enumerate(row):
            if c == "O":
                world.set_cell(x0 + dx, y0 + dy, 1)


def main():
    w = cppdemo.World(WIDTH, HEIGHT)
    w.clear()

    pat_h = len(SPACESHIP_PATTERN)
    pat_w = len(SPACESHIP_PATTERN[0])

    # La nave empieza a la derecha y se desplaza hacia la izquierda (c/4)
    x0 = WIDTH - pat_w - 2
    y0 = (HEIGHT - pat_h) // 2
    place_world(w, x0, y0, SPACESHIP_PATTERN)

    plt.ion()
    fig, ax = plt.subplots()
    try:
        fig.canvas.manager.set_window_title("119P4H1V0 spaceship (C++ via pybind11)")
    except Exception:
        pass

    img = ax.imshow(w.get_state(), interpolation="nearest")
    ax.set_axis_off()

    for step in range(STEPS):
        w.step()
        img.set_data(w.get_state())
        ax.set_title(f"119P4H1V0 – step {step}")
        plt.pause(0.03)

    plt.ioff()
    plt.show()


if __name__ == "__main__":
    main()
