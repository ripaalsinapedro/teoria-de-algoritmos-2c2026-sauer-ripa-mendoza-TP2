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
            
    
    maxima_ganancia = opt[0][len(opt) - 1]
    sol = solucion(opt, monedas, [], 0, len(opt) - 1)
    return maxima_ganancia, sol

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
            ganancia_Sophia, elegidos = elegir(datos)
            
            ganancia_max = sum(datos)
            ganancia_Mateo = ganancia_max - ganancia_Sophia
            
            if ganancia_Sophia > ganancia_Mateo:
                for i in range(len(elegidos)):
                    print("Ultima moneda para " if elegidos[i] else "Primera moneda para ", end="")
                    print("Sophia; " if not (i % 2) else "Mateo; ", end="")
                
                print("")
                print("Gnancia de Sophia: ", ganancia_Sophia)
                print("Ganancia de Mateo: ", ganancia_Mateo)
            else:
                print("El algorimto fallo gano Mateo, o empataron")
        else:
            print("El archivo no contiene datos válidos")
            sys.exit(1)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()