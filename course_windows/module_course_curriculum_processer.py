import pandas as pd


def course_curriculum_processer(data_folder_path, global_semester):
    
    

    course_corriculum_df = pd.read_csv(data_folder_path + global_semester + '_course_corriculum_downloaded.csv')
    
    newData = list()
    
    
    for row in range(0, course_corriculum_df.shape[0]):
        if (pd.isna(course_corriculum_df.iloc[row,4]) ):
            continue
        else:
            course_ID_full_orig = course_corriculum_df.iloc[row,0]
            current_enrollment = int(course_corriculum_df.iloc[row,8])
        
        
        newData.append([course_ID_full_orig, current_enrollment])
        
        
        
    course_corriculum_processed_df = pd.DataFrame(data=newData)
    #                                           0                      1
    course_corriculum_processed_df.columns = ['course_ID_full_orig', 'current_enrollment']
    
    course_corriculum_processed_df.to_csv(data_folder_path + global_semester + '_course_corriculum_processed.csv', index=False)