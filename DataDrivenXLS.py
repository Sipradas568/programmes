from selenium import webdriver
from selenium.webdriver.common.by import By
import utils
import time
driver = webdriver.Chrome()
driver.get("https://www.calculator.net/percent-calculator.html")
driver.maximize_window()
web_el = driver.find_element(By.XPATH, "//form[@name = 'calform3']")
ele = utils.scroll_ele(driver,web_el)
#driver.execute_script("arguments[0].scrollIntoView();" , ele )
time.sleep(2)
file = r"C:\Users\10744603\OneDrive - LTIMindtree\Documents\openpyxl.xlsx"
rows = utils.row_count(file,"Sheet1")
print(rows)
cols = utils.col_count(file,"Sheet1")
print(cols)

for r in range(2,rows+1):
        
                value1 = utils.read_data(file,"Sheet1",r,1)
                value2 = utils.read_data(file,"Sheet1",r,2)
                exp_val = utils.read_data(file,"Sheet1",r,3)
                
                driver.find_element(By.XPATH, "//input[@name = 'c3par1']").send_keys(value1)
                time.sleep(2)
                driver.find_element(By.XPATH, "//input[@name = 'c3par2']").send_keys(value2)
                time.sleep(2)
                driver.find_element(By.XPATH, "//form[@name = 'calform3']//input[@type = 'submit']").click()
                res = driver.find_element(By.XPATH,"//div[@id = 'content']//table[2]//tr[4]/td[2]").text.replace('%','').strip()
                print("result in:" ,res)
                print(type(res))
                print(type(exp_val))
                print("in sheet:", exp_val)
                if float(exp_val) == float(res):
                        print("Pass")
                else:
                        print("Fail")
                driver.find_element(By.XPATH,"//td[@colspan = '2']//input[@value= 'Clear']").click()
                


            


