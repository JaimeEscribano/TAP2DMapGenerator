from post_processing.post_process import PostProcess


class Polarize(PostProcess):
	"""
	Este postproceso polariza la entrada, convirtiendo en 0 todos los valores inferiores a un umbral y a 1 el resto
	"""

	def __init__(self, data, upper_threshold=0.9,_higher_threshold = 0.7,  high_threshold = 0.5, middle_threshold = 0.3):
		super().__init__(data)
		self._threshold = upper_threshold
		self._higher_threshold = _higher_threshold
		self._lower_threshold = middle_threshold
		self.high_threshold = high_threshold

	def do_work(self) -> [[float]]:
		"""
		Realiza su trabajo
		:param data: Datos a transformar
		:return: Datos transformados
		"""
		return [[1.0 if self._data[x][y] >= self._threshold
				 else 0.8 if self._data[x][y] >= self._higher_threshold
		else 0.6 if self._data[x][y] >= self.high_threshold
		else 0.4 if self._data[x][y] >= self._lower_threshold
		else 0.1 if self._data[x][y] >= self._lower_threshold/1.2
		else 0.0 for x in range(len(self._data[0]))] for y in range(len(self._data))]

	def __str__(self):
		return self.__class__.__name__
