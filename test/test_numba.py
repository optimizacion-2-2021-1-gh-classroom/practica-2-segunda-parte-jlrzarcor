from hill_final import *
import time
import numpy as np
import numba
from numba import jit
from functools import wraps
import os

os.chdir("../")

from src.hill_cg.hill import *


def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        ts = time.time()
        result = f(*args, **kwargs)
        te = time.time()
        return result
    return wrap

@timing
@jit(parallel=True)
def best_solution(coordinate, initial_point=0, tolerance=1e-7):
    """
    finds an optimal solution for the TSP problem using hill climbing algorithm
        input:
            points[array]: coordinates of the places to be visited
            initial_point[integer]: number of the place to be visited first
            tolerance[float]: value that indicates the solution is not improving
        outputs:
            bst_distance[float]: distance of the best route
            best_sol[list]: order the places to be visted in the optimal solution
            time[float]: time that take the algorithm to obtain the solution
    """

    start_time = time.time()
    matrix = distance_matrix(coordinate)

    current_solution = random_solution(matrix, initial_point)
    current_path = calculate_distance(matrix, current_solution)
    neighbor = neighbors(matrix, current_solution)[0]
    best_neighbor, best_neighbor_path = neighbors(matrix, neighbor)
    global_path = 2 * current_path
    itera = 400

    for _ in numba.prange(itera):
        while best_neighbor_path < current_path:
            while abs(best_neighbor_path - current_path) > tolerance:
                current_solution = best_neighbor
                current_path = best_neighbor_path
                neighbor = neighbors(matrix, current_solution)[0]
                best_neighbor, best_neighbor_path = neighbors(matrix, neighbor)

        if current_path < global_path:
            global_path = current_path
            global_solution = current_solution

        current_solution = random_solution(matrix, initial_point)
        current_path = calculate_distance(matrix, current_solution)
        neighbor = neighbors(matrix, current_solution)[0]
        best_neighbor, best_neighbor_path = neighbors(matrix, neighbor)

    return global_path, global_solution, time.time() - start_time



sources = np.array([
    [40.73024833, -73.79440675],
    [41.47362495, -73.92783272],
    [41.26591   , -73.21026228],
    [41.3249908 , -73.507788  ]
])

distance_with_numba, b, c = best_solution(sources)
print(distance_with_numba)


from python_tsp.distances import euclidean_distance_matrix
from python_tsp.exact import solve_tsp_dynamic_programming

distance_matrix = euclidean_distance_matrix(sources)
permutation, distance_without_numba = solve_tsp_dynamic_programming(distance_matrix)


def test_distance():
   assert np.linalg.norm(distance_without_numba - distance_with_numba) < 1e-3
