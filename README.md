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


