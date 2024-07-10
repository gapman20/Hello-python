## Operadores Aritméticos##

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 2) #Residual 
print(10 // 3) #Division mas aproximada al entero
print(2 ** 3) # Exponente
print(2 ** 3 + 3 - 7 / 1 //4)


print('Hola ' + 'Python ' + '¿Qué tal?')
print('Hola ' + str(5))
print('Hola ' * 5) # Sale 5 veces el string Hola

my_float = 2.5 * 2
print('Hola ' * int(my_float))


## Operadores Comparativos ##

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

print('Separación')

print('Hola' > 'Python')
print('Hola' < 'Python')
print('aaaa' >= 'abaa') #Ordenación alfabética por ASCII
print(len('aaaa') >= len('abaa')) #Cuenta caracteres
print('Hola' <= 'Python')
print('Hola' == 'Hola')
print('Hola' != 'Python')

## Operadores lógicos ##

print(3 > 4 and 'Hola' > 'Python')
print(3 > 4 or 'Hola' > 'Python')
print(3 < 4 and 'Hola' < 'Python')
print(3 < 4 or 'Hola' > 'Python')
print(3 < 4 or ('Hola' > 'Python' and 4 == 4))
print(not(3 > 4 ))