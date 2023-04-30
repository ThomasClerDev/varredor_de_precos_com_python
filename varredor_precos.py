from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://sitepreco1.netlify.app/')
sleep(5)
precos_site_1 = driver.find_elements(By.XPATH,'//h6[@class="price_heading"]')
sleep(2)
preco_final_site_1 = precos_site_1[3].text.split(' ')[1]

driver.get('https://sitepreco2.netlify.app/')
sleep(5)
precos_site_2 = driver.find_elements(By.XPATH,"//h5")
sleep(2)
preco_final_site_2 = precos_site_2[3].text.split('$')[1]
print('test')

driver.get('https://sitepreco3.netlify.app/')
sleep(5)
precos_site_3 = driver.find_elements(By.XPATH,'//div[@class="featured__item__text"]//h5')
sleep(2)
preco_final_site_3 = precos_site_3[2].text.split('$')[1]

with open('precos.csv','w',newline='',encoding='utf-8') as arquivo:
    arquivo.write(f'site,preço{os.linesep}')
    arquivo.write(f'https://sitepreco1.netlify.app/,{preco_final_site_1}{os.linesep}')
    arquivo.write(f'https://sitepreco2.netlify.app/,{preco_final_site_2}{os.linesep}')
    arquivo.write(f'https://sitepreco3.netlify.app/,{preco_final_site_3}{os.linesep}')