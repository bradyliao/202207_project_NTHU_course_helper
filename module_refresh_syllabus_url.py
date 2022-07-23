
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


from module_captcha import captcha_file

def refresh_syllabus_url(curriculum_semester_option, curriculum_url, selenium_driver_path):
    
    # Selenium
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_experimental_option('excludeSwitches', ['enable-logging']) # shut up error code triggered by chrome: "Failed to read descriptor from node connection: A device attached to the system is not functioning." 
    s = Service(selenium_driver_path)
    

    
    
    while True:
        # open chrome
        driver = webdriver.Chrome(service= s, options= options)
        # to url
        driver.get(curriculum_url)
        # select semester
        Select(driver.find_element(by=By.ID, value="YS_id")).select_by_visible_text(curriculum_semester_option)
        # click first option ( 僅列出所選開課代號之科目(only courses offered by this department) )
        driver.find_element(by=By.NAME, value="cond").click()
        # choose i th option in the drop down menu
        Select(driver.find_element(by=By.NAME, value="cou_code")).select_by_visible_text('CS 　資工系 Computer Science')
        
        
        
        
        
        # captcha
        
        # screenshot -> it will be the same from the website
        image_location = driver.find_element(By.XPATH, "/html/body/div/form/table[2]/tbody/tr/td/img")
        with open('image_screenshot.png', 'wb') as file:
            file.write(image_location.screenshot_as_png)
        
        captcha_result = captcha_file('image_screenshot.png')
        
        # captcha return non 3-digig result -> redo this iteration
        if len(captcha_result) != 3:
            driver.close()
            continue
        
        driver.find_element(By.NAME, "auth_num").send_keys(captcha_result)
        
        
        
        # enter
        driver.find_element(by=By.NAME, value="Submit").click()
        
            
        
        try:
            WebDriverWait(driver, 1).until(EC.alert_is_present())
            driver.switch_to.alert.accept()
            print("alert(curriculum login)-yes")
            driver.close()
            continue
        except TimeoutException:
            print("alert(curriculum login)-no")
        
        
        
        
        driver.find_element(by=By.NAME, value="Submit6").click()
        
        sleep(3)
        
        driver.switch_to.window(driver.window_handles[1])
        
        url = driver.current_url
        
        driver.close()
        
        break
    
    driver.quit
    
    return url.replace('11110CS%20%20135501', '')