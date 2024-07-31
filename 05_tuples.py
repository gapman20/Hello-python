### Tuples ###

my_tuple = tuple() # Forma de definir a una tupla 
my_other_tuple = () # Esta forma de definir a la tupla solo con paréntesis. Nota: Para las listas es con []

my_tuple = (28, 1.75, 'Gabriel', 'Alvarez', 'Alvarez')
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) Es un Index Error sale del parámetro
# print(my_tuple[-6]) Es un Index Error sale del parámetro

print(my_tuple.count('Alvarez')) # Encuentra dos veces la palabra u objeto
print(my_tuple.index('Gabriel')) # Indica el indice del objeto
print(my_tuple.index('Alvarez')) # Indica el indice del objeto

#my_tuple[1] = 1.80 Es un error porque no lo podemos modificar 

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple) # Si podemos agregar otra tupla a la tupla

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = 'Patita'
my_tuple.insert(1, 'Azul')
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple # Elimina la variable  
# print(my_tuple) NameError: name 'my_tuple'is not defined, 