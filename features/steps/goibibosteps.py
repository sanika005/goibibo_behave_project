from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import logging
import os

is_exists = os.path.exists('report')
if not is_exists:
    os.makedirs('report')

logger = logging.getLogger()
fh = logging.FileHandler('./report/Log.log')
logger.addHandler(fh)

price_list = []


@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="/Users/apple/Desktop/Sanika/Drivers/chromedriver.exe")

@when('Open goibibo website')
def openHomepage(context):
    context.driver.get("https://www.goibibo.com/flights/")


@then('search flight from mumbai to delhi')
def searchFlight(context):
    context.driver.find_element(By.XPATH,'//span[text()="From"]/following-sibling::p').click()
    context.driver.find_element(By.XPATH,'//span[text()="From"]/following-sibling::input').send_keys("Mumbai(BOM)")
    sleep(2)
    context.driver.find_element(By.XPATH,'//*[@id="autoSuggest-list"]/li[1]/div').click()
    context.driver.find_element(By.XPATH,'//span[text()="To"]/following-sibling::input').send_keys("New Delhi (DEL)")
    sleep(2)
    context.driver.find_element(By.XPATH,'//*[@id="autoSuggest-list"]/li[1]/div').click()
    sleep(2)
    context.driver.find_element(By.XPATH,'//span[text()="Done"]').click()
    sleep(2)
    context.driver.find_element(By.XPATH,'//span[text()="SEARCH FLIGHTS"]').click()
    sleep(1)
    
    sleep(5)
    #Page is not loading after 5 sec
    Price = context.driver.find_elements(By.XPATH,'//button[contains(text(),"VIEW FARES")]/parent::div/parent::div/parent::div/div/div/div/text()')
    for i in Price:
        i.replace(',','')
        price_list.append(int(i))

    for j in range(0,len(price_list)):
        if price_list[j+1] < len(price_list):
            if price_list[j]>price_list[j+1]:
                assert False