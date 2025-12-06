# Game of Life con C++ + pybind11 + Python

Pequeño proyecto para demostrar cómo usar **pybind11** para exponer código C++ a Python.

La idea es sencilla:

- El **núcleo** del Juego de la Vida de Conway está implementado en C++ (clase `World`).
- Usamos **pybind11** para compilarlo como módulo de Python (`cppdemo`).
- Desde Python controlamos el mundo, lo visualizamos con `matplotlib` y comparamos rendimiento con una versión en Python puro.

Este proyecto está pensado como demo didáctica para gente que no conoce pybind11.

---

## Requisitos

- Python 3.11 (o similar)
- CMake 3.15+
- Compilador C++ (Visual Studio 2022 en Windows, g++/clang en Linux/macOS)
- Dependencias Python:

  ```bash
  pip install numpy matplotlib
  ```

---

## Estructura básica
```bash
src/
  world.hpp        # Clase World con la logica del Game of Life
  world.cpp
  bindings.cpp     # Envoltura pybind11 (PYBIND11_MODULE)

CMakeLists.txt     # Proyecto CMake

examples/          # ficheros de ejemplo para probar el programa
build/             # (se genera) ficheros intermedios y el modulo cppdemo*.pyd
```

---


## Compilación (ejemplo en Windows + Visual Studio)

Desde la raíz del proyecto:

```
mkdir build
cd build

cmake -DPYTHON_EXECUTABLE="C:\Ruta\A\tu\python.exe" ..
cmake --build . --config Release
```

El módulo cppdemo se generará en algo como:

```
build/Release/cppdemo.cp3XX-win_amd64.pyd
```

---

## Probar los módulos

Entra en la carpeta /examples. Desde la raiz:

```
cd examples
```

### Demo de patrones

Desde la carpeta /examples:
```
python demo_patterns.py
```

### Demo de animacion con matplotlib

Desde la carpeta /examples:

```
python demo_matplolib.py
```

### Benchmark: Python vs C++

Desde la carpeta /examples:
```
python benchmark.py
```

### Demo de numpy

Desde la carpeta /examples:

```
python test_numpy.py
```

### Test de como funciona un estado a nivel interno

Desde la carpeta /examples:

```
python test_world.py
```

---

## Definir un patrón

Se puede hacer de dos maneras:
- Definiendo células vivas
- Pasando el World como string
  
### Definiendo las celulas vivas del patrón
Esto se hace con una lista de coordenadas. Aqui se muestran varios ejemplos.

Glider:
```
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
```

Two Ring explosion:
```
def pattern_explosion(w, x0, y0):
    """Coloca un patrón de explosión de dos anillos."""
    coords = [
        # Anillo izquierdo
        (x0, y0), (x0+1, y0), (x0+2, y0),
        (x0, y0+1),           (x0+2, y0+1),
        (x0, y0+2), (x0+1, y0+2), (x0+2, y0+2),
        
        # Anillo derecho
        (x0+4, y0), (x0+5, y0), (x0+6, y0),
        (x0+4, y0+1),           (x0+6, y0+1),
        (x0+4, y0+2), (x0+5, y0+2), (x0+6, y0+2),
    ]
    for x, y in coords:
        if 0 <= x < w.width and 0 <= y < w.height:
            w.set_cell(x, y, 1)  
```

Tras definir el patrón llamas al método con las coordenadas iniciales:
```
  w = empty_world()
  pattern_explosion(w, 25, 15)
```

### Definiendo el mundo como string
Definimos el mundo inicial en un string o en un fichero de texto:
```
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
```

Y empleamos el metodo place_world:
```
def place_world(world, x0, y0, PATTERN):
    """Coloca el patrón 119P4H1V0 con su esquina superior izquierda en (x0, y0)."""
    for dy, row in enumerate(PATTERN):
        for dx, c in enumerate(row):
            if c == "O":
                world.set_cell(x0 + dx, y0 + dy, 1)
```
