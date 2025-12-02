#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
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
	         py::arg("x"), py::arg("y"), py::arg("value"))
	    // ?? NUEVO: devolver estado como numpy.ndarray
	    .def("get_state", [](const World &self) {
	        // Creamos un array 2D (height, width)
	        py::array_t<std::uint8_t> arr({self.height(), self.width()});
	        auto buf = arr.mutable_unchecked<2>();
	
	        for (int y = 0; y < self.height(); ++y) {
	            for (int x = 0; x < self.width(); ++x) {
	                buf(y, x) = static_cast<std::uint8_t>(self.get_cell(x, y));
	            }
	        }
	
	        return arr;
	    })
	.def("set_state",
        [](World &self,
    		py::array_t<std::uint8_t,
            	py::array::c_style | py::array::forcecast> state) {
            if (state.ndim() != 2) {
            	throw std::runtime_error("state must be a 2D array");
            }
            if (state.shape(0) != self.height()
            	|| state.shape(1) != self.width()) {
                throw std::runtime_error("state shape does not match world size");
            }

            auto buf = state.unchecked<2>();

            for (int y = 0; y < self.height(); ++y) {
            	for (int x = 0; x < self.width(); ++x) {
                    // Cualquier valor != 0 lo consideramos "vivo"
                    int value = buf(y, x) ? 1 : 0;
                    self.set_cell(x, y, value);
                }
            }
        },
        py::arg("state"));
}

