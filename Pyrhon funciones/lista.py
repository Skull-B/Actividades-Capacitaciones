# frutas = ["manzana", "banana", "cereza", "durazno", "fresa", "guayaba"]

# verduras = list(["lechuga", "tomate", "pimiento", "zanahoria"])
# verduras.insert(0, "cebolla")

# frutas.append ("naranja")
# print(frutas)

# fuera = verduras.pop()
# print(verduras)

# frutas.remove("banana")
# print(frutas)

# frutas.clear()
# print(frutas)

milist = ['manzana', 'banana', 'cereza', 'durazno', 'fresa', 'guayaba']
print(milist[1:4])

miLista = ['manzana', 'banana', 'cereza', 'durazno', 'fresa', 'guayaba']
miLista[1:2] = ['naranja', 'pera']
print (miLista[2])

nuevaLista =[x for x in miLista if x=='banana']
print (nuevaLista)
