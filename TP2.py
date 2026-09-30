""" 
El algoritmo plantea una matriz de n * n, siendo n la cantidad de monedas. 
Luego determiana los casos base, siendo estos, tener una sola mondea
donde el optimo es la moneda en si, y el caso donde tiene dos monedas,
donde el optimo es la mas grande entre la dos.
Luego recorre la parte superior de la matriz (ya que los punteros i, j que 
apuntan al principio y final del array de monedas respectivametne, nunca se
intercambian, lo que es igual, se cummple que i <= j).
Cuando recorre la matriz lo que analiza es los dos casos posibles

1.
Sophia toma la primera moneda, la moneda i
Mateo elige la mayor entre las monedas i + 1 y j

1.a.
Si mateo eligio la moneda i + 1
El rango (i, j) se achica a (i + 2, j), por lo que nuestra solucion sera
el valor de la moneda i mas la solucion del rango (i + 2, j)

opt(i, j) = moneda_i + opt(i + 2, j)

1.b.
Si mateo eligio la moneda j
El rango (i, j) se achica a (i + 1, j - 1), por lo que nuestra solucion sera
el valor de la moneda i mas la solucion del rango (i + 1, j - j)

opt(i, j) = moneda_i + opt(i + 1, j - 1)


2.
Sophia toma ahora la ultima moneda, la moneda j
Mateo elige la mayor entre las monedas i y j - 1

2.a.
Si mateo eligio la moneda i
El rango (i, j) se achica a (i + 1, j - 1), por lo que nuestra solucion sera
el valor de la moneda j mas la solucion del rango (i + 1, j - 1)

opt(i, j) = moneda_j + opt(i + 1, j - 1)

2.b.
Si mateo eligio la moneda j
El rango (i, j) se achica a (i, j - 2), por lo que nuestra solucion sera
el valor de la moneda j mas la solucion del rango (i, j - 2)

opt(i, j) = moneda_i + opt(i, j - 2)


Luego de plantear las cuatro posibles situaciones, puedo ver que, 
sin importar lo que elija sophia, mateo siempre elije la moneda mas grande
por lo que en ambos casos en simplemente realizar una comparacion para ver cual 
es mas grande, segun la situacion de monedas. Esta comparacion determina el rango
de mis soluciones parciales. Luego obtengo mis soluciones parciales para los rangos 
respectivos segun la eleccion de mateo, me quedo con aquella solucion, que maximize mi 
ganancia. Entonces

Siendo opt_i, la solucion para un rango (i_i, j_i), asumiendo que sophia toma la moneda i, y
Siendo opt_j, la solucion para un rango (i_j, j_j), asumiendo que sophia toma la moneda j

Nuestro optimo para el rango (i, j) queda de la siguente manera 

opt(i, j) = max(moneda_i + opt_i, moneda_j + opt_j)
opt(i, j) = max(
        monedas[i] + opt(i + 2, j) si monedas[i + 1] > monedas[j] sino opt(i + 1, j - 1),
        monedas[j] + opt(i + 1, j - 1) si monedas[i] > monedas[j - 1] sino opt(i, j - 2)
    )
    
    
2. Complejdiad

El algoritmo para obtener la matriz optima, tiene la siguente complejidad.

a. Crear la matriz opt de N x N O(N^2)
b. Plantear los casos base de una moneda O(N)
c. Plantear los casos base de dos monedas O(N)
d. Completar la matriz optima O(N^2), recorro la matriz de N x N y hago un trabajo de O(1) por iteracion

Por lo que la complejidad nos queda

T(N) = O(N^2 + N + N + N^2) = O(N^2)

El algoritmo para reconstruir la solucion
"""
import sys

def elegir(monedas):
    opt = [[0] * len(monedas) for i in range(len(monedas))]
    
    # Casos base con una moneda
    for i in range(0, len(monedas)):
        opt[i][i] = monedas[i]
        
    # Casos base con 2 monedas
    for i in range(0, len(monedas) - 1):
        j = i + 1
        opt[i][j] = max(monedas[i], monedas[j])
    
    for i in range(len(opt) - 1, -1, -1):
        for j in range(i + 2, len(opt)):
            # Sophia toma la primera
            # Achico mi rango segun lo que eliga Mateo
            opt_i = opt[i + 2][j] if monedas[i + 1] > monedas[j] else opt[i + 1][j - 1]
            
            # Sophia toma la ultima
            # Achico mi rango segun lo que eliga Mateo
            opt_j = opt[i + 1][j - 1] if monedas[i] > monedas[j - 1] else opt[i][j - 2]
            
            opt[i][j] = max(monedas[i] + opt_i, monedas[j] + opt_j)
            
            
    sol = solucion(opt, monedas, [], 0, len(opt) - 1)
    return sol

def solucion(opt, monedas, s, i, j):
    if i > j:
        return s
    
    if i == j:
        s.append(i)
        return s
    
    opt_i = opt[i + 2][j] if monedas[i + 1] > monedas[j] else opt[i + 1][j - 1]
    opt_j = opt[i + 1][j - 1] if monedas[i] > monedas[j - 1] else opt[i][j - 2]
    
    if monedas[i] + opt_i > monedas[j] + opt_j:
        s.append(i)
        
        if monedas[i + 1] > monedas[j]:
            return solucion(opt, monedas, s, i + 2, j)
        else:    
            return solucion(opt, monedas, s, i + 1, j - 1)
    else:
        s.append(j)
        
        if monedas[i] > monedas[j - 1]:
            return solucion(opt, monedas, s, i + 1, j - 1)
        else:
            return solucion(opt, monedas, s, i, j - 2)

def procesar_texto(archivo):
    with open(archivo, "r") as arc:
        arc.readline()
        linea = arc.readline().strip()
        monedas = [int(x) for x in linea.split(";")]
    return monedas

    
def main():
    ruta_entrada = sys.argv[1]
    try:
        datos = procesar_texto(ruta_entrada)
        if datos:
            elegidos = elegir(datos)
            
            for i in range(len(elegidos)):
                print("Ultima moneda para " if elegidos[i] else "Primera moneda para ", end="")
                print("Sophia; " if not (i % 2) else "Mateo; ", end="")

        else:
            print("El archivo no contiene datos válidos")
            sys.exit(1)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()