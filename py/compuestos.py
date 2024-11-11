#las listas nos sirven para agrupar datos las matrices son un conjunto de datos que se puede modificar
#en programacion se cuenta desde el 0 
lista = ["dalto", "soy dalto", True, 1.85]
lista[2]="Maquinola"
print(lista)
print(lista[2])
#Tuplas tambien son conjunto de datos es una matriz, con la diferencia de que no se puede modificar
tupla=("dalto", "soy dalto", True, 1.85)
#tupla(2)=("ashen")
print(tupla[2])


#conjunto o set, se puede modificar pero no el elemento
#tampoco se puede acceder por el indicie a un elemento del conjunto y repetir valores
set={"dalto", "soy dalto", True, 1.85}
print(set)

#creando un diccionario (dict)
#key : valor
diccionario = {
    "nombre" : "Nizu",
    "canal" : "dsnizu",
    "es real": True,
    "altura" : 1.70,
    "sword": "Excalibur",
    "abrigo": "Media noche",
    "sword2": "rosaazul",
    "hack": "inmunidad",
    "alias": "kiritohacks"
    }

print(diccionario["sword"])
