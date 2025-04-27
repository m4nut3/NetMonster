

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
# python3 main.py -i <ip>                                                      #
#                                                                              #
# Autor: manut3                                                                #
# Fecha de creación: 14/01/2025                                                #
# Versión: 1.1                                                                 #
#                                                                              #
# Nota: Por favor, usa esta herramienta únicamente en entornos controlados y   #
# con autorización explícita. El autor no se hace responsable del uso indebido #
# de la herramienta.                                                           #
################################################################################

import argparse
import signal
import os
import time

from lib.utils import print_banner, ctrlc_signal_handler, analysis_time
from lib.analysis import nmap_enum
from lib.colors import NORMAL, RED, GREEN, BLUE, ORANGE, WHITE_BACK_GREEN, WHITE_BACK_BLUE


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