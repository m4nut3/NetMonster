# NetMonster v1.1

![Logo](https://github.com/m4nut3/NetMonster/blob/main/images/Logo.png)

NetMonster es una herramienta de reconocimiento inicial diseñada automatizar el proceso de descubrimiento y análisis de servicios en máquinas para la práctica de pentesting.

Instalaciones necesarias:
```shell
sudo apt-get update
sudo apt-get install nmap whatweb
```

Nmap y WhatWeb son dos herramientas de reconocimiento que se van a ejecutar para automatizar el análisis de la información en red que necesitamos.

Descarga de NetMonster:
```shell
git clone https://github.com/m4nut3/NetMonster
cd NetMonster
sudo python3 netmonster.py
```

# Consideraciones previas

- Es necesario que la herramienta se ejecute como root ya que nmap utiliza el modo sigiloso -sS y esto requiere privilegios de root.
- La detección de servicios web todavía es algo imprecisa ya que solo detecta los puertos comúnmente usados para este tipo de servicios.

## Uso

![Usage](https://github.com/m4nut3/NetMonster/blob/main/images/Usage.png)
## Ejemplo de uso
![Ejemplo](https://github.com/m4nut3/NetMonster/blob/main/images/Example.png)
