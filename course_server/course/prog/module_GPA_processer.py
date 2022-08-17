import pandas as pd
import re
import html
from module_utility import to_reference




def GPA_processer(data_folder_path, grap_GPA_semester_code):
    
    

    GPA_new_df = pd.read_csv(data_folder_path + 'GPA_downloaded_' + grap_GPA_semester_code + '.csv')

    
    
    newData = list()
        
    for row in range(0, GPA_new_df.shape[0]):

        
        # --------------------------------------------------------------------------------------- (col. 0) course_ID_full_orig  -> course_ID, course
        course_ID_full_orig = GPA_new_df.iloc[row,0]
        
        semester = course_ID_full_orig[0:3]
        if course_ID_full_orig[3:5] == '10':
            semester += '上'
        elif course_ID_full_orig[3:5] == '20':
            semester += '下'
        elif course_ID_full_orig[3:5] == '30':
            semester += '暑'
        else:
            semester = 'ERROR'
        

        course_ID = course_ID_full_orig.replace('  ', ' ')
        if course_ID.count(' ') == 0:
            course_ID = course_ID[:-6] + ' ' + course_ID[-6:]
        course_ID = course_ID[5:]

        
        course = course_ID[:-2].replace(' ', '')
        
        
        
        # --------------------------------------------------------------------------------------- (col. 1) course_title_zh_eng
        course_title_zh_eng = GPA_new_df.iloc[row,1]
        
        for i in range(1, len(course_title_zh_eng)-1 ):
            if( \
            ( ord(course_title_zh_eng[i-1])<0 or ord(course_title_zh_eng[i-1])>127 ) and \
            ( ord(course_title_zh_eng[i])>=0 and ord(course_title_zh_eng[i])<=127 ) and \
            ( ord(course_title_zh_eng[i+1])>=0 and ord(course_title_zh_eng[i+1])<=127 ) \
            ):
                course_title_zh_eng = course_title_zh_eng[:i] + '\n' + course_title_zh_eng[i:]
                break
            
            

        # --------------------------------------------------------------------------------------- (col. 3) instructor
        instructor = GPA_new_df.iloc[row,2]
        # 分行
        for i in range(1, len(instructor) ):
            if( \
            ( ord(instructor[i-1])>=65 and ord(instructor[i-1])<=90 ) and \
            ( ord(instructor[i])<0 or ord(instructor[i])>127 ) \
            ):
                instructor = instructor[:i] + '\n' + instructor[i:]
        
        instructor_ref = to_reference(instructor)
        
        
        enrollment_count = int(GPA_new_df.iloc[row,3])
        average_GPA = float(GPA_new_df.iloc[row,4])
        SD = float(GPA_new_df.iloc[row,5])
        
        
        
        
        #                0          1          2                    3           4                 5            6   7      8
        newData.append( [semester, course_ID, course_title_zh_eng, instructor, enrollment_count, average_GPA, SD, course,instructor_ref] ) 
        
    # --------------------------------------------------------------------------------------- end of for loop
    
    course_data_processed_df = pd.DataFrame(data=newData)
    course_data_processed_df.columns = ['學期\nSemester', '課號\nCourse ID', '課名\nCourse Title', '教師\nInstructor', '選課人數\nEnrollment Count', '平均GPA\nAverage GPA', '標準差\nStandard Deviation', 'course', 'instructor_ref']
    
    course_data_processed_df.to_csv(data_folder_path + 'GPA_processed_' + grap_GPA_semester_code + '.csv', index=False)
