import time
import random
import numpy as np
import numba as nb
from numba import prange


def distance_matrix(coordinate):
    """
    calculate the distance among each suggest solution point

        input:
            coordinate[array]: array containig the points to be visited
        outputs:
            matrix[array]: nxn array with distances among solution points
    """
    matrix = []
    
    for i in prange(len(coordinate)):
        for j in prange(len(coordinate)) :       
            p = np.linalg.norm(coordinate[i] - coordinate[j])
            matrix.append(p)
    matrix = np.reshape(matrix, (len(coordinate),len(coordinate)))
    #print(matrix)
    return matrix


def random_solution(matrix, initial_point):
    """
    create a random solution with the places to be visited

        input:
            matrix[array]: distance between points
            initial_point[integer]: number of the place to be visited first
        output:
            temp_solution[list]: creates random solution
    """
    points = list(range(0, len(matrix)))
    first_sol = [initial_point]
    points.remove(initial_point)
    for i in range(0, len(matrix)-1):
        random_point = points[random.randint(0, len(points) - 1)]
        first_sol.append(random_point)
        points.remove(random_point)
    first_sol.append(first_sol[0])

    return first_sol


@nb.njit(parallel=True)
def calculate_distance(matrix, sol):
    """
    returns the distance associated with a solution

        input:
            matrix[array]: distance between points
            solution[list]: contains a propose random solution 
        output:
            distance[float]: distance cover a propose solution            
    """
    distance = 0
    lend = len(sol)
    for i in prange(0, lend):
        distance += matrix[sol[i]][sol[i - 1]]
    return distance


def neighbors(matrix, solution):
    """
    create neighbors of a propose solution

        input: 
            matrix[array]: distance between points
            solution[list]: contains a propose random solution
        output:
            best_neighbor[list]: contains the best neighbor of he current solution
            best_path[float]: distance cover by the best_neighbor route
    """
    neighbors = []
    for i in range(1, len(solution)-1):
        for j in range(i + 2, len(solution)-1):
            neighbor = solution.copy()
            neighbor[i] = solution[j]
            neighbor[j] = solution[i]
            neighbors.append(neighbor)
            
    best_neighbor = neighbors[0]
    best_path = calculate_distance(matrix, best_neighbor)
    
    for neighbor in neighbors:
        current_path = calculate_distance(matrix, neighbor)
        if current_path < best_path:
            best_path = current_path
            best_neighbor = neighbor
    return best_neighbor, best_path


def nb_best_solution(coordinate, initial_point = 0, tolerance = 1e-7, n_restarts = 100):
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
    neighbor = neighbors(matrix,current_solution)[0]
    best_neighbor, best_neighbor_path = neighbors(matrix, neighbor)
    global_path = 2 * current_path
    
    for _ in prange(n_restarts):
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
        neighbor = neighbors(matrix,current_solution)[0]
        best_neighbor, best_neighbor_path = neighbors(matrix, neighbor)
        
    return global_path, global_solution, time.time() - start_time