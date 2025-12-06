#pragma once


#include <vector>
#include <cstdint>


class World {
public:
    World(int width, int height);

    int width() const { return width_; }
    int height() const { return height_; }

    // Pone todas las celdas a 0 (muertas)
    void clear();

    // Rellena aleatoriamente con probabilidad alive_prob de estar viva
    void randomize(double alive_prob);

    // Avanza una generacion aplicando las reglas del Game of Life
    void step();

    // Devuelve 0 o 1 para la celda (x, y)
    int get_cell(int x, int y) const;


    // Establece la celda (x, y) a 0 o 1
    void set_cell(int x, int y, int value);

private:
    int width_;
    int height_;
    std::vector<std::uint8_t> cells_;  // 0: muerta, 1: viva

    // indice lineal en el vector a partir de (x, y)
    int index(int x, int y) const {
        return y * width_ + x;
    }

    // Cuenta vecinos vivos alrededor de (x, y)
    int count_alive_neighbors(int x, int y) const;
};

