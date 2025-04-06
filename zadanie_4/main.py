import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS, VIKOR
from pymcdm.weights import entropy_weights
from pymcdm.normalizations import minmax_normalization

# Macierz decyzyjna – dane samochodów (cena, spalanie, moc, pojemność bagażnika)
matrix = np.array([
    [109900, 5.5, 140, 470],   # Toyota Corolla
    [117000, 6.1, 150, 381],   # Volkswagen Golf
    [112000, 6.0, 122, 358],   # Mazda 3
    [105000, 5.8, 120, 395]    # Hyundai i30
])

# Typy kryteriów: -1 (min), 1 (max)
types = [-1, -1, 1, 1]

# Normalizacja i wagi
norm_matrix = minmax_normalization(matrix, types)
weights = entropy_weights(norm_matrix)

# Obliczenia metodami
topsis = TOPSIS()
bounds = [
    [matrix[:, i].min(), matrix[:, i].max()] for i in range(matrix.shape[1])
]
spotis = SPOTIS(bounds)
vikor = VIKOR()

topsis_scores = topsis(matrix, weights, types)
spotis_scores = spotis(matrix, weights, types)
vikor_scores = vikor(matrix, weights, types)

# Alternatywy
cars = ['Toyota Corolla', 'Volkswagen Golf', 'Mazda 3', 'Hyundai i30']

df = pd.DataFrame({
    'Samochód': cars,
    'TOPSIS': topsis_scores,
    'SPOTIS': spotis_scores,
    'VIKOR': vikor_scores
})

df['TOPSIS_rank'] = df['TOPSIS'].rank(ascending=False)
df['SPOTIS_rank'] = df['SPOTIS'].rank()
df['VIKOR_rank'] = df['VIKOR'].rank()

print(df)