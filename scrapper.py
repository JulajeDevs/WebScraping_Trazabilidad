from selenium import webdriver 
from selenium.webdriver import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.common.exceptions import TimeoutException
import time 


user = {
    "username": "BOTCONSULTACMVS",
    "password": "Traza.2025"
}

def safe_wait(driver, condition, timeout=20, action_desc="acción"):
    """Espera segura con manejo de excepciones"""
    try:
        return Wait(driver, timeout).until(condition)
    except TimeoutException:
        print(f"[ERROR] Tiempo de espera agotado al intentar {action_desc}.")
    except Exception as e:
        print(f"[ERROR] Ocurrió un problema en {action_desc}: {e}")
    return None

def iniciar_driver(): 
    service = Service(ChromeDriverManager().install())
    options = chrome.options.Options()
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(service=service, options=options)
    
    try:  
        print("Navegando a TRAZABILIDAD...")
        driver.get("https://trazabilidad.esculapiosis.com/Account/Login?ReturnUrl=%2F")
        return driver
    except Exception as e: 
        print(f"No se pudo cargar la pagina: {e}")
        return None

def login(driver, data): 
    try:
        # Campo de usuario/email
        userInput = safe_wait(driver, EC.element_to_be_clickable((By.ID, "Email")), action_desc="encontrar campo de usuario")
        userInput.clear()
        userInput.send_keys(data["username"])
        
        # Campo de contraseña
        passInput = safe_wait(driver, EC.element_to_be_clickable((By.ID, "Password")), action_desc="encontrar campo de contraseña")
        passInput.clear()
        passInput.send_keys(data["password"])
        
        # Hacer click en el botón de Login
        login_button = safe_wait(driver, EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(), 'Login')]")), action_desc="encontrar botón de login")
        login_button.click()
        
        # Esperar a que la página cargue después del login
        time.sleep(2)
        
        # Verificar si el login fue exitoso (puedes ajustar esta verificación)
        if "login" not in driver.current_url.lower():
            print("Login exitoso")
            return True
        else:
            print("Posible fallo en el login")
            return False
            
    except Exception as e:
        print(f"Error durante el login: {e}")
        return False

def navegar_ips(driver):
     empresa_link = safe_wait(driver, EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href, '/Empresas/Seleccionada?empresa=TO')]")
        ), action_desc="encontrar enlace de empresa")
     empresa_link.click()
     
     time.sleep(3)
     
     opcTrazabilidad = safe_wait(driver, EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="idBodyPage"]/div[1]/div/div[2]/ul/li[1]/a')
        ), action_desc="encontrar enlace de opciones")
     opcTrazabilidad.click()
     
     time.sleep(3)
     
     gestionarCaso = safe_wait(driver, EC.element_to_be_clickable((By.XPATH, '//*[@id="idBodyPage"]/div[1]/div/div[2]/ul/li[1]/ul/li[1]/a')
        ), action_desc="encontrar enlace de busqueda de casos")
     gestionarCaso.click()
     

def consultar_informacion(driver):
    
    NoCasoInput = safe_wait(driver, EC.element_to_be_clickable((By.ID, "NoCaso")), action_desc="encontrar campo de No. Caso")
    NoCasoInput.clear()
    NoCasoInput.send_keys("52874")
    
    BuscarCaso = safe_wait(driver, EC.element_to_be_clickable((By.XPATH, '//*[@id="divCaso"]/form/div/div[2]/button/span')), action_desc="encontrar botón de buscar caso")
    BuscarCaso.click()

def automatizar_proceso():
    driver = iniciar_driver()
    if driver is None:
        return
    login(driver,user)
    navegar_ips(driver)
    consultar_informacion(driver)
    time.sleep(12)
    
    
    driver.quit()    
    

def main():
    print("Iniciando proceso...")
    automatizar_proceso()

if __name__ == "__main__":
    main()