
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
from module_captcha import captcha_file

def course_curriculum_downloader(data_folder_path, global_semester, curriculum_semester_option, curriculum_url, selenium_driver_path):
    
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " course_curriculum_downloader - start")
    
    # Selenium
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_experimental_option('excludeSwitches', ['enable-logging']) # shut up error code triggered by chrome: "Failed to read descriptor from node connection: A device attached to the system is not functioning." 
    s = Service(selenium_driver_path)
    
    
    
    # open chrome
    driver = webdriver.Chrome(service= s, options= options)
    # to url
    driver.get(curriculum_url)
    # select semester
    Select(driver.find_element(by=By.ID, value="YS_id")).select_by_visible_text(curriculum_semester_option)
    # click first option ( 僅列出所選開課代號之科目(only courses offered by this department) )
    driver.find_element(by=By.NAME, value="cond").click()
    # get drop down menu length
    dropdownlist_len = len( Select(driver.find_element(by=By.NAME, value="cou_code")).options )
    # close the tab
    driver.close()
    
    
    # print drop down menu length
    print("Drop down list length: " + str(dropdownlist_len))
    
    course_curriculum_df = pd.DataFrame()
    
    
    i = 1
    while i < dropdownlist_len:
        # open chrome
        driver = webdriver.Chrome(service= s, options= options)
        # to url
        driver.get(curriculum_url)
        # select semester
        Select(driver.find_element(by=By.ID, value="YS_id")).select_by_visible_text(curriculum_semester_option)
        # click first option ( 僅列出所選開課代號之科目(only courses offered by this department) )
        driver.find_element(by=By.NAME, value="cond").click()
        # choose i th option in the drop down menu
        Select(driver.find_element(by=By.NAME, value="cou_code")).select_by_index(i)
        
        
        
        
        
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
        # captcha key in
        driver.find_element(By.NAME, "auth_num").send_keys(captcha_result)
        # enter
        driver.find_element(by=By.NAME, value="Submit").click()
        
            
        
        try:
            WebDriverWait(driver, 1).until(EC.alert_is_present())
            driver.switch_to.alert.accept()
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " course_curriculum_downloader - login - " + str(i) + " - fail")
            driver.close()
            continue
        except TimeoutException:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " course_curriculum_downloader - login - " + str(i) + " - success")
        
        
        

        # load data to dataframe
        course_curriculum_df_incoming = to_df(driver=driver)
        
        # combine current & incoming dataframe
        course_curriculum_df = pd.concat([course_curriculum_df, course_curriculum_df_incoming], ignore_index=True, sort=False)
        
        driver.close()
        
        i += 1
    
    driver.quit
    
    
    
    # drop 必選修說明 row
    row_to_drop = []
    for row in range(0, len(course_curriculum_df)):
        if course_curriculum_df.loc[row][8]  == None:
            row_to_drop.append(row)
    course_curriculum_df = course_curriculum_df.drop(index=row_to_drop)
    
    
    
    course_curriculum_df.to_csv(data_folder_path + global_semester + '_course_corriculum_downloaded.csv', index = False)
    course_curriculum_df.to_csv(data_folder_path + 'log/' + datetime.datetime.now().strftime("%Y%m%d_%H%M%S_") + global_semester + '_course_corriculum_downloaded.csv', index = False)

    
    
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " course_curriculum_downloader - done")