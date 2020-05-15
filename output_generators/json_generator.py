import json

from output_generators.output_generator import OutputGenerator


class JsonGenerator(OutputGenerator):
	"""
	Guarda los datos en un json
	"""
	def generate_output(self):
		"""
		Genera un json a partir de una matriz de datos
		"""
		j = json.dumps(self._data)
		with open(self._path, 'w') as f:
			f.write(j)
