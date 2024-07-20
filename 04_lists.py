### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [28,35,24,62,52,30,30]

print(my_list)
print(len(my_list))

my_other_list = [28, 1.75, "Gabriel", "Alvarez"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_other_list.count("Gabriel"))
print(my_list.count(30))
# print(my_other_list[4]) Index Error fuera de rango
# print(my_other_list[-5]) Index Error fuera de rango

age,height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3],
print(surname)

print(my_list + my_other_list)
# print(my_list + my_other_list) Error

my_other_list.append("MoureDev") #Agrega un elemento a una lista
print(my_other_list)

my_other_list.insert(1, "Rojo") #Inserta un elemento en la posición que quieras 
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30) #Es para eliminar un elemento que sabemos que esta adentro
print(my_list)

print(my_list.pop()) #Quita el ultimo elemento de la lista y retorna el elemento
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2] #Elimina por indice
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort() #Ordena a la lista de mayor a menor
print(my_new_list)

print(my_new_list[1:3])

my_list = "Hola Python"
print(my_list)
print(type(my_list))

