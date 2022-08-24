from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

ser = Service('C:\Program Files (x86)\chromedriver.exe')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://arithmetic.zetamac.com/")

i = 0

e = 0


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="welcome"]/form/input'))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'problem'))
    )
    eq = element.text


    equation = eq.split(' ')
    operator = equation.pop(1)
    rop = ''

    if operator == '–':
        rop = '-'
    if operator == '+':
        rop = '+'
    if operator == '÷':
        rop = '/'
    if operator == '×':
        rop = '*'

    equation.insert(1, rop)

    ev = ' '.join(equation)

except:
    pass

def main():
    eq = ""
    ev = ''
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'problem'))
        )
        eq = element.text

        #Takes out the current operator
        equation = eq.split(' ')
        operator = equation.pop(1)
        rop = ''
        #Switches the operator to an operator python can use
        if operator == '–':
            rop = '-'
        if operator == '+':
            rop = '+'
        if operator == '÷':
            rop = '/'
        if operator == '×':
            rop = '*'
        #Inserts an operator python can use
        equation.insert(1, rop)
        
        ev = ' '.join(equation)
    except:
        pass
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="game"]/div/div[1]/input'))
        )
        element.clear()
        element.send_keys(eval(ev))
    except:
        pass

while i < 10000000:
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'left'))
        )
        if element.text == "Seconds left: 0":
            e = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'correct'))
        )
            print(f"""
            ****************************\n
                     {e.text}\n
            ****************************
            """)
            driver.quit()
            break
    except:
        break
    main()
    i += 1
