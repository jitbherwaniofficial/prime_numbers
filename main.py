from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import os
import time
from dotenv import load_dotenv
load_dotenv()

driver = webdriver.Chrome(executable_path=os.environ['CHROME_DRIVER_PATH'])


url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"

driver.get(url)
driver.maximize_window()

quest_links = driver.find_elements_by_xpath('//*[@id="table_id"]/tbody/tr[1]/td[2]/a/b')

for quest_link in quest_links:
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(quest_link).key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[-1])
    print(driver.window_handles)
    quest_number = driver.find_element_by_xpath('//*[@id="view-bid-posting"]/div[2]/div[2]/div/h4/span/b').text.split(' ')[2]
    closing_date = driver.find_element_by_xpath('//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[1]/td[2]').text
    est_value_notes = driver.find_element_by_xpath('//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[3]/td[2]').text
    description = driver.find_element_by_xpath('//*[@id="current_project"]/div/div[3]/div/table/tbody/tr[3]/td[2]').text
    print(f"Quest Number: {quest_number}\nEst. Value notes: {est_value_notes}\nDescription: {description}\nClosing Date: {closing_date}\n\n\n")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    


