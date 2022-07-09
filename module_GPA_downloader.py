import pandas as pd
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


from module_utility import grab_GPA
from module_captcha import captcha_url


def GPA_downloader(selenium_driver_path, NTHU_homepage_url, student_ID, password, data_folder_path, grap_GPA_semester_name, grap_GPA_semester_code):
    # Selenium
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_experimental_option('excludeSwitches', ['enable-logging']) # shut up error code triggered by chrome: "Failed to read descriptor from node connection: A device attached to the system is not functioning." 
    s = Service(selenium_driver_path)
    
    while(True):
        # open chrome
        driver = webdriver.Chrome(service= s, options= options)
        # to url
        driver.get(NTHU_homepage_url)
        # enter student_ID and password
        driver.find_element(by=By.NAME, value="account").send_keys(student_ID)
        driver.find_element(by=By.NAME, value="passwd").send_keys(password)
        # captcha
        image_url = driver.find_element(By.XPATH, "//input[@name='passwd2']/following-sibling::img").get_attribute("src")
        captcha_result = captcha_url(6,image_url)
        driver.find_element(By.NAME, "passwd2").send_keys(captcha_result)
        # enter
        driver.find_element(by=By.NAME, value="Submit").click()
        
        
        try:
            WebDriverWait(driver, 1).until(EC.alert_is_present())
            driver.switch_to.alert.accept()
            print("alert(homepage login)-yes")
            driver.close()
            continue
        except TimeoutException:
            print("alert(homepage login)-no")
            break
    
    
    # 切換到修課同學
    driver.switch_to.frame(1)
    driver.find_element(by=By.ID, value="nodeIcon16").click() #課程、成績
    driver.find_element(by=By.ID, value="itemIcon22").click() #全校課程等級制平均值及標準差查詢

    # 切到中間的畫面
    driver.switch_to.parent_frame()
    driver.switch_to.frame(2)

    GPA_110_1=grab_GPA(driver, grap_GPA_semester_name)
    GPA_110_1.to_csv(data_folder_path + 'GPA_downloaded_' + grap_GPA_semester_code + '.csv', index = False)

    
    driver.quit()