#include <pybind11/pybind11.h>
#include "world.hpp"

namespace py = pybind11;

// Ejemplo simple de antes
int add(int a, int b) {
    return a + b;
}

PYBIND11_MODULE(cppdemo, m) {
    m.doc() = "Modulo de ejemplo con pybind11 (add + Game of Life)";

    m.def("add", &add,
          "Suma dos enteros y devuelve el resultado",
          py::arg("a"), py::arg("b"));

    py::class_<World>(m, "World")
        .def(py::init<int, int>(), py::arg("width"), py::arg("height"))
        .def_property_readonly("width", &World::width)
        .def_property_readonly("height", &World::height)
        .def("clear", &World::clear)
        .def("randomize", &World::randomize, py::arg("alive_prob") = 0.5)
        .def("step", &World::step)
        .def("get_cell", &World::get_cell, py::arg("x"), py::arg("y"))
        .def("set_cell", &World::set_cell,
             py::arg("x"), py::arg("y"), py::arg("value"));
}

