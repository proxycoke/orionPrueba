import selenium
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #simula las funciones de teclado
import time #para tener tiempo de rendimiento


#URL
url='https://dev.market.orion.global/es/store/'
path_driver=os.chdir('D:\AUTOMATION\pruebasAutomation')
driver=webdriver.Chrome()
driver.maximize_window()
driver.get(url)

#obteniendo login
login=driver.find_element(By.XPATH,'/html/body/div[1]/div/header/div/div/div/a[1]')
login.click()
time.sleep(5)

#ingreso de usuario y contraseña
usuario=driver.find_element(By.XPATH,'//*[@id=":r0:"]')
usuario.send_keys('cuentademoorionhub@gmail.com')
time.sleep(2)

clave=driver.find_element(By.XPATH,'//*[@id=":r1:"]')
clave.send_keys('12345678Fs')
time.sleep(5)

#darle boton de ingresar
entrar=driver.find_element(By.XPATH,'//*[@id=":r2:"]')
entrar.click()
time.sleep(8)


#Uso de Assertion para validar el login
try:
    elemento_validacion = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/main/div/div[3]/div/table/tbody/tr[1]/td[1]/div')
    assert elemento_validacion.is_displayed(), "busqueda elemento para validar"
    print("ENCONTRADO XPATH DE ELEMENTO POST LOGIN")

except NoSuchElementException:
    print("PROBLEMAS DE LOGIN, NO SE LOGRO INGRESAR")

driver.close()