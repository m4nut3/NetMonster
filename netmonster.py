
################################################################################
#                                 NetMonster                                   #
# -----------------------------------------------------------------------------#
# Descripción:                                                                 #
# NetMonster es una herramienta de reconocimiento inicial diseñada para        #
# automatizar el proceso de descubrimiento y análisis de servicios en máquinas #
# para la práctica de pentesting.                                              #
#                                                                              #
# Funcionalidades principales:                                                 #
# - Escaneo de puertos con Nmap (descubrimiento rápido y análisis detallado).  #
# - Detección del Sistema Operativo                                            #
# - Identificación de servicios web y análisis con WhatWeb.                    #
# - Automatización del flujo de reconocimiento inicial.                        #
# 																			   #
# Versión de Python: Python 3                                                  #
#                                               							   #
# Uso:                                                                         #
# python3 netmonster.py <ip>                                                   #
#                                                                              #
# Autor: manut3                                                                #
# Fecha de creación: 14/01/2025                                                #
# Versión: 1.0                                                                 #
#                                                                              #
# Nota: Por favor, usa esta herramienta únicamente en entornos controlados y   #
# con autorización explícita. El autor no se hace responsable del uso indebido #
# de la herramienta.                                                           #
################################################################################


import subprocess
import re
import sys
import signal
import argparse
import time


def print_banner():

#	Nombre de la función:
#    	[print_banner]

#	Descripción:
#    	[Función para la impresión del banner de la herramienta NetMonster]

	print("\n ███▄    █ ▓█████▄▄▄█████▓ ███▄ ▄███▓ ▒█████   ███▄    █   ██████ ▄▄▄█████▓▓█████  ██▀███  \n ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒▓██▒▀█▀ ██▒▒██▒  ██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒\n▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░▓██    ▓██░▒██░  ██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒\n▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ ▒██    ▒██ ▒██   ██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  \n▒██░   ▓██░░▒████▒ ▒██▒ ░ ▒██▒   ░██▒░ ████▓▒░▒██░   ▓██░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒\n░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░\n░ ░░   ░ ▒░ ░ ░  ░   ░    ░  ░      ░  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░\n   ░   ░ ░    ░    ░      ░      ░   ░ ░ ░ ▒     ░   ░ ░ ░  ░  ░    ░         ░     ░░   ░ \n         ░    ░  ░               ░       ░ ░           ░       ░              ░  ░   ░     \n")
	print("\nHerramienta de reconocimiento inicial\n\033[33;1m[!]\033[0m Ejecutar la herramienta como root\n")


def ctrlc_signal_handler(sig, frame):

#	Nombre de la función:
#    	[ctrlc_signal_handler]

#	Descripción:
#    	[Función para el manejo de la señal producida con la combinación de teclas Ctrl + C pulsada por el usuario]

	print("\n\nTerminando NetMonster...")
	sys.exit(0)

def analysis_time(tiempo_inicio):

#	Nombre de la función:
#    	[analysis_time]

#	Descripción:
#    	[Función para el cálculo del tiempo tardado en la ejecución completa del análisis al sistema objetivo]

	tiempo_final = time.time()
	
	minutos = int((tiempo_final - tiempo_inicio)/60)
	segundos = int((tiempo_final - tiempo_inicio) - (60*minutos))

	print(f"\n\033[34;1m[i]\033[0m Análisis completado en {minutos} minuto/s y {segundos} segundo/s")


def web_analyze(ip, port):

#	Nombre de la función:
#    	[web_analyze]

#	Descripción:
#    	[Función para el análisis en profundidad de los servicios web detectados con la herramienta WhatWeb.]
	
	service = "http"

	if port[1]:
		service = "https"

	whatweb_result = subprocess.run(["whatweb", f"{service}://{ip}:{port[0]}"], capture_output=True, text=True)

	print(f"\033[32;1m[+] \033[0mLanzando un whatweb {service}://{ip}:{port[0]} ...")
	print(f"\n{whatweb_result.stdout}")


def nmap_enum(ip):

#	Nombre de la función:
#    	[nmap_enum]

#	Descripción:
#    	[Enumeración de puertos y el Sistema Operativo del sistema. Crea un fichero "nmap_enum" con el output del nmap utilizado.]

	ports_string = ""
	http_ports = []

	nmap_enum = subprocess.run(["nmap", "--open", "-sS", "-O", "--osscan-guess", "-p-", "--min-rate", "4000", "-Pn", "-n", ip, "-oN", "nmap_enum"], capture_output=True, text=True)

	ports_results = re.findall(r"(\d+)/(tcp|udp)\s+(open)(.*)", nmap_enum.stdout)
	so_results = re.findall(r"Aggressive OS guesses:\s+(.*?)\,", nmap_enum.stdout)

	print(f"\033[32;1m[+] \033[0mSistema Operativo detectado: \033[32;1m{so_results[0]}\033[0m")

	print("\033[32;1m[+] \033[0mPuertos encontrados:", end=" ")

	for coincidencias in ports_results:

		if "https" in coincidencias[3]:
			http_ports.append((coincidencias[0], True))

		elif "http" in coincidencias[3]:
			http_ports.append((coincidencias[0], False))

		print(f"\033[32;1m{coincidencias[0]}\033[0m", end="")
		ports_string = ports_string + coincidencias[0]

		if len(ports_results) > ports_results.index(coincidencias)+1:
			print("\033[32;1m, \033[0m", end="")
			ports_string = ports_string + ","

	print("\n\033[32;1m[+] \033[0mFichero \033[32;1mnmap_enum\033[0m creado")
	

	try:

		print("\033[32;1m[+] \033[0mPuertos con servicios web detectados:\n")

		for ports in http_ports:
			
			print(f"\033[42;1m{ports[0]}\033[0m")
			web_analyze(ip, ports)

	except Exception as e:
		
		print("\r\033[31;1m[-]\033[0m Error al ejecutar whatweb")

	return ports_string


def nmap_versions(ip, ports_string):

#	Nombre de la función:
#    	[nmap_versions]

#	Descripción:
#    	[Función para el análisis en profundidad de los puertos enumerados previamente. Crea un fichero "nmap_versions" con el output del nmap utilizado.]

	subprocess.run(["nmap", "-sCV", f"-p{ports_string}", "-n", "-Pn", "-T5", ip, "-oN", "nmap_versions"], capture_output=True, text=True)
	print("\033[32;1m[+] \033[0mFichero \033[32;1mnmap_versions\033[0m creado")


if __name__ == "__main__":

	tiempo_inicio = time.time()

	signal.signal(signal.SIGINT, ctrlc_signal_handler)

	parser = argparse.ArgumentParser(description="# NetMonster es una herramienta de reconocimiento inicial diseñada para automatizar el proceso de descubrimiento y análisis de servicios en máquinas para la práctica de pentesting.\n\n Funcionalidades principales:\n- Escaneo de puertos con Nmap (descubrimiento rápido y análisis detallado).\n- Detección del Sistema Operativo.\n- Identificación de servicios web y análisis con WhatWeb.\n- Automatización del flujo de reconocimiento inicial.")
	parser.add_argument("-i", "--ip", type=str, default="127.0.0.1", help="Dirección IP del objetivo.")

	args = parser.parse_args()

	try:

		print_banner()

		print(f"\033[34;1m[i]\033[0m Escaneando \033[44;1m{args.ip}\033[0m\n")

		ports_string = nmap_enum(args.ip)
		nmap_versions(args.ip, ports_string)

	except Exception as e:

		print("\r\033[31;1m[-]\033[0m Error al ejecutar el nmap")

	analysis_time(tiempo_inicio)