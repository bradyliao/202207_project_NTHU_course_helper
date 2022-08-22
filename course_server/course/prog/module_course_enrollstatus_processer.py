# only copy paste from curriculum part

import pandas as pd
import datetime


def course_enrollstatus_processer(data_folder_path, global_semester):
    
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " course_enrollstatus_processer - start")

    course_enrollstatus_df = pd.read_csv(data_folder_path + global_semester + '_course_enrollstatus_downloaded.csv')
    
    newData = list()
    
    
    for row in range(0, course_enrollstatus_df.shape[0]):
        course_ID_full_orig = course_enrollstatus_df.iloc[row,0]
        
        if pd.isna(course_enrollstatus_df.iloc[row,8]):
            current_enrollment = int(course_enrollstatus_df.iloc[row,5])
            if course_enrollstatus_df.iloc[row,6] == '無限制':
                spots_avl = '∞'
            else:
                spots_avl = int(course_enrollstatus_df.iloc[row,6])
            pending_enrollment = int(course_enrollstatus_df.iloc[row,7])
        else:
            current_enrollment = int(course_enrollstatus_df.iloc[row,6])
            if course_enrollstatus_df.iloc[row,7] == '無限制':
                spots_avl = '∞'
            else:
                spots_avl = int(course_enrollstatus_df.iloc[row,7])
            pending_enrollment = int(course_enrollstatus_df.iloc[row,8])
        
        
        newData.append([course_ID_full_orig, current_enrollment, spots_avl, pending_enrollment])
        
        
        
    course_enrollstatus_processed_df = pd.DataFrame(data=newData)
    #                                           0                      1                        2           3
    course_enrollstatus_processed_df.columns = ['course_ID_full_orig', 'current_enrollment', 'spots_avl', 'pending_enrollment']
    
    course_enrollstatus_processed_df.to_csv(data_folder_path + global_semester + '_course_enrollstatus_processed.csv', index=False)
    course_enrollstatus_processed_df.to_csv(data_folder_path + 'log/' + datetime.datetime.now().strftime("%Y%m%d_%H%M%S_") + global_semester + '_course_enrollstatus_processed.csv', index=False)
    
    
    
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " course_enrollstatus_processer - done")