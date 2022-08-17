import pandas as pd
import requests
import datetime

def course_data_downloader(data_folder_path, global_semester, course_data_url):
    
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " course_data_downloader - start")
    
    # get json and save
    response = requests.get(course_data_url)
    open(data_folder_path + global_semester + "_course_data_downloaded.json", "wb").write(response.content)
    
    # open json and save to csv
    course_data_df = pd.read_json(data_folder_path + global_semester + "_course_data_downloaded.json", encoding='UTF-8')
    course_data_df.to_csv(data_folder_path + global_semester + '_course_data_downloaded.csv', index = False)
    
    
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " course_data_downloader - done")
