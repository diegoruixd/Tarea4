# Ejercicio 6
import numpy as np

arr = np.zeros((10, 10, 10), dtype=int)
i_idx = np.arange(10)[1::2]
j_idx = np.arange(10)[::2]

def primos_hasta(n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(np.sqrt(n)) + 1):
        sieve[i*i:n+1:i] = False
    return np.flatnonzero(sieve)

k_idx = primos_hasta(9)
I, J, K = np.meshgrid(i_idx, j_idx, k_idx, indexing='ij')
arr[I, J, K] = 1

# Verificar resultado
print("Número total de 1's:", np.sum(arr))
