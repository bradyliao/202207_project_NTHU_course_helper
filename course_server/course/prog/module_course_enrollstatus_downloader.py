# only copy paste from curriculum part

from os import spawnlp
import pandas as pd
from time import sleep
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


from module_utility import to_df
from module_captcha import captcha_url

def course_enrollstatus_downloader(selenium_driver_path, NTHU_homepage_url, global_semester, student_ID, password, data_folder_path):
    
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " course_enrollstatus_downloader - start")
    
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
        # # captcha
        image_url = driver.find_element(By.XPATH, "//input[@name='passwd2']/following-sibling::img").get_attribute("src")
        captcha_result = captcha_url(6,image_url)
        driver.find_element(By.NAME, "passwd2").send_keys(captcha_result)
        
        # enter
        driver.find_element(by=By.NAME, value="Submit").click()
        
        
        try:
            WebDriverWait(driver, 1).until(EC.alert_is_present())
            driver.switch_to.alert.accept()
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " course enrollstatus - login - fail")
            driver.close()
            continue
        except TimeoutException:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " course enrollstatus - login - success")
            break
    

    
    # 切換到修課同學
    driver.switch_to.frame(1)
    driver.find_element(by=By.ID, value="nodeIcon55").click() # 選課
    driver.find_element(by=By.ID, value="nodeIcon62").click() # 報表
    driver.find_element(by=By.ID, value="itemIcon63").click() # 選上/剩餘名額/待亂數人數統計

    # 切到中間的畫面
    driver.switch_to.parent_frame()
    driver.switch_to.frame(2)

    # get drop down menu length
    dropdownlist_len = len( Select(driver.find_element(by=By.NAME, value="select")).options )
    
    
    course_enrollstatus_df = pd.DataFrame()
    
    
    i = 1
    while i < dropdownlist_len:
        Select(driver.find_element(by=By.NAME, value="select")).select_by_index(i)
        # enter
        driver.find_element(by=By.NAME, value="Submit").click()
        
        # load data to dataframe
        course_enrollstatus_df_incoming = to_df(driver=driver)
        
        # combine current & incoming dataframe
        course_enrollstatus_df = pd.concat([course_enrollstatus_df, course_enrollstatus_df_incoming], ignore_index=True, sort=False)
            
        # back
        driver.find_element(by=By.XPATH, value="/html/body/div/form/input[3]").click()
        
        i += 1
    
    
    driver.quit()
    
    
    
    # drop 必選修說明 row
    row_to_drop = []
    for row in range(0, len(course_enrollstatus_df)):
        if course_enrollstatus_df.loc[row][4]  == None or course_enrollstatus_df.loc[row][0] == "科號Course Number":
            row_to_drop.append(row)
        
    course_enrollstatus_df = course_enrollstatus_df.drop(index=row_to_drop)
    
    
    
    course_enrollstatus_df.to_csv(data_folder_path + global_semester + '_course_enrollstatus_downloaded.csv', index = False)
    course_enrollstatus_df.to_csv(data_folder_path + 'log/' + datetime.datetime.now().strftime("%Y%m%d_%H%M%S_") + global_semester + '_course_enrollstatus_downloaded.csv', index = False)
    
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " course_enrollstatus_downloader - done")
    
    
    
    
    
    
    
    
    
    
    
    