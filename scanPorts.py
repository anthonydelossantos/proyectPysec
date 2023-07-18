'''Scanner de puertos abiertos dada una direccion ip establecida o digitada al usuario. en un rango determinado. 
la info debe ser enviada a un correo especifico'''

import os
import sys
from getpass import getpass

import nmap
import smtMail
import config

nmap_path = r"'C:\Program Files (x86)\Nmap\nmap.exe'"
scanner = nmap.PortScanner(nmap_search_path=nmap_path)
mensajeFinal = ""


def clean():
    if os.name == 'posix':  # Unix/Linux/Mac
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')


try:
    begin = int(input("Puerto de inicio?: "))
    end = int(input("Puerto donde finaliza el escaneo?: "))
    target = str(input("Digite la dirección IP objetivo: "))

    print("[+] Iniciando escaneo...")
    
    for i in range(begin, end + 1):
        res = scanner.scan(target, str(i), arguments='-sC -sV')
        state = res['scan'][target]['tcp'][i]['state'] # Da el estatus del puerto (open or closed).
        version = res['scan'][target]['tcp'][i]['version']
        service = res['scan'][target]['tcp'][i]['name']
        sys.stdout.write(".") # Animacion en el proceso del escaneo
        sys.stdout.flush() 
        if i % 5 == 0:
            clean()
        if state == "open":
            mensajeFinal += f"Port {i} is {state}  (Service: {service} Version: {version})\n"
        else:
            mensajeFinal += f"Port {i} is {state}\n" # Guarda cada iteracion en una cadena
    print("Escaneo finalizado!...\n")
    print("Enviando mediante email....\n\n")

    
    remitente = config.email
    contrasena = config.password
    destino = input("Digite hacia qué correo desea enviarlo: ")
    asunto = f'Escaneo de puertos a la dirección IP {target}'
    mensaje = f"Escaneo Completo!\n\nResultado del escaneo de puertos para la dirección IP {target}:\n\n{mensajeFinal}"
    mail = smtMail.Mail()
    mail.set_values(remitente,contrasena,destino,asunto,mensaje)
    mail.set_connection()
    if mail.send_email():

        print("Correo enviado !!")
    else:
        print("Error al enviar el correo.")

except:

    print("Error!!!")