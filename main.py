#Import all moduals
import random
import string
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




#Create The "driver" fonction For The chromedriver.exe
driver = webdriver.Chrome('./chromedriver.exe')




#Get The Uppercase/Digits From The String Modual
uc = string.ascii_uppercase
dg = string.digits


#Open Chrome with Selenium, Login with Microsoft Then Go To The Main Code-Redeem Page
driver.get("https://www.minecraft.net/en-us/login")
time.sleep(7)
os.system('cls')
int(input("Login With Microsoft Then Press '1' When You Finish: "))
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div/div/nav/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/main/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/a").click()
time.sleep(2)


#infinit Loop
def loop():






    #first = 5x5  "Create a 5x5 string code"
    def first():
        one = "".join(random.choice(uc + dg)for a in range(5))
        two = "".join(random.choice(uc + dg)for a in range(5))
        three = "".join(random.choice(uc + dg)for a in range(5))
        four = "".join(random.choice(uc + dg)for a in range(5))
        five = "".join(random.choice(uc + dg)for a in range(5))

        final = "-".join([one, two, three, four, five])
        print(final)
        enter_code = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[1]/main/div/div/div/div/div[2]/div/div/div/form/div/div[1]/div/input")
        enter_code.send_keys(Keys.CONTROL + 'a')
        enter_code.send_keys(final)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[1]/main/div/div/div/div/div[2]/div/div/div/form/div/div[2]/button").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[1]/main/div/div/div/div/div[2]/div/div/div/form/div/div[1]/div/input").click()
        loop()












    #second = V-5x5     "Create a 5x5 string code with 'V-' in the begining"
    def second():
        one = "".join(random.choice(uc + dg)for a in range(5))
        two = "".join(random.choice(uc + dg)for a in range(5))
        three = "".join(random.choice(uc + dg)for a in range(5))
        four = "".join(random.choice(uc + dg)for a in range(5))
        five = "".join(random.choice(uc + dg)for a in range(5))

        final = "-".join(["V", one, two, three, four, five])
        print(final)
        enter_code = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[1]/main/div/div/div/div/div[2]/div/div/div/form/div/div[1]/div/input")
        enter_code.send_keys(Keys.CONTROL + 'a')
        enter_code.send_keys(final)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[1]/main/div/div/div/div/div[2]/div/div/div/form/div/div[2]/button").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[1]/main/div/div/div/div/div[2]/div/div/div/form/div/div[1]/div/input").click()
        loop()









    #third = digits   "Create a 10 digits String"
    def third():
        final = "".join(random.choice(dg)for a in range(10))
        print(final)
        enter_code = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[1]/main/div/div/div/div/div[2]/div/div/div/form/div/div[1]/div/input")
        enter_code.send_keys(Keys.CONTROL + 'a')
        enter_code.send_keys(final)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[1]/main/div/div/div/div/div[2]/div/div/div/form/div/div[2]/button").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[1]/main/div/div/div/div/div[2]/div/div/div/form/div/div[1]/div/input").click()
        loop()






    #Choose Which Code To Use
    q = random.randint(1, 3)

    if q == 1:
        
        #Use The 5x5 String Code
        first()
    elif q == 2:

        #Use The 5x5 String Code With The 'V-'
        second()
    else:

        #Use The 10 Digits String
        third()


#Call The Loop
loop()