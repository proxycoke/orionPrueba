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
time.sleep(3)

#ingreso de usuario y contraseña
usuario=driver.find_element(By.XPATH,'//*[@id=":r0:"]')
usuario.send_keys('cuentademoorionhub@gmail.com')
time.sleep(2)

clave=driver.find_element(By.XPATH,'//*[@id=":r1:"]')
clave.send_keys('12345678Fs')
time.sleep(2)

#darle boton de ingresar
entrar=driver.find_element(By.XPATH,'//*[@id=":r2:"]')
entrar.click()
time.sleep(5)

#Agregar Producto
producto1=driver.find_element(By.XPATH,'//html/body/div[1]/div/div[1]/main/div/div[3]/div/table/tbody/tr[1]/td[1]/div/div[2]/span[1]')
producto1.click()
time.sleep(2)

licencia1=driver.find_element(By.XPATH,'//html/body/div[1]/div/div[1]/main/div/div[2]/div[2]/button')
licencia1.click()
time.sleep(2)


#Aumentar el producto en 1 con el boton de adicionar
AgregarContador= driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium mui-mjh5v']//span[@class='MuiBox-root mui-vxcmzt']")
botonAumenta = AgregarContador.find_element(By.XPATH, "./parent::button")
botonAumenta.click()
time.sleep(2)

#Acepta Documentación Respaldo
elemento_interno = driver.find_element(By.XPATH, "//span[@class='MuiButtonBase-root MuiRadio-root MuiRadio-colorPrimary MuiRadio-sizeSmall PrivateSwitchBase-root MuiRadio-root MuiRadio-colorPrimary MuiRadio-sizeSmall MuiRadio-root MuiRadio-colorPrimary MuiRadio-sizeSmall mui-lutibj']//input[@class='PrivateSwitchBase-input mui-j8yymo']")
bolita = elemento_interno.find_element(By.XPATH, "./parent::span")
bolita.click()
time.sleep(3)

#Agregar Producto al Carro
agragarCarro1 = driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-disableElevation MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-disableElevation mui-1v8i4st']//span[@class='MuiLoadingButton-label mui-jv36sd']")
agregando = agragarCarro1.find_element(By.XPATH, "./parent::button")
agregando.click()
time.sleep(3)

regresaAcomprar = driver.find_element(By.XPATH, "//*[@class='MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButton-outlinedInherit MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-colorInherit MuiButton-disableElevation MuiButton-root MuiButton-outlined MuiButton-outlinedInherit MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-colorInherit MuiButton-disableElevation mui-bna05u']")
regresaAcomprar.click()
time.sleep(3)

#Agregar Segundo producto
#regresar a Suscripciones
suscripciones=driver.find_element(By.XPATH,"//*[@id='nav-section-horizontal']/a[2]")
suscripciones.click()
time.sleep(3)

producto2=driver.find_element(By.XPATH,'//html/body/div[1]/div/div[1]/main/div/div[3]/div/table/tbody/tr[3]/td[1]/div/div[2]/span[1]')
producto2.click()
time.sleep(2)

licencia2=driver.find_element(By.XPATH,'//html/body/div[1]/div/div[1]/main/div/div[2]/div[2]/button')
licencia2.click()
time.sleep(2)


#Aumentar el producto en 1 con el boton de adicionar
AgregarContador= driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium mui-mjh5v']//span[@class='MuiBox-root mui-vxcmzt']")
botonAumenta = AgregarContador.find_element(By.XPATH, "./parent::button")
botonAumenta.click()
time.sleep(2)

#Acepta Documentación Respaldo
elemento_interno = driver.find_element(By.XPATH, "//span[@class='MuiButtonBase-root MuiRadio-root MuiRadio-colorPrimary MuiRadio-sizeSmall PrivateSwitchBase-root MuiRadio-root MuiRadio-colorPrimary MuiRadio-sizeSmall MuiRadio-root MuiRadio-colorPrimary MuiRadio-sizeSmall mui-lutibj']//input[@class='PrivateSwitchBase-input mui-j8yymo']")
bolita = elemento_interno.find_element(By.XPATH, "./parent::span")
bolita.click()
time.sleep(3)

#Agregar Producto al Carro
agragarCarro1 = driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-disableElevation MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-disableElevation mui-1v8i4st']//span[@class='MuiLoadingButton-label mui-jv36sd']")
agregando = agragarCarro1.find_element(By.XPATH, "./parent::button")
agregando.click()
time.sleep(3)

regresaAcomprar = driver.find_element(By.XPATH, "//*[@class='MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButton-outlinedInherit MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-colorInherit MuiButton-disableElevation MuiButton-root MuiButton-outlined MuiButton-outlinedInherit MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-colorInherit MuiButton-disableElevation mui-bna05u']")
regresaAcomprar.click()
time.sleep(3)

driver.close()