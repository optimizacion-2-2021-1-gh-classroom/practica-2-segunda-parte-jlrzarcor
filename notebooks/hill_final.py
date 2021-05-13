import time
import random
import numpy as np




def distance_matrix(coordinate):
    """
    calculate the distance among each suggest solution point
        input:
            coordinate[array]: array containig the points to be visited
        outputs:
            matrix[array]: nxn array with distances among solution points
    """
    matrix = []
    for i in range(len(coordinate)):
        for j in range(len(coordinate)):
            p = np.linalg.norm(coordinate[i] - coordinate[j])
            matrix.append(p)
    matrix = np.reshape(matrix, (len(coordinate), len(coordinate)))
    # print(matrix)
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
    solution = [initial_point]
    points.remove(initial_point)
    for i in range(0, len(matrix) - 1):
        random_point = points[random.randint(0, len(points) - 1)]
        solution.append(random_point)
        points.remove(random_point)

    return solution


def calculate_distance(matrix, solution):
    """
    returns the distance associated with a solution
        input:
            matrix[array]: distance between points
            solution[list]: contains a propose random solution
        output:
            distance[float]: distance cover a propose solution
    """
    distance = 0
    for i in range(0, len(solution)):
        distance += matrix[solution[i]][solution[i - 1]]
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
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
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
