#comparacion usuarios
usuario = 'espadachinnegro'
password = 'Sao52689658'
#input nos sirve para ingresar datos 
usuario_por_teclado=input('ingrese su usuario: ')
password_por_teclado=input('ingrese su password: ')

print(usuario == usuario_por_teclado)
print(password == password_por_teclado)

#condicionales
#si condicion se cumple: True
    #codigo a ejecutar en caso de
    #que la condicion se cumpla
#si condicion no se cumple: False
    #codigo a ejecutar en caso de
    #que la condicion se cumpla

#de la contrario
    #codigo a ejecutar en caso de 
    #que la condicion no se cumpla

edad = 18
if edad >= 18:
    print('sos mayor de edad')
else:
    print('sos menor de edad')


validacion = usuario == usuario_por_teclado
if validacion == True:
    print('El usuario valido')
else:
    print('el usuario es incorrecto salame')

validacion_password = password == password_por_teclado
if password == password_por_teclado:
    if validacion_password == True:
        print('la password es correcta')
    else:
        print('password no es correcta')

validacion_de_datos= validacion and validacion_password
if validacion and validacion_password:
    if validacion_de_datos == True:
        print("iniciando sesion")
    else:
        print("verifica los datos")

#ejercicio como saber si estoy bien de money
#crear un programa que te permita saber cuanto es tu ingreso mensual
#que te permita saber cuanto te queda restandole los gastos del mes
#que te permita saber tu situacion economica
#cuanto te queda
ingreso_mensual = int(input("ingrese sus transacciones: "))
gasto_mensual = int(input("ingrese su gasto: "))
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print('bien pa, estas bien')
    else:
        print('y pa, estas gastando una banda, hay que ver si te alcanza')

elif ingreso_mensual > 1000:
    print ("estas bien en latinoamerica")
elif ingreso_mensual > 500:
    print ("estas bien en Argentina")
elif ingreso_mensual > 200:
    print ("estas bien en venezuela")

else:
    print("buscate un laburo con mejor sueldo")

print(f'tus ingresos son {ingreso_mensual}' )
print(f'gastos del mes {gasto_mensual}')

print(f'te queda {ingreso_mensual-gasto_mensual}')
