import pandas as pd

from module_course_curriculum_downloader import course_curriculum_downloader
from module_course_curriculum_processer import course_curriculum_processer

from module_course_data_downloader import course_data_downloader
from module_course_data_processer import course_data_processer

from module_course_enrollstatus_downloader import course_enrollstatus_downloader
from module_course_enrollstatus_processer import course_enrollstatus_processer

from module_refresh_syllabus_url import refresh_syllabus_url

from module_course_merge import course_merge

from module_GPA_downloader import GPA_downloader
from module_GPA_processer import GPA_processer

import time
import schedule
import datetime

# check tesseract path in module_captcha.py

# update before use
curriculum_url = 'https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/6/6.2/6.2.9/JH629001.php'
curriculum_semester_option = "111上(2022-Fall)"
global_semester = '111_10' # file name
course_data_url = 'https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/OPENDATA/open_course_data.json'

selenium_driver_path = './chromedriver'
data_folder_path = '../data/'

NTHU_homepage_url = 'https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/'
student_ID = '109062272'
password = 'relatedPoland793'
# To all of you got here, I know wordpress is fragile.
# I'm just trying to make the course registration easier.
# Please don't hack this account, this account is not even mine. (My friend's)



GPArecord_url = 'https://nthucourse.com/gpa-record/'


# test use in mac
if False:
    selenium_driver_path = './chromedriver_mac'
    selection_system_on = True
    # course_enrollstatus_processer(data_folder_path, global_semester)                                                                        # < 1s
    course_merge(data_folder_path, global_semester, selection_system_on, GPArecord_url)
    exit()



# get course information data from 教務處
course_data_downloader(data_folder_path, global_semester, course_data_url)      # < 1s
course_data_processer(data_folder_path, global_semester)                        # 2s

# curriculum page info
# return ['course_ID_full_orig', 'current_stage_enrollment']
# course_curriculum_downloader(data_folder_path, global_semester, curriculum_semester_option, curriculum_url, selenium_driver_path)       # 12 min on server
# course_curriculum_processer(data_folder_path, global_semester)                                                                          # 1s

# enrollment status
course_enrollstatus_downloader(selenium_driver_path, NTHU_homepage_url, global_semester, student_ID, password, data_folder_path)        # 3 ish min
course_enrollstatus_processer(data_folder_path, global_semester)                                                                        # < 1s

# get active syllabus url
refresh_syllabus_url(curriculum_semester_option, curriculum_url, selenium_driver_path, data_folder_path)

# merge data
if datetime.datetime.now() < datetime.datetime(2022, 8, 23, 9, 0, 0):
    selection_system_on = True
else:
    selection_system_on = False

course_merge(data_folder_path, global_semester, selection_system_on, GPArecord_url)


# GPA record - need it once a semester after GPA is availiable
# grap_GPA_semester_name = '109上(2020-Fall)'
# grap_GPA_semester_code = '109_10'
# GPA_downloader(selenium_driver_path, NTHU_homepage_url, student_ID, password, data_folder_path, grap_GPA_semester_name, grap_GPA_semester_code )
# GPA_processer(data_folder_path, grap_GPA_semester_code)






'''
# course information data
schedule.every().day.at("12:16:00").do(course_data_downloader, data_folder_path, global_semester, course_data_url)
schedule.every().day.at("12:16:30").do(course_data_processer, data_folder_path, global_semester)

# curriculum page download
schedule.every().day.at("12:30:30").do(course_data_downloader, data_folder_path, global_semester, course_data_url)
schedule.every().day.at("12:43:45").do(course_data_processer, data_folder_path, global_semester)
'''

schedule.every().hour.at("55:00").do(course_enrollstatus_downloader, selenium_driver_path, NTHU_homepage_url, global_semester, student_ID, password, data_folder_path)
schedule.every().hour.at("59:00").do(course_enrollstatus_processer,data_folder_path, global_semester)
schedule.every().hour.at("59:20").do(refresh_syllabus_url, curriculum_semester_option, curriculum_url, selenium_driver_path, data_folder_path)
schedule.every().hour.at("59:50").do(course_merge, data_folder_path, global_semester, selection_system_on, GPArecord_url)


schedule.every().hour.at("10:00").do(course_enrollstatus_downloader, selenium_driver_path, NTHU_homepage_url, global_semester, student_ID, password, data_folder_path)
schedule.every().hour.at("14:00").do(course_enrollstatus_processer,data_folder_path, global_semester)
schedule.every().hour.at("14:20").do(refresh_syllabus_url, curriculum_semester_option, curriculum_url, selenium_driver_path, data_folder_path)
schedule.every().hour.at("14:50").do(course_merge, data_folder_path, global_semester, selection_system_on, GPArecord_url)

schedule.every().hour.at("25:00").do(course_enrollstatus_downloader, selenium_driver_path, NTHU_homepage_url, global_semester, student_ID, password, data_folder_path)
schedule.every().hour.at("29:00").do(course_enrollstatus_processer,data_folder_path, global_semester)
schedule.every().hour.at("29:20").do(refresh_syllabus_url, curriculum_semester_option, curriculum_url, selenium_driver_path, data_folder_path)
schedule.every().hour.at("29:50").do(course_merge, data_folder_path, global_semester, selection_system_on, GPArecord_url)

schedule.every().hour.at("40:00").do(course_enrollstatus_downloader, selenium_driver_path, NTHU_homepage_url, global_semester, student_ID, password, data_folder_path)
schedule.every().hour.at("44:00").do(course_enrollstatus_processer,data_folder_path, global_semester)
schedule.every().hour.at("44:20").do(refresh_syllabus_url, curriculum_semester_option, curriculum_url, selenium_driver_path, data_folder_path)
schedule.every().hour.at("44:50").do(course_merge, data_folder_path, global_semester, selection_system_on, GPArecord_url)

while True:
    if datetime.datetime.now() < datetime.datetime(2022, 8, 23, 9, 0, 0):
        selection_system_on = True
    else:
        selection_system_on = False
    
    schedule.run_pending()
    time.sleep(1)
