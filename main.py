import pandas as pd
from module_crawler_course_data import crawler_course_data
from module_crawler_course_curriculum import crawler_course_curriculum
from module_data_process_merge import data_process_merge

# check tesseract path in module_captcha

# update before use
curriculum_url = 'https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/6/6.2/6.2.9/JH629001.php'
curriculum_semester_option = "111上(2022-Fall)"
global_semester = '111_10' # file name
course_data_url = 'https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/OPENDATA/open_course_data.json'

selenium_driver_path = './chromedriver_win.exe'
data_folder_path = './data/'



course_data_df = crawler_course_data(data_folder_path, global_semester, course_data_url)
course_data_df.to_csv(data_folder_path + global_semester + '_course_data.csv', index = False)

course_curriculum_df = crawler_course_curriculum(curriculum_semester_option, curriculum_url, selenium_driver_path)
course_curriculum_df.to_csv(data_folder_path + global_semester + '_course_corriculum.csv', index = False)

course_merged = data_process_merge(False, course_data_df, course_curriculum_df)
course_merged.to_csv(data_folder_path + global_semester + '_course_merged.csv', index = False)





















# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service



# # Selenium
# options = Options()
# options.add_argument("--disable-notifications")
# options.add_experimental_option('excludeSwitches', ['enable-logging']) # shut up error code triggered by chrome: "Failed to read descriptor from node connection: A device attached to the system is not functioning." 
# s = Service(selenium_driver_path)



# # open chrome
# driver = webdriver.Chrome(service= s, options= options)
# # to url
# driver.get(curriculum_url)

# # screenshot -> it will be the same from the website
# image_location = driver.find_element(By.XPATH, "/html/body/div/form/table[2]/tbody/tr/td/img")
# with open('image_screenshot.png', 'wb') as file:
#     file.write(image_location.screenshot_as_png)
    
    
