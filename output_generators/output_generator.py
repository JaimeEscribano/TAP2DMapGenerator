import numpy as np


class OutputGenerator:
	"""
	Superclase de todos los output generators (generadores de ficheros a partir de datos)
	"""
	def __init__(self, data, path):
		"""
		Genera un fichero a partir de unos datos
		:param data: datos a guardar
		:param path: ruta del fichero
		"""
		self._data = np.copy(data)
		self._path = path
