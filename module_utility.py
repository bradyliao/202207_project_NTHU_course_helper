import pandas as pd
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup



def to_df(driver):
    soup=BeautifulSoup(driver.page_source, 'html.parser')
    trs = soup.find_all('tr')[1:]
    rows = list()
    for tr in trs:
        rows.append([td.text.replace('\n', '').replace('\xa0', '').replace('\t', '') for td in tr.find_all('td')])
    df = pd.DataFrame(data=rows)
    return df    

def grab_GPA(driver, semester):
    # 選所有課程
    Select(driver.find_element(by=By.ID, value="qyt_id")).select_by_visible_text(semester)
    driver.find_element(by=By.NAME, value="Submit").click()

    # 按掉alert
    WebDriverWait(driver, 1).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

    # 等所有資料load
    sleep(5)
    
    # 表格轉dataframe
    df=to_df(driver)
    # df.columns=['科號 Course No.','科目名稱 Course Name','授課教師 Teacher','修課人數 Enrollment', '平均值 average GPA','標準差 standard deviation']
    
    #上一頁
    driver.find_element(by=By.NAME, value="Submit").click()
    
    return df

def to_reference(string):
    out = ''
    for c in string:
        if c.isalpha():
            out += str(ord(c))
    
    return out



def tablepress_link_code(display_str, url, target_str):
    link = url + '?table_filter=' + target_str
    code = '<a href=\"' + link + '\" rel=\"noopener\" target=\"_blank\">' + display_str + '</a>'
    
    return code


def hyperlink_code(display_str, link):
    code = '<a href=\"' + link + '\" rel=\"noopener\" target=\"_blank\">' + display_str + '</a>'
    return code