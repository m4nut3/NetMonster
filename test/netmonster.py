
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
# python3 netmonster.py -i <ip>                                                #
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
import os


# Colores de Terminal

NORMAL="\033[0m"
RED="\033[31;1m"
GREEN="\033[32;1m"
BLUE="\033[34;1m"
ORANGE="\033[33;1m"
WHITE_BACK_GREEN="\033[42;1m"
WHITE_BACK_BLUE="\033[44;1m"

def print_banner():

#	Nombre de la función:
#    	[print_banner]

#	Descripción:
#    	[Función para la impresión del banner de la herramienta NetMonster]

	print("\n ███▄    █ ▓█████▄▄▄█████▓ ███▄ ▄███▓ ▒█████   ███▄    █   ██████ ▄▄▄█████▓▓█████  ██▀███  \n ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒▓██▒▀█▀ ██▒▒██▒  ██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒\n▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░▓██    ▓██░▒██░  ██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒\n▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ ▒██    ▒██ ▒██   ██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  \n▒██░   ▓██░░▒████▒ ▒██▒ ░ ▒██▒   ░██▒░ ████▓▒░▒██░   ▓██░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒\n░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░\n░ ░░   ░ ▒░ ░ ░  ░   ░    ░  ░      ░  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░\n   ░   ░ ░    ░    ░      ░      ░   ░ ░ ░ ▒     ░   ░ ░ ░  ░  ░    ░         ░     ░░   ░ \n         ░    ░  ░               ░       ░ ░           ░       ░              ░  ░   ░     \n")
	print(f"\nHerramienta de reconocimiento inicial\n")


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

	print(f"\n{BLUE}[i]{NORMAL} Análisis completado en {minutos} minuto/s y {segundos} segundo/s")


def web_analyze(target, port):

#	Nombre de la función:
#    	[web_analyze]

#	Descripción:
#    	[Función para el análisis en profundidad de los servicios web detectados con la herramienta WhatWeb.]
	
	service = "http"

	if port[1]:
		service = "https"

	whatweb_result = subprocess.run(["whatweb", f"{service}://{target}:{port[0]}"], capture_output=True, text=True)

	print(f"{GREEN}[+] {NORMAL}Lanzando un whatweb {service}://{target}:{port[0]} ...")
	print(f"\n{whatweb_result.stdout}")


def nmap_enum(target):

#	Nombre de la función:
#    	[nmap_enum]

#	Descripción:
#    	[Enumeración de puertos y el Sistema Operativo del sistema. Crea un fichero "nmap_enum" con el output del nmap utilizado.]

	ports_string = ""
	http_ports = []

	nmap_enum = subprocess.run([f"nmap", "--open", "-sS", "-O", "--osscan-guess", "-p-", "--min-rate", "4000", "-Pn", "-n", target, "-oN", "nmap_enum"], capture_output=True, text=True)


	ports_results = re.findall(r"(\d+)/(tcp|udp)\s+(open)(.*)", nmap_enum.stdout)

	try:
		so_results_list = re.findall(r"Aggressive OS guesses:\s+(.*?)\,|OS details:\s+(.*?)\n", nmap_enum.stdout)

		if so_results_list[0][0]:
			so_results = so_results_list[0][0]

		else:
			so_results = so_results_list[0][1]

		print(f"{GREEN}[+] {NORMAL}Sistema Operativo detectado: {GREEN}{so_results}{NORMAL}")

	except Exception as e:

		print(f"\r{RED}[-]{NORMAL} No se ha podido determinar el Sistema Operativo")

	print(f"{GREEN}[+] {NORMAL}Puertos encontrados:", end=" ")

	for coincidencias in ports_results:

		if "https" in coincidencias[3]:
			http_ports.append((coincidencias[0], True))

		elif "http" in coincidencias[3]:
			http_ports.append((coincidencias[0], False))

		print(f"{GREEN}{coincidencias[0]}{NORMAL}", end="")
		ports_string = ports_string + coincidencias[0]

		if len(ports_results) > ports_results.index(coincidencias)+1:
			print(f"{GREEN}, {NORMAL}", end="")
			ports_string = ports_string + ","

	print(f"\n{GREEN}[+] {NORMAL}Fichero {GREEN}nmap_enum{NORMAL} creado")
	
	try:
		if http_ports:

			response = subprocess.run([f"curl -v http://{target}:{http_ports[0][0]} 2>&1"], capture_output=True, text=True, shell=True, check=True)
			matches = re.findall(r"Location: http://([^/]+)", response.stdout)

			if matches:

				domain = matches[0]

				try:
					add_host_elecction = input(f"Parece que se está aplicando virtual host, ¿quieres añadir el dominio {domain} a /etc/hosts? [Y/N]")

					if add_host_elecction.lower() == 'y':
						subprocess.run([f"echo '{target} {domain}\' >> /etc/hosts"], shell=True, check=True)
						print(f"{GREEN}[+] {NORMAL}{domain} añadido correctamente al /etc/hosts")
						target = domain
			
				except Exception as e:
					
					print(f"\r{RED}[-]{NORMAL} Error al añadir {domain} al /etc/hosts")
					
	except Exception as e:
		
		print(f"\r{RED}[-]{NORMAL} Error al identificar el dominio")


	try:

		print(f"{GREEN}[+] {NORMAL}Puertos con servicios web detectados: {len(http_ports)}\n")

		for ports in http_ports:
			
			web_analyze(target, ports)

	except Exception as e:
		
		print(f"\r{RED}[-]{NORMAL} Error al ejecutar whatweb")

	nmap_versions(target, ports_string)


def nmap_versions(target, ports_string):

#	Nombre de la función:
#    	[nmap_versions]

#	Descripción:
#    	[Función para el análisis en profundidad de los puertos enumerados previamente. Crea un fichero "nmap_versions" con el output del nmap utilizado.]

	subprocess.run(["nmap", "-sCV", f"-p{ports_string}", "-n", "-Pn", "-T5", target, "-oN", "nmap_versions"], capture_output=True, text=True)
	print(f"{GREEN}[+] {NORMAL}Fichero {GREEN}nmap_versions{NORMAL} creado")


if __name__ == "__main__":

	if os.getuid() == 0:

		tiempo_inicio = time.time()

		signal.signal(signal.SIGINT, ctrlc_signal_handler)

		parser = argparse.ArgumentParser(description="# NetMonster es una herramienta de reconocimiento inicial diseñada para automatizar el proceso de descubrimiento y análisis de servicios en máquinas para la práctica de pentesting.\n\n Funcionalidades principales:\n- Escaneo de puertos con Nmap (descubrimiento rápido y análisis detallado).\n- Detección del Sistema Operativo.\n- Identificación de servicios web y análisis con WhatWeb.\n- Automatización del flujo de reconocimiento inicial.")
		parser.add_argument("-i", "--ip", type=str, default="127.0.0.1", help="Dirección IP del objetivo.")

		args = parser.parse_args()

		try:

			target = args.ip

			print_banner()

			print(f"{BLUE}[i]{NORMAL} Escaneando {WHITE_BACK_BLUE}{target}{NORMAL}\n")

			ports_string = nmap_enum(target)

		except Exception as e:

			print(f"\r{RED}[-]{NORMAL} Error al ejecutar el nmap")
			print(e)

		analysis_time(tiempo_inicio)

	else:

		print(f"\n{RED}[!]{NORMAL} Ejecutar la herramienta como root\n")