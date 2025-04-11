# Ejercicio 5
import numpy as np

# Posiciones dadas
locs = np.array([
    [0, 0, 0],
    [1, 1, 2],
    [0, 0, 0],
    [2, 1, 3],
    [5, 5, 4],
    [5, 0, 0],
    [5, 0, 0],
    [0, 0, 0],
    [2, 1, 3],
    [1, 3, 1]
])

generator = np.random.default_rng(1010)
weights = np.abs(generator.normal(size=10))  # Todos positivos
out_of_bounds = np.any(locs >= 5, axis=1)
valid_fish_idx = np.where(~out_of_bounds)[0]
valid_locs = locs[valid_fish_idx]
valid_weights = weights[valid_fish_idx]
flat_indices = np.ravel_multi_index(valid_locs.T, dims=(5, 5, 5))
unique_cells, inverse_idx = np.unique(flat_indices, return_inverse=True)
max_fish_per_cell = np.zeros_like(unique_cells, dtype=int)

for i, cell in enumerate(unique_cells):
    cell_fish_idx = np.where(flat_indices == cell)[0]
    max_weight_idx = cell_fish_idx[np.argmax(valid_weights[cell_fish_idx])]
    max_fish_per_cell[i] = valid_fish_idx[max_weight_idx] 

# Ver resulatdo
surviving_fish = np.sort(max_fish_per_cell)
print("Pesos de los peces:", weights)
print("Peces que sobrevivieron (índices):", surviving_fish)
