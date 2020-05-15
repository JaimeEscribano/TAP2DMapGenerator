import numpy as np


def normalized_val(val: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
	"""
	Normaliza un valor entre 0 y 1 comparativamente a min_val y max_val
	:param val: valor a normalizar
	:param min_val: valor mínimo de referencia (será igual a 0)
	:param max_val: valor máximo de referencia (será igual a 1)
	:return: valor normalizado entre 0 y 1
	"""
	return (val - min_val)/(max_val - min_val)


def normalized(data: [[float]]) -> [[float]]:
	"""
	Normaliza una matriz, transformándola para que su valor mínimo sea 0.0 y el máximo 1.0
	:param data:
	:return:
	"""
	transformed = np.copy(data)
	max_val = np.max(transformed)
	min_val = np.min(transformed)

	for r in range(len(transformed)):
		for c in range(len(transformed[r])):
			transformed[r][c] = normalized_val(transformed[r][c], min_val, max_val)
	return transformed
