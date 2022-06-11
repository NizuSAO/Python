from socket import *
import sys
from turtle import pu

IPServidor = "localhost"
puertoServidor = 9099

socketCliente = socket(AF_INET, SOCK_STREAM)
socketCliente.connect((IPServidor, puertoServidor))

while True:
    
    mensaje = input()
    if mensaje != 'adios':

        socketCliente.send(mensaje.encode())

        respuesta = socketCliente.recv(4096).decode()
        print(respuesta)


    else:
        socketCliente.send(mensaje.encode())
        socketCliente.close()
        sys.exit()


#now = datetime.datetime.utcnow().isoformat()

#token: with open('token.json', 'w') as token.write(‘pepe’)