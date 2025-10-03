from selenium import webdriver 
from selenium.webdriver import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.common.exceptions import TimeoutException
import time 

#TODO 
"""
1. Realizar Login 
2. Navegar para cada una de las IPS
3. Especifiar el paso siguiente con CMVS 
4. Consultar la información de los números de casos
5. Descargar los ZIP 
6. Descomprimir los ZIP y guardar la información en una carpeta renombrados
7. Subir estos archivos al drive con la siguiente estructura 

## Estructura de carpeta drive
Nombre: 1111478831 - KEVIN [
    IPS1 :
        - archivo1.csv
        - archivo2.csv
    IPS2 :
        - archivo1.csv
        - archivo2.csv
    ETC....
]
"""

def iniciar_driver(): 
    print("Iniciando driver...")
    
def login(driver): 
    print("Realizando login...")
    
def navegar_ips(driver):
    print("Navegando por las IPS...")
    
def consultar_informacion(driver):
    print("Consultando información...")
    
def automatizar_proceso(driver):
    driver = iniciar_driver()
    login(driver)
    navegar_ips(driver)
    consultar_informacion(driver)

def main():
    print("Iniciando proceso...")
    automatizar_proceso()


if __name__ == "__main__":
    print("test")