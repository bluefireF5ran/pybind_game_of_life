# \# Game of Life con C++ + pybind11 + Python

# 

# Pequeño proyecto para demostrar cómo usar \*\*pybind11\*\* para exponer código C++ a Python.

# 

# La idea es sencilla:

# 

# \- El \*\*núcleo\*\* del Juego de la Vida de Conway está implementado en C++ (clase `World`).

# \- Usamos \*\*pybind11\*\* para compilarlo como módulo de Python (`cppdemo`).

# \- Desde Python controlamos el mundo, lo visualizamos con `matplotlib` y comparamos rendimiento con una versión en Python puro.

# 

# Este proyecto está pensado como demo didáctica para gente que no conoce pybind11.

# 

# ---

# 

# \## Requisitos

# 

# \- Python 3.11 (o similar)

# \- CMake 3.15+

# \- Compilador C++ (Visual Studio 2022 en Windows, g++/clang en Linux/macOS)

# \- Dependencias Python:

# &nbsp; ```bash

# &nbsp; pip install numpy matplotlib

# 

