cmake_minimum_required(VERSION 3.15)
project(cppdemo_project LANGUAGES CXX)

# Usamos C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Para descargar pybind11 automáticamente
include(FetchContent)

FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG        v2.12.0
)

FetchContent_MakeAvailable(pybind11)

# Creamos el módulo de Python
# El nombre "cppdemo" aquí DEBE coincidir con el de PYBIND11_MODULE(cppdemo, m)
pybind11_add_module(cppdemo
    src/bindings.cpp
    src/world.cpp
)
