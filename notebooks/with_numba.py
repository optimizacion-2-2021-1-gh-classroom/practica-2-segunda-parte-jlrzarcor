from hill_final import *
import time
import numba
from numba import jit
from functools import wraps
import click
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

@click.group()
def cli():
    pass

def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        ts = time.time()
        result = f(*args, **kwargs)
        te = time.time()
        print(f"print(f'fun: {f.__name__}, args: [{args}, {kwargs}] took: {te - ts} seconds")
        return result
    return wrap

@timing
@jit(parallel=True)
def best_solution_jit(coordinate, initial_point=0, tolerance=1e-7):
    """
    Finds an optimal solution for the TSP problem using hill climbing algorithm
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



@timing
def best_solution(coordinate, initial_point=0, tolerance=1e-7):
    """Regular Function"""
    """
    Finds an optimal solution for the TSP problem using hill climbing algorithm
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

    for _ in range(itera):
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




@cli.command()
@click.option('--threads/--no-jit', default=False)
def thread_test(threads):
    dat = pd.read_csv("https://raw.githubusercontent.com/optimizacion-2-2021-1-gh-classroom/practica-2-segunda-parte-jlrzarcor/main/datasets/tsp.csv")
    dat1 = dat.to_numpy()
    rea = dat1[0:30, :]

    if threads:
        click.echo(click.style('Running with multicore threads', fg='green'))
        return best_solution_jit(rea)
    else:
        click.echo(click.style('Running NO THREADS', fg='red'))
        return best_solution(rea)

if __name__ == "__main__":
    cli()




