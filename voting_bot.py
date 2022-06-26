from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

URL         = 'https://europe.triple-e-awards.com/index/finalist/id/521'

for i in range(500):
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(URL)
        driver.find_element_by_name('Email').send_keys('fedeelozanomalaga+' + str(i) + '@gmail.com\n')
        time.sleep(3)
        driver.quit()
        print('Voted, i = ' + str(i))

    except:
        print('Connection refused, i = ', str(i))
    time.sleep(3)