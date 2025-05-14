from sys import stdin

MOD = 10**9 + 7

particiones_mem = {}


class DisjointSet:
    def __init__(self, n):
        self.padre = list(range(n + 1))  
        self.tamaño = [1] * (n + 1)

    def find(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.find(self.padre[x])
        return self.padre[x]


    def union(self, x, y):
        raiz_x = self.find(x)
        raiz_y = self.find(y)
        if raiz_x != raiz_y:
            if self.tamaño[raiz_x] < self.tamaño[raiz_y]:
                self.padre[raiz_x] = raiz_y
                self.tamaño[raiz_y] += self.tamaño[raiz_x]
            else:
                self.padre[raiz_y] = raiz_x
                self.tamaño[raiz_x] += self.tamaño[raiz_y]

    def size(self, x):
        return self.tamaño[self.find(x)]


def contar_particiones(n):
    resultado = 0
    if n in particiones_mem:
        resultado = particiones_mem[n]
    else:
        def contar(restante, maximo):
            resultado_local = 0
            if restante == 0:
                resultado_local = 1
            elif restante < 0 or maximo == 0:
                resultado_local = 0
            else:
                combinacion = (restante, maximo)
                if combinacion in particiones_mem:
                    resultado_local = particiones_mem[combinacion]
                else:
                    suma = (contar(restante - maximo, maximo) + contar(restante, maximo - 1)) % MOD
                    particiones_mem[combinacion] = suma
                    resultado_local = suma
            return resultado_local      # return de la función contar

        resultado = contar(n, n)
        particiones_mem[n] = resultado
    
    return resultado        # return de la función contar_particiones


def procesar_caso(n, m, operaciones):
    djSet = DisjointSet(n)
    resultados = []
    for operacion in operaciones:
        partes = operacion.split()
        if partes[0] == "union":
            x = int(partes[1])
            y = int(partes[2])
            djSet.union(x, y)
        elif partes[0] == "partitions":
            x = int(partes[1])
            tam = djSet.size(x)
            resultado = contar_particiones(tam)
            resultados.append(str(resultado))
    return resultados


def main():
    T = int(input())  
    
    for i in range(T):
        n_m = stdin.readline().strip().split()
        n = int(n_m[0])
        m = int(n_m[1])
        operaciones = []
        
        for i in range(m):
            op = stdin.readline().strip()
            operaciones.append(op)
        
        resultados = procesar_caso(n, m, operaciones)

        for resultado in resultados:
            print(resultado)
main()