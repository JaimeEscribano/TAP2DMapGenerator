from post_processing.post_process import PostProcess


class CellularAutomata(PostProcess):
	def __init__(self, data: [[float]], iterations: int = 4):
		super().__init__(data)
		self._iterations = iterations

	def do_work(self) -> [[float]]:
		"""
		A partir de la entrada, realiza self._iterations iteraciones de algoritmo
		autómata celular
		:return: Datos transformados
		"""
		for i in range(self._iterations):
			new_data = []
			for y, row in enumerate(self._data):
				new_row = []
				for x, value in enumerate(row):
					neighbours = self.get_surrounding_active_cells(x, y)
					new_row.append(1 if self.validate(neighbours) else 0)
				new_data.append(new_row)
			self._data = new_data
		return self._data

	def validate(self, active_neighbours: int) -> bool:
		return active_neighbours > 3

	def get_surrounding_active_cells(self, x: int, y: int) -> int:
		"""
		Número de celdas activas entre los ocho vecinos
		:param x: coordenada x a comprobar
		:param y: coordenada y a comprobar
		:return: número de vecinos vivos de la posición
		"""
		alive = 0
		if x > 0 and y > 0:
			# Top Left
			if self._data[x - 1][y - 1] > 0.5:
				alive += 1
		if y > 0:
			# Top
			if self._data[x][y - 1] > 0.5:
				alive += 1
		if x < len(self._data[0]) - 1 and y > 0:
			# Top right
			if self._data[x + 1][y - 1] > 0.5:
				alive += 1
		if x > 0:
			# Left
			if self._data[x - 1][y] > 0.5:
				alive += 1
		if x < len(self._data[0]) - 1:
			# right
			if self._data[x + 1][y] > 0.5:
				alive += 1
		if x > 0 and y < len(self._data) - 1:
			# Bottom Left
			if self._data[x - 1][y + 1] > 0.5:
				alive += 1
		if y < len(self._data) - 1:
			# Bottom
			if self._data[x][y + 1] > 0.5:
				alive += 1
		if x < len(self._data[0]) - 1 and y < len(self._data) - 1:
			# Bottom right
			if self._data[x + 1][y + 1] > 0.5:
				alive += 1
		return alive

	def __str__(self):
		return self.__class__.__name__
