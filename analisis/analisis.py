# Imports necesarios para el notebook
from random import seed

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp

from util import time_algorithm
from TP2 import elegir

# Siempre seteamos la seed de aleatoridad para que los resultados sean reproducibles
seed(12345)
np.random.seed(12345)

sns.set_theme() 

def get_random_array(size: int):
    return np.random.randint(0, 100.000, size)

def main():
    # La variable x van a ser los valores del eje x de los gráficos en todo el notebook
    # Tamaño mínimo=100, tamaño máximo=10kk, cantidad de puntos=20
    x = np.linspace(100, 10_000_000, 20).astype(int)

    results = time_algorithm(elegir, x, lambda s: [get_random_array(s)])

    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, [results[i] for i in x], label="Medición")
    ax.set_title('Tiempo de ejecución de elegir')
    ax.set_xlabel('Tamaño del array')
    ax.set_ylabel('Tiempo de ejecución (s)')

    # scipy nos pide una función que recibe primero x y luego los parámetros a ajustar:
    f = lambda x, c1, c2: c1 * x + c2 

    c, pcov = sp.optimize.curve_fit(f, x, [results[n] for n in x])

    print(f"c_1 = {c[0]}, c_2 = {c[1]}")
    r = np.sum((c[0] * x + c[1] - [results[n] for n in x])**2)
    print(f"Error cuadrático total: {r}")
        
    y_medido = np.array([results[n] for n in x])
    y_predicho = c[0] * x + c[1]

    ss_res = np.sum((y_medido - y_predicho)**2)
    ss_tot = np.sum((y_medido - np.mean(y_medido))**2)

    r_cuadrado = 1 - (ss_res / ss_tot)
    print(f"R² = {r_cuadrado}")
    
    
    ax.plot(x, [c[0] * n + c[1] for n in x], 'r--', label="Ajuste")
    ax.legend()
    
    plt.show()


if __name__ == '__main__':
    main()