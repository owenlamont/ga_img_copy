# fitness.py

from genome import Genome, set_image_dimensions as genome_set_image_dimensions
import numpy as np
from numpy.typing import NDArray
from renderer import (
    render_genome,
    set_image_dimensions as renderer_set_image_dimensions,
)
from skimage.metrics import mean_squared_error


def fitness_worker(
    genome: Genome, target_array: NDArray[np.uint8], image_width: int, image_height: int
) -> Genome:
    # Set image dimensions in worker process
    renderer_set_image_dimensions(image_width, image_height)
    genome_set_image_dimensions(image_width, image_height)

    generated_image = render_genome(genome)
    generated_array = np.array(generated_image)
    mse = mean_squared_error(target_array, generated_array)
    genome.fitness = mse
    return genome
