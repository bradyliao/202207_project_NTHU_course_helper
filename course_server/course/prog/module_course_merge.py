import pandas as pd
import re
import datetime

from module_utility import tablepress_link_code, to_reference, hyperlink_code



def course_merge(data_folder_path, global_semester, selection_system_on, GPArecord_url): 
    
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " course_merge - start")
    
    with open(data_folder_path + 'active_syllabus_url.txt') as f:
        syllabus_activity_url = f.readline().rstrip()
    
    
    course_data_processed_df = pd.read_csv(data_folder_path + global_semester + '_course_data_processed.csv')
    course_corriculum_processed_df = pd.read_csv(data_folder_path + global_semester + '_course_corriculum_processed.csv')
    
    
    newData = list()
    
    
    
    
    for row in range(0, course_data_processed_df.shape[0]):
        
        course_ID_full_orig   = course_data_processed_df.iloc[row,0 ]
        course_ID             = course_data_processed_df.iloc[row,1 ]
        course_num            = course_data_processed_df.iloc[row,2 ]
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
        
        Monday = 'O' if time.find('M')!=-1 else 'X'
        M1 = 'O' if time.find('M1')!=-1 else 'X'
        M2 = 'O' if time.find('M2')!=-1 else 'X'
        M3 = 'O' if time.find('M3')!=-1 else 'X'
        M4 = 'O' if time.find('M4')!=-1 else 'X'
        Mn = 'O' if time.find('Mn')!=-1 else 'X'
        M5 = 'O' if time.find('M5')!=-1 else 'X'
        M6 = 'O' if time.find('M6')!=-1 else 'X'
        M7 = 'O' if time.find('M7')!=-1 else 'X'
        M8 = 'O' if time.find('M8')!=-1 else 'X'
        M9 = 'O' if time.find('M9')!=-1 else 'X'
        Ma = 'O' if time.find('Ma')!=-1 else 'X'
        Mb = 'O' if time.find('Mb')!=-1 else 'X'
        Mc = 'O' if time.find('Mc')!=-1 else 'X'
        
        Tuesday = 'O' if time.find('T')!=-1 else 'X'
        T1 = 'O' if time.find('T1')!=-1 else 'X'
        T2 = 'O' if time.find('T2')!=-1 else 'X'
        T3 = 'O' if time.find('T3')!=-1 else 'X'
        T4 = 'O' if time.find('T4')!=-1 else 'X'
        Tn = 'O' if time.find('Tn')!=-1 else 'X'
        T5 = 'O' if time.find('T5')!=-1 else 'X'
        T6 = 'O' if time.find('T6')!=-1 else 'X'
        T7 = 'O' if time.find('T7')!=-1 else 'X'
        T8 = 'O' if time.find('T8')!=-1 else 'X'
        T9 = 'O' if time.find('T9')!=-1 else 'X'
        Ta = 'O' if time.find('Ta')!=-1 else 'X'
        Tb = 'O' if time.find('Tb')!=-1 else 'X'
        Tc = 'O' if time.find('Tc')!=-1 else 'X'
        
        Wednesday = 'O' if time.find('W')!=-1 else 'X'
        W1 = 'O' if time.find('W1')!=-1 else 'X'
        W2 = 'O' if time.find('W2')!=-1 else 'X'
        W3 = 'O' if time.find('W3')!=-1 else 'X'
        W4 = 'O' if time.find('W4')!=-1 else 'X'
        Wn = 'O' if time.find('Wn')!=-1 else 'X'
        W5 = 'O' if time.find('W5')!=-1 else 'X'
        W6 = 'O' if time.find('W6')!=-1 else 'X'
        W7 = 'O' if time.find('W7')!=-1 else 'X'
        W8 = 'O' if time.find('W8')!=-1 else 'X'
        W9 = 'O' if time.find('W9')!=-1 else 'X'
        Wa = 'O' if time.find('Wa')!=-1 else 'X'
        Wb = 'O' if time.find('Wb')!=-1 else 'X'
        Wc = 'O' if time.find('Wc')!=-1 else 'X'
        
        Thursday = 'O' if time.find('R')!=-1 else 'X'
        R1 = 'O' if time.find('R1')!=-1 else 'X'
        R2 = 'O' if time.find('R2')!=-1 else 'X'
        R3 = 'O' if time.find('R3')!=-1 else 'X'
        R4 = 'O' if time.find('R4')!=-1 else 'X'
        Rn = 'O' if time.find('Rn')!=-1 else 'X'
        R5 = 'O' if time.find('R5')!=-1 else 'X'
        R6 = 'O' if time.find('R6')!=-1 else 'X'
        R7 = 'O' if time.find('R7')!=-1 else 'X'
        R8 = 'O' if time.find('R8')!=-1 else 'X'
        R9 = 'O' if time.find('R9')!=-1 else 'X'
        Ra = 'O' if time.find('Ra')!=-1 else 'X'
        Rb = 'O' if time.find('Rb')!=-1 else 'X'
        Rc = 'O' if time.find('Rc')!=-1 else 'X'
        
        Friday = 'O' if time.find('F')!=-1 else 'X'
        F1 = 'O' if time.find('F1')!=-1 else 'X'
        F2 = 'O' if time.find('F2')!=-1 else 'X'
        F3 = 'O' if time.find('F3')!=-1 else 'X'
        F4 = 'O' if time.find('F4')!=-1 else 'X'
        Fn = 'O' if time.find('Fn')!=-1 else 'X'
        F5 = 'O' if time.find('F5')!=-1 else 'X'
        F6 = 'O' if time.find('F6')!=-1 else 'X'
        F7 = 'O' if time.find('F7')!=-1 else 'X'
        F8 = 'O' if time.find('F8')!=-1 else 'X'
        F9 = 'O' if time.find('F9')!=-1 else 'X'
        Fa = 'O' if time.find('Fa')!=-1 else 'X'
        Fb = 'O' if time.find('Fb')!=-1 else 'X'
        Fc = 'O' if time.find('Fc')!=-1 else 'X'
        
        Saturday = 'O' if time.find('S')!=-1 else 'X'
        S1 = 'O' if time.find('S1')!=-1 else 'X'
        S2 = 'O' if time.find('S2')!=-1 else 'X'
        S3 = 'O' if time.find('S3')!=-1 else 'X'
        S4 = 'O' if time.find('S4')!=-1 else 'X'
        Sn = 'O' if time.find('Sn')!=-1 else 'X'
        S5 = 'O' if time.find('S5')!=-1 else 'X'
        S6 = 'O' if time.find('S6')!=-1 else 'X'
        S7 = 'O' if time.find('S7')!=-1 else 'X'
        S8 = 'O' if time.find('S8')!=-1 else 'X'
        S9 = 'O' if time.find('S9')!=-1 else 'X'
        Sa = 'O' if time.find('Sa')!=-1 else 'X'
        Sb = 'O' if time.find('Sb')!=-1 else 'X'
        Sc = 'O' if time.find('Sc')!=-1 else 'X'
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        # 選課系統 - 開
        if(selection_system_on):
            chance_text = '選上機率\nChance'
            
        # 選課系統 - 關
        else:            
            if (course_corriculum_processed_df[course_corriculum_processed_df['course_ID_full_orig']==course_ID_full_orig].size == 0):
                current_enrollment = '--'
            else:
                current_enrollment = course_corriculum_processed_df[course_corriculum_processed_df['course_ID_full_orig']==course_ID_full_orig].values[0,1]
            
            if limit != '--' and current_enrollment != '--' and int(limit)!=0 :
                spots_avl = int(limit) - int(current_enrollment)
                chance = int(spots_avl)/int(limit)
                chance = "{:4.2f}".format(chance)
            else:
                spots_avl = '--'
                chance = '--'
            
            pending_enrollment = '--'
            
            chance_text = '空位比例\nAVL/Lim'
        
        
        
        
        
        # -------------------------------------------------------------------------------------------------------------------------------------------------- display output for table
        display_course_ID = tablepress_link_code(course_ID, GPArecord_url, course_num) + '\n' + course_title_zh + '\n' + course_title_eng
        
        filter_course = course_ID[:-2] + ' ' + course_title_zh + ' ' + course_title_eng
        
        display_instructor = ''
        
        instructor_split = re.split('\n', instructor)
        for line in instructor_split:
            display_instructor = tablepress_link_code(line, GPArecord_url, to_reference(line)) + '\n'
        
        display_instructor = display_instructor[:-1]
        
        
        display_info = '<strong>' + hyperlink_code('課綱 Syllabus', syllabus_activity_url+course_ID_full_orig.replace(' ', '%20')) + '</strong>' + '\n' \
                     + '<strong>學分數 Credit unit : </strong>' + str(credit_unit) + '\n' \
                     + '<strong>授課語言 Language : </strong>' + language + '\n' \
                     + '<strong>教師 Instructor : </strong>\n' + display_instructor  + '\n' \
                     + '<strong>教室 Room & 時間 Time : </strong>\n' + room_and_time_orig
                     
        
        
        
        
        display_enrollment = '<strong>加簽 Extra Enrollment : </strong>\n' + str(extra_enrollment) + '\n'\
                           + '<strong>人限 Limit / 新生保留 New Only : </strong>\n'  + str(limit) + ' / ' + str(new_only) + '\n' \
                           + '<strong>剩餘名額 Spots AVL / 待亂數 Pending : </strong>\n'  + str(spots_avl) + ' / ' + str(pending_enrollment) + '\n' \



        display_other = '<strong>備註 Note : </strong>' + ( memo if(memo == '--') else ('\n' + memo) ) + '\n'\
                      + '<strong>限制 Limitation : </strong>' + ( limitation if(limitation == '--') else ('\n' + limitation) ) + '\n'\
                      + '<strong>擋修 Prerequisite : </strong>' + ( prerequisite if(prerequisite == '--') else ('\n' + prerequisite) ) + '\n'\
                      + '<strong>專長 Speciality : </strong>' + ( speciality if(speciality == '--') else ('\n' + speciality) ) + '\n'\
                      + '<strong>學程 Program : </strong>' + ( program if(program == '--') else ('\n' + program) ) + '\n'\
                      + '<strong>必選修 Required / Elective : </strong>' + ( required_or_elective if(required_or_elective == '--') else ('\n' + required_or_elective) ) + '\n'\
        

        course_level = course_num[-4] + "XXX"
        
                            
        
        
        
        newData.append([display_course_ID, display_info, display_enrollment, display_other, department, gen_cat, chance, building, language, extra_enrollment, course_level,
                        filter_course,
                        Monday,
                        M1, M2, M3, M4, Mn, M5, M6, M7, M8, M9, Ma, Mb, Mc,
                        Tuesday,
                        T1, T2, T3, T4, Tn, T5, T6, T7, T8, T9, Ta, Tb, Tc, 
                        Wednesday,
                        W1, W2, W3, W4, Wn, W5, W6, W7, W8, W9, Wa, Wb, Wc, 
                        Thursday,
                        R1, R2, R3, R4, Rn, R5, R6, R7, R8, R9, Ra, Rb, Rc, 
                        Friday,
                        F1, F2, F3, F4, Fn, F5, F6, F7, F8, F9, Fa, Fb, Fc, 
                        Saturday,
                        S1, S2, S3, S4, Sn, S5, S6, S7, S8, S9, Sa, Sb, Sc
                        ])
        
        
        
    course_merged = pd.DataFrame(data=newData)
    course_merged.columns = ['課號 Course ID', '課程資訊 Course Info', '註冊資訊 Enrollment Info', '其他 Other', '系所 Department', '通識 GE', chance_text, '教室大樓 Building', '授課語言 Language', '加簽 Extra Enrollment', '課程年級 Course Level (4位數課號的第一個數字，不見得適用每一個科系)',
                            '課程 Course ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------',
                            'Monday -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', 
                            'M1', 'M2', 'M3', 'M4', 'Mn', 'M5', 'M6', 'M7', 'M8', 'M9', 'Ma', 'Mb', 'Mc', 
                            'Tuesday -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', 
                            'T1', 'T2', 'T3', 'T4', 'Tn', 'T5', 'T6', 'T7', 'T8', 'T9', 'Ta', 'Tb', 'Tc', 
                            'Wednesday ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', 
                            'W1', 'W2', 'W3', 'W4', 'Wn', 'W5', 'W6', 'W7', 'W8', 'W9', 'Wa', 'Wb', 'Wc', 
                            'Thursday ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', 
                            'R1', 'R2', 'R3', 'R4', 'Rn', 'R5', 'R6', 'R7', 'R8', 'R9', 'Ra', 'Rb', 'Rc', 
                            'Friday ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', 
                            'F1', 'F2', 'F3', 'F4', 'Fn', 'F5', 'F6', 'F7', 'F8', 'F9', 'Fa', 'Fb', 'Fc', 
                            'Saturday ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', 
                            'S1', 'S2', 'S3', 'S4', 'Sn', 'S5', 'S6', 'S7', 'S8', 'S9', 'Sa', 'Sb', 'Sc'
                            ]
    
    course_merged.to_csv(data_folder_path + global_semester + '_course_merged.csv', index=False)
    
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " course_merge - done")
    