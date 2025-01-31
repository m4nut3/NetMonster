# NetMonster v1.0
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

![Usage](https://private-user-images.githubusercontent.com/171588712/403861601-191ae082-d291-4515-ba8b-3e21dab6f633.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzcwMzA5NzcsIm5iZiI6MTczNzAzMDY3NywicGF0aCI6Ii8xNzE1ODg3MTIvNDAzODYxNjAxLTE5MWFlMDgyLWQyOTEtNDUxNS1iYThiLTNlMjFkYWI2ZjYzMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDExNlQxMjMxMTdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zN2UyOWZiMDhkMzJiMWE2YWE3YWRkYTFiMTgwYmRiMmM1ZjU5OWJlZmNiMDI5ZjlmZTM1MDJjYTZmY2VkZWZjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.zU_DBj4WkLPzdB-bNA7P1XzapE-wMunw7GOhVyJkvTA)

## Ejemplo de uso
![Ejemplo](https://private-user-images.githubusercontent.com/171588712/403860379-2891e571-b81a-4c39-bb53-16c20dfa6e15.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzgzMjM0NjMsIm5iZiI6MTczODMyMzE2MywicGF0aCI6Ii8xNzE1ODg3MTIvNDAzODYwMzc5LTI4OTFlNTcxLWI4MWEtNGMzOS1iYjUzLTE2YzIwZGZhNmUxNS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTMxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEzMVQxMTMyNDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jYzc2NWIxMTE1NTgwMTI5YzM2NTI1YmZhMDEzMjg4NjBlZWM4Y2VjZTNkMzRlNWE0NjYxOGFkOGQzN2VmN2RiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.e2E5oxDG0X-oDusn7YNa2nM4kaJuIqd6wpUbpSbOF6A)
