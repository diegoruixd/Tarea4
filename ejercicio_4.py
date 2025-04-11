# Ejercicio 4
import numpy as np

scores = np.array([78, 98, 45, 55, 72, 48, 85, 40, 65, 30, 90, 58, 53])
indices_menores_60 = np.flatnonzero(scores < 60)
indices_a_cambiar = indices_menores_60[:3]
scores[indices_a_cambiar] = 0

# Ver resultado
print(scores)
