import pandas as pd
import requests




def crawler_course_data(data_folder_path, global_semester, course_data_url):
    
    # get json and save
    response = requests.get(course_data_url)
    open(data_folder_path + global_semester + "_course_data.json", "wb").write(response.content)
    
    # open json as df
    course_data_df = pd.read_json(data_folder_path + global_semester + "_course_data.json", encoding='UTF-8')
    
    
    return course_data_df