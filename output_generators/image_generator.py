import numpy as np
from PIL import Image, ImageDraw

from output_generators.output_generator import OutputGenerator
from utils import normalized_val


class ImageGenerator(OutputGenerator):
	"""
	Guarda los datos en una imagen
	"""
	def __init__(self, data: [[float]], path: str, water=(30,144,255),
				 snow=(255,250,250), high_mountain = (139,69,19),
				 forest = (34,139,34), valley = (127,255,0),
				 beach = (255,250,205)):
		"""
		Constructor
		:param data: datos a representar
		:param path: ruta del fichero a crear
		:param min_color: color asociado al valor mínimo de data
		:param max_color: color asociado al valor máximo de data
		"""
		super().__init__(data, path)
		self.water = water
		self.snow = snow
		self.forest = forest
		self.valley = valley
		self.high_mountain = high_mountain
		self.beach = beach
		self.__min_value = np.min(data)
		self.__max_value = np.max(data)

	def generate_output(self) -> None:
		"""
		Genera una imagen a partir de una matriz de datos
		"""
		# (0, 0) = esquina superior izquierda
		img = Image.new('RGB', (len(self._data), len(self._data[0])))
		draw = ImageDraw.Draw(img)
		for y, row in enumerate(self._data):
			for x, value in enumerate(row):
				draw.point((x, y), fill=self.get_target_color(value))
		del draw

		img.save(self._path)

	def get_target_color(self, val: float) -> (int, int, int):
		"""
		Obtiene el color correspondiente a un valor.
		Será max_color si el valor es el valor máximo de self._data,
		min_color si es el valor mínimo y uno intermedio en otro caso
		:param val: valor del que queramos obtener el color
		:return: color RGB con valoers en el rango 0-255
		"""
		if val == 1: target_r, target_g, target_b = self.snow
		elif val == 0.8: target_r, target_g, target_b = self.high_mountain
		elif val == 0.6: target_r, target_g, target_b = self.forest
		elif val == 0.4: target_r, target_g, target_b = self.valley
		elif val == 0.1: target_r, target_g, target_b = self.beach
		else: target_r, target_g, target_b = self.water



		return target_r, target_g, target_b
