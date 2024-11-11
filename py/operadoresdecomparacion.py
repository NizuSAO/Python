#true o false
#operadores de comparacion
#==
#!=
#>
#=>
#<
#>=

#con 1 solo = estamos asignando con == estamos afirmando que un valor es igual a otro
es_igual_que = 5 == 6
#la expresion != es que decimos que un valor es distinto de otro 
es_distinto_de = 5 !=6
#la expresion > dice que el valor 5 es mayor que 6
mayor_que = 5 > 6
#la expresion < dice que el valor 5 es menor que 6
menor_que = 5 < 6
#la expresion >= 5 es mayor o igual a 6
mayor_o_igual = 5 >= 6
#la expresion <= 5 es menor o igual a 6
menor_o_igual = 5 <= 6

print(es_igual_que)#false
print(es_distinto_de)#true
print(mayor_que)#false
print(menor_que)#true
print(mayor_o_igual)#false
print(menor_o_igual)#true=

#calculos combinados
a=45
b=4
c=65

comparacion = a + b < c

print(comparacion)


#comparacion usuarios
usuario = 'espadachinnegro'
password = 'Sao52689658'
#input nos sirve para ingresar datos 
usuario_por_teclado=input('ingrese su usuario: ')
password_por_teclado=input('ingrese su password: ')

print(usuario == usuario_por_teclado)
print(password == password_por_teclado)
