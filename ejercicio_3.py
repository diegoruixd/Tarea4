# Ejercicio 3
import numpy as np

generator = np.random.default_rng(1010)
puntajes_amor = np.round(generator.uniform(low=0, high=100, size=10))
diferencias = np.abs(puntajes_amor[:, np.newaxis] - puntajes_amor)

# Ver resultados
print("Puntajes de amor:")
print(puntajes_amor)
print("\nDiferencias absolutas:")
print(diferencias)
