from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint


chromedriver_path = 'F:\setups\chromedriver_win32/chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
#webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
webdriver.get('https://www.instagram.com')
webdriver.maximize_window()
#sleep(3)

#username = webdriver.find_element_by_name('username')
#username.send_keys('')
#password = webdriver.find_element_by_name('password')
#password.send_keys('your_password')

#button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > button')
#button_login.click()
#sleep(3)

temp = input('Logged in?')

#webdriver.get('https://www.instagram.com/anurag3.4')


difference = []


j = 1
for i in difference:
    webdriver.get('https://www.instagram.com/'+i)
    sleep(randint(4,10))

    try:
        confirmButton = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button')
        confirmButton.click()
        sleep(randint(2,5))
        confirmButton = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]')
        confirmButton.click()
        print(j,'Unfollowed: ',i)

    except:
        print('error',i)
    
    j+=1
    
    if j%100 == 0:
        temp = input('Unfollowed count=',j,' Continue?')
    
    elif j%17 == 0:
        print('Unfollowed count',j)
        sleep(randint(3602,3610))
    else:
        sleep(randint(4,8))

print('Unfollowed All :)')
