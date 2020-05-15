from noises.white_noise_generator import WhiteNoiseGenerator
from output_generators.image_generator import ImageGenerator
from noises.perlin_noise_generator import PerlinNoiseGenerator
from noises.simplex_noise_generator import SimplexNoiseGenerator
from output_generators.json_generator import JsonGenerator
from post_processing.cellular import CellularAutomata
from post_processing.polarize import Polarize
from post_processing.soften import Soften
from utils import normalized
import numpy as np

print('Bienvenido a la aplicación de pruebas de algoritmos procedimentales')

# Paso 1: Creación de los datos
print('Paso 1: generación del ruido base')
generator = PerlinNoiseGenerator(7, 1024, True,1)
elevation = generator.generate()


data = normalized(elevation)
# Paso 2: Procesamiento adicional
print('Paso 2: procesamiento adicional')
post = Polarize(elevation)
elevation = post.do_work()
# Paso 3: Creación de la imagen a partir de los datos finales
print('Paso 3: exportando datos')
out_gen = ImageGenerator(elevation, 'output.png')
out_gen.generate_output()
