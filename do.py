from selenium import webdriver
from selenium.webdriver.support.ui import Select
from random import randint

def func(username, password):
    driver = webdriver.Chrome('./chromedriver64')
    driver.get('https://erp.lnmiit.ac.in/MIS/default.aspx')
    element = driver.find_element_by_id('txt_username')
    element.send_keys(username)
    ele = driver.find_element_by_id('txt_password')
    ele.send_keys(password)
    driver.find_element_by_id("btnSubmit").click()
    for link in driver.find_elements_by_xpath('//a[@href]'):
        try:
            if 'FeedBack' in link.get_attribute("href"):
                driver.get(link.get_attribute("href"))
                alert = driver.switch_to.alert
                alert.accept()
                select = Select(driver.find_element_by_xpath('//*[@title="Please Select Course"]'))
                for index in range(1, len(select.options)):
                    select = Select(driver.find_element_by_xpath('//*[@title="Please Select Course"]'))
                    select.select_by_index(index)
                    try:
                        driver.switch_to.alert.accept()
                        continue
                    except Exception as e:
                        print(e)
                        pass

                    selectTeach = Select(driver.find_element_by_xpath('//*[@title="Please Select Teacher"]'))
                    for indexes in xrange(1, len(selectTeach.options)):
                        select = Select(driver.find_element_by_xpath('//*[@title="Please Select Course"]'))
                        select.select_by_index(index)
                        selectTeach = Select(driver.find_element_by_xpath('//*[@title="Please Select Teacher"]'))
                        selectTeach.select_by_index(indexes)
                        selectTeach = Select(driver.find_element_by_xpath('//*[@title="Please Select Teacher"]'))
                        total = len(driver.find_elements_by_css_selector("input[type='radio']"))
                        iterations = 0
                        while 5*(iterations + 1) <= total:
                            rand = randint(1, 5) + iterations*5
                            driver.find_elements_by_css_selector("input[type='radio']")[rand - 1].click()
                            iterations += 1
                        driver.find_element_by_xpath('//*[@type="submit"]').click()
                        alert = driver.switch_to.alert
                        alert.accept()
                break
        except Exception as e:
            print e
    driver.quit()
