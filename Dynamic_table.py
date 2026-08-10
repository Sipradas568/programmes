from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://datatables.net/")  

rows = driver.find_elements(By.XPATH,"//table[@id = 'example']//tbody/tr")
print(len(rows))
cols = driver.find_elements(By.XPATH,"//table[@id = 'example']//tbody/tr/td")
print(len(cols))
for i in range (1,len(rows)+1):
    val = driver.find_element(By.XPATH,f"//table[@id = 'example']//tbody/tr[{i}]/td").text
   
    if val == "Airi Satou":
        for j in range(1,len(cols)+1):
            
                print(driver.find_element(By.XPATH,f"//table[@id = 'example']//tbody/tr[{i}]/td[{j}]").text)
                
        
           

        


    
