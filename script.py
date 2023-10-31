from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import csv
import os.path
import time

def formatRGBA(rgbaColor):
	match rgbaColor:
		case 'rgba(241, 44, 76, 1)':
			return 'red'
		case 'rgba(38, 47, 60, 1)':
			return 'black'
		case 'rgba(255, 255, 255, 1)':
			return 'white'
		case _:
			return 'undefined color'

def getIdentifier(element):
	element.click()

	#espera a tela carregar
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "server-roll")))
	identifier = driver.find_element(By.CLASS_NAME, 'server-roll').text
	

	#fecha o modal
	driver.find_element(By.ID, 'parent-modal-close').click()

	return identifier

URL = "https://blaze-4.com/pt/games/double"

driver = webdriver.Chrome()
driver.get(URL)

data = []

filename = './dados.csv'
if(os.path.isfile(filename)):
	csvFile = pd.read_csv(filename)
	numeroTotal = csvFile.shape[0]
else:
	with open(filename, 'w') as csvfile:
		w = csv.DictWriter(csvfile, ['id','identifier','number','color'])
		w.writeheader()

	csvFile = pd.read_csv(filename)
	numeroTotal = csvFile.shape[0]

idAI = numeroTotal


#pra cada quadradinho de resultados
for box in driver.find_elements(By.CLASS_NAME, 'sm-box'):
	color = formatRGBA(box.value_of_css_property('background-color'))
	
	if(color == 'white'):
		number = 0
	elif(color == 'undefined color'):
		continue
	else:
		number = box.find_element(By.CLASS_NAME, 'number').text

	divAberta = box.click()

	#espera a tela carregar
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "server-roll")))
	identifier = driver.find_element(By.CLASS_NAME, 'server-roll').text
	

	#fecha o modal
	driver.find_element(By.ID, 'parent-modal-close').click()

	resultado = {}
	resultado['id'] = idAI
	resultado['identifier'] = identifier
	resultado['number'] = number
	resultado['color'] = color
	data.append(resultado)
	idAI += 1

with open(filename, 'a', newline='') as f:
	w = csv.DictWriter(f,['id','identifier','number','color'])

	for row in data:
		w.writerow(row)


driver.quit()
print("feito!")
