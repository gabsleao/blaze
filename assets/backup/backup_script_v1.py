from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv 

URL = "https://blaze-4.com/pt/games/double"

driver = webdriver.Chrome()

driver.get(URL)

datas = [] # a list to store quotes

# entries = driver.find_element(By.CLASS_NAME,'entries.main')
# print(entries)


for box in driver.find_elements(By.CLASS_NAME, 'sm-box'):
	rgbaColor = box.value_of_css_property('background-color')
	if(rgbaColor == 'rgba(241, 44, 76, 1)'):
		color = 'red'
	elif(rgbaColor == 'rgba(38, 47, 60, 1)'):
		color = 'black'
	elif(rgbaColor == 'rgba(255, 255, 255, 1)'):
		color = 'white'
	else:
		continue

	if box.find_element(By.CLASS_NAME, 'number').text is None:
		continue
	else:
		number= box.find_element(By.CLASS_NAME, 'number').text

	print(color + ' - ' + number)
	# for row in box.find_elements(By.CLASS_NAME, 'number'):
	# 	print(color + ' - ' + row.text)

	# data = {} 
	# data['numero'] = row.text 
	# data['cor'] = row.a['href'] 
	# data['data_add'] = row.img['src'] 
	# data['lines'] = row.img['alt'].split(" #")[0] 
	# data['author'] = row.img['alt'].split(" #")[1] 
	# datas.append(data) 

# filename = 'dados.csv'
# with open(filename, 'w', newline='') as f: 
# 	w = csv.DictWriter(f,['theme','url','img','lines','author']) 
# 	w.writeheader() 
# 	for data in datas: 
# 		w.writerow(data) 

driver.quit()
print("feito!")
