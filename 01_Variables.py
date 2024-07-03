# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print 
print(my_string_variable, str(my_int_variable),my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas Funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea. CUIDADO CON ABUSAR DE ESTA SINTAXIS
name, surname, alias, age = "Gabriel","Alvarez", "Gabo", 28
print("Me llamo",name,surname,"Tengo",age, "años","Y mi alias es",alias)

#input
'''
name = input('What is your name: ')
age = input('How old are you? ')

print(name)
print(age)
'''

# Cambiamos su tipo
name = 28
age = "Gabriel"
print(name)
print(age)

# Forzamos el tipo
address: str = "Mi dirección"
address = 32
print(address)