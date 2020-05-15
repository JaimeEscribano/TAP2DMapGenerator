from post_processing.post_process import PostProcess


class Soften(PostProcess):
	def __init__(self, data, iterations: int = 4, sample_size: int = 1):
		super().__init__(data)
		self._iterations = iterations
		self._sample_size = sample_size

	def do_work(self) -> [[float]]:
		"""
		Realiza su trabajo
		:param data: Datos a transformar
		:return: Datos transformados
		"""
		for i in range(self._iterations):
			new_data = []
			for y, row in enumerate(self._data):
				new_row = []
				for x, value in enumerate(row):
					new_row.append(self.get_surrounding_average(x, y))
				new_data.append(new_row)
		return self._data

	def get_surrounding_average(self, center_x: int, center_y: int) -> float:
		"""
		Devuelve el valor medio entre los vecinos
		:param center_x: posición x a comprobar
		:param center_y: posición y a comprobar
		:return: media de valores
		"""
		num = 0
		avg = 0
		for x in range(center_x - self._sample_size, center_x + self._sample_size + 1):
			for y in range(center_y - self._sample_size, center_y + self._sample_size + 1):
				if 0 <= x < len(self._data) and 0 <= y < len(self._data):
					num += 1
					avg += self._data[x][y]
		if num > 0:
			avg /= num
		return avg

	def __str__(self):
		return self.__class__.__name__
