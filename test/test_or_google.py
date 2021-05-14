import google_or_tools_tsp as tsp
import pandas as pd
import os
import numpy as np

os.chdir("../")
from src.hill_cg.hill import *


dat = pd.read_csv("https://github.com/optimizacion-2-2021-1-gh-classroom/practica-2-segunda-parte-jlrzarcor/tree/main/datasets/tsp.csv")
dat1 = dat.to_numpy()
ciudades = dat1[0:17, :]


# Distancia de nuestro de método
hc_best_dist = best_solution(ciudades, 0 , 1e-9, 300)
# Distancia de Google OR-tools
tsp_sol = tsp.main(ciudades)

#Test
test = 1 - hc_best_dist/tsp_sol

# Validar test
def test_distance():
    assert np.linalg.norm(test - 0.1) < 1e-1