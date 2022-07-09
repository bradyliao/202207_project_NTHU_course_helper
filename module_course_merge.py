import pandas as pd
import re

from module_utility import tablepress_link_code, to_reference



def course_merge(data_folder_path, global_semester, selection_system_on, GPArecord_url): 
    
    course_data_processed_df = pd.read_csv(data_folder_path + global_semester + '_course_data_processed.csv')
    course_corriculum_processed_df = pd.read_csv(data_folder_path + global_semester + '_course_corriculum_processed.csv')
    
    
    newData = list()
    
    
    
    
    for row in range(0, course_data_processed_df.shape[0]):

        
        course_ID_full_orig   = course_data_processed_df.iloc[row,0 ]
        course_ID             = course_data_processed_df.iloc[row,1 ]
        course                = course_data_processed_df.iloc[row,2 ]
        department            = course_data_processed_df.iloc[row,3 ]
        course_title_zh       = course_data_processed_df.iloc[row,4 ]
        course_title_eng      = course_data_processed_df.iloc[row,5 ]
        credit_unit           = course_data_processed_df.iloc[row,6 ]
        limit                 = course_data_processed_df.iloc[row,7 ]
        new_only              = course_data_processed_df.iloc[row,8 ]
        gen_cat               = course_data_processed_df.iloc[row,9 ]
        language              = course_data_processed_df.iloc[row,10]
        room_and_time_orig    = course_data_processed_df.iloc[row,11]
        time                  = course_data_processed_df.iloc[row,12]
        building              = course_data_processed_df.iloc[row,13]
        instructor            = course_data_processed_df.iloc[row,14]
        memo                  = course_data_processed_df.iloc[row,15]
        prerequisite          = course_data_processed_df.iloc[row,16]
        limitation            = course_data_processed_df.iloc[row,17]
        speciality            = course_data_processed_df.iloc[row,18]
        program               = course_data_processed_df.iloc[row,19]
        extra_enrollment      = course_data_processed_df.iloc[row,20]
        required_or_elective  = course_data_processed_df.iloc[row,21]
        
        
        


        
        # 選課系統 - 開
        if(selection_system_on):
            dummy=1
            
        # 選課系統 - 關
        else:            
            if (course_corriculum_processed_df[course_corriculum_processed_df['course_ID_full_orig']==course_ID_full_orig].size == 0):
                current_enrollment = '--'
            else:
                current_enrollment = course_corriculum_processed_df[course_corriculum_processed_df['course_ID_full_orig']==course_ID_full_orig].values[0,1]
            
            if limit != '--' and current_enrollment != '--':
                spots_avl = int(limit) - int(current_enrollment)
            else:
                spots_avl = '--'

            pending_enrollment = '--'
            chance = '--'
        
        
        
        
        
        # -------------------------------------------------------------------------------------------------------------------------------------------------- display output for table
        display_course_ID = tablepress_link_code(course_ID, GPArecord_url, course) + '\n' + course_title_zh + '\n' + course_title_eng
        
        
        display_instructor = ''
        
        instructor_split = re.split('\n', instructor)
        for line in instructor_split:
            display_instructor = tablepress_link_code(line, GPArecord_url, to_reference(line)) + '\n'
        
        display_instructor = display_instructor[:-1]
        
        
        
        display_info = '<人限 Limit / 新生保留 New Only>' + '\n' + str(limit) + ' / ' + str(new_only) + '\n' \
                     + '<剩餘名額 Spots AVL / 待亂數 Pending>' + '\n' + str(spots_avl) + ' / ' + str(pending_enrollment) + '\n' \
                     + '<學分數 Credit unit>' + '\n' + str(credit_unit) + '\n' \
                     + '<授課語言 Language>' + '\n' + language + '\n' \
                     + '<教師 Instructor>\n' + display_instructor  + '\n' \
                     + '<教室 Room & 時間 Time>\n' + room_and_time_orig
        
        
        display_note = '<加簽 Extra Enrollment>\n' + str(extra_enrollment) + '\n'\
                     + '<備註 Memo>\n' + memo + '\n'\
                     + '<限制 Limitation>\n' + limitation + '\n'\
                     + '<擋修 Prerequisite>\n' + prerequisite + '\n'\
                     + '<專長 Speciality>\n' + speciality + '\n'\
                     + '<學程 Program>\n' + program + '\n'\
                     + '<必選修 Required or Elective>\n' + required_or_elective + '\n'\
                            
        
        
        
        newData.append([display_course_ID, display_info, display_note, department, gen_cat, chance, '', course, building, time, language, extra_enrollment])
        
        
        
    course_merged = pd.DataFrame(data=newData)
    course_merged.columns = ['課號 Course ID', '資訊 Information', '備註 Note', '系所 Department', '通識 GE', '選上機率\nChance', '重設\nReset', '課程 Course', '教室大樓 Building', '時間 Time', '授課語言 Language', '加簽 Extra Enrollment']
    
    course_merged.to_csv(data_folder_path + global_semester + '_course_merged.csv', index=False)