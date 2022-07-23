import pandas as pd

from module_course_curriculum_downloader import course_curriculum_downloader
from module_course_curriculum_processer import course_curriculum_processer

from module_course_data_downloader import course_data_downloader
from module_course_data_processer import course_data_processer

from module_refresh_syllabus_url import refresh_syllabus_url

from module_course_merge import course_merge

from module_GPA_downloader import GPA_downloader
from module_GPA_processer import GPA_processer

# check tesseract path in module_captcha

# update before use
curriculum_url = 'https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/6/6.2/6.2.9/JH629001.php'
curriculum_semester_option = "111上(2022-Fall)"
global_semester = '111_10' # file name
course_data_url = 'https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/OPENDATA/open_course_data.json'

selenium_driver_path = './chromedriver_win.exe'
data_folder_path = './data/'

NTHU_homepage_url = 'https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/'
student_ID = '109062272'
password = 'swedenLettuce342'



GPArecord_url = 'https://nthucourse.com/gpa-record/'


# # course_curriculum_downloader(data_folder_path, global_semester, curriculum_semester_option, curriculum_url, selenium_driver_path)
# course_curriculum_processer(data_folder_path, global_semester)

# # course_data_downloader(data_folder_path, global_semester, course_data_url)
# course_data_processer(data_folder_path, global_semester)

syllabus_activity_url = refresh_syllabus_url(curriculum_semester_option, curriculum_url, selenium_driver_path)



selection_system_on = False
course_merge(data_folder_path, global_semester, selection_system_on, GPArecord_url, syllabus_activity_url)








# grap_GPA_semester_name = '109上(2020-Fall)'
# grap_GPA_semester_code = '109_10'
# GPA_downloader(selenium_driver_path, NTHU_homepage_url, student_ID, password, data_folder_path, grap_GPA_semester_name, grap_GPA_semester_code )
# GPA_processer(data_folder_path, grap_GPA_semester_code)
