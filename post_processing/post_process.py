import numpy as np


class PostProcess:
	"""
	Superclase de los post procesos, que se encargan de transformar unos datos de entrada siguiendo un algoritmo
	"""
	def __init__(self, data):
		self._data = np.copy(data)

	def do_work(self) -> [[float]]:
		"""
		Realiza su función de postprocessing
		:return: Datos transformados
		"""
		return [[]]
