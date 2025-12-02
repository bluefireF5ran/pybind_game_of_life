#include "world.hpp"
#include <random>
#include <stdexcept>

World::World(int width, int height)
    : width_(width), height_(height), cells_(width * height, 0) {
    if (width <= 0 || height <= 0) {
        throw std::runtime_error("width and height must be positive");
    }
}

void World::clear() {
    std::fill(cells_.begin(), cells_.end(), 0);
}

void World::randomize(double alive_prob) {
    if (alive_prob < 0.0 || alive_prob > 1.0) {
        throw std::runtime_error("alive_prob must be between 0 and 1");
    }

    static thread_local std::mt19937 rng{std::random_device{}()};
    std::bernoulli_distribution dist(alive_prob);

    for (auto &cell : cells_) {
        cell = dist(rng) ? 1 : 0;
    }
}

int World::get_cell(int x, int y) const {
    if (x < 0 || x >= width_ || y < 0 || y >= height_) {
        throw std::runtime_error("coordinates out of range");
    }
    return cells_[index(x, y)];
}

void World::set_cell(int x, int y, int value) {
    if (x < 0 || x >= width_ || y < 0 || y >= height_) {
        throw std::runtime_error("coordinates out of range");
    }
    if (value != 0 && value != 1) {
        throw std::runtime_error("cell value must be 0 or 1");
    }
    cells_[index(x, y)] = static_cast<std::uint8_t>(value);
}

int World::count_alive_neighbors(int x, int y) const {
    int count = 0;

    // Recorremos los 8 vecinos
    for (int dy = -1; dy <= 1; ++dy) {
        for (int dx = -1; dx <= 1; ++dx) {
            if (dx == 0 && dy == 0) {
                continue; // saltar la propia celda
            }
            int nx = x + dx;
            int ny = y + dy;

            if (nx < 0 || nx >= width_ || ny < 0 || ny >= height_) {
                continue; // fuera de los límites, se considera muerta
            }

            if (cells_[index(nx, ny)] == 1) {
                ++count;
            }
        }
    }

    return count;
}

void World::step() {
    std::vector<std::uint8_t> new_cells = cells_;

    for (int y = 0; y < height_; ++y) {
        for (int x = 0; x < width_; ++x) {
            int alive_neighbors = count_alive_neighbors(x, y);
            int current = cells_[index(x, y)];

            std::uint8_t next_state = current;

            if (current == 1) {
                // Una célula viva con menos de 2 o más de 3 vecinos muere
                if (alive_neighbors < 2 || alive_neighbors > 3) {
                    next_state = 0;
                }
            } else {
                // Una célula muerta con exactamente 3 vecinos vivos nace
                if (alive_neighbors == 3) {
                    next_state = 1;
                }
            }

            new_cells[index(x, y)] = next_state;
        }
    }

    cells_.swap(new_cells);
}

