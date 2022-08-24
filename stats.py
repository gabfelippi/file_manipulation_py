# Procura pelo menor valor dentro de uma lista e o retorna
def min(valores):
    minimo = valores[0]
    for valor in valores:
      if valor < minimo:
        minimo = valor
    return minimo

# Procura pelo maior valor dentro de uma lista e o retorna
def max(valores):
    maximo = valores[0]
    for valor in valores:
      if valor > maximo:
        maximo = valor
    return maximo

def quad(valor):
    return valor**2