
import sys
import time

from lib.colors import NORMAL, RED, GREEN, BLUE, ORANGE, WHITE_BACK_GREEN, WHITE_BACK_BLUE


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
