
import pandas as pd
import re



def data_process_merge(selection_system_on, course_data_df, course_curriculum_df): 
    
    
    newData = list()
    
    # not included: 6通識對象
    
    error_message = 'error (screenshot and send it to me)'
    
    
    for row in range(0, course_data_df.shape[0]):
        # --------------------------------------------------------------------------------------- (col. 10) course_cancel 停開直接移除
        course_cancel = course_data_df.iloc[row,10]
        if course_cancel == '停開':
            continue
        
        
        # --------------------------------------------------------------------------------------- (col. 0) course_ID_full_orig  -> course_ID, department
        course_ID_full_orig = course_data_df.iloc[row,0]
        course_ID = course_ID_full_orig.replace('  ', ' ')
        if course_ID.count(' ') == 0:
            course_ID = course_ID[:-6] + ' ' + course_ID[-6:]
        course_ID = course_ID[5:]
        department = course_ID[:-7]
        
        
        # --------------------------------------------------------------------------------------- (col. 1) course_title_zh, (col. 2) course_title_eng
        course_title_zh = course_data_df.iloc[row,1]
        course_title_eng = course_data_df.iloc[row,2]
        
        
        # --------------------------------------------------------------------------------------- (col. 3) credit_units
        credit_units = course_data_df.iloc[row,3]
        
        
        # --------------------------------------------------------------------------------------- (col. 4) limit
        limit = course_data_df.iloc[row,4]
        limit = '-' if (limit=='') else limit
        
        # --------------------------------------------------------------------------------------- (col. 5) new_only
        new_only = course_data_df.iloc[row,5]
        
        
        # --------------------------------------------------------------------------------------- (col. 7) gen_cat
        if course_data_df.iloc[row,7] == '核心通識Core GE courses 1':
            gen_cat = '核通 GEC 1'
        elif course_data_df.iloc[row,7] == '核心通識Core GE courses 2':
            gen_cat = '核通 GEC 2'
        elif course_data_df.iloc[row,7] == '核心通識Core GE courses 3':
            gen_cat = '核通 GEC 3'
        elif course_data_df.iloc[row,7] == '核心通識Core GE courses 4':
            gen_cat = '核通 GEC 4'
        elif course_data_df.iloc[row,7] == '自然科學領域 Elective GE course: Natural Sciences':
            gen_cat = '自然 Natural'
        elif course_data_df.iloc[row,7] == '社會科學領域 Elective GE course: Social Sciences':
            gen_cat = '社會 Social'
        else:
            gen_cat = ''
        
        
        # --------------------------------------------------------------------------------------- (col. 8) language
        if course_data_df.iloc[row,8] == '中':
            language = '中文 ZH'
        elif course_data_df.iloc[row,8] == '英':
            language = '英文 EN'
        else:
            language = 'other'
            
    
        # --------------------------------------------------------------------------------------- (col. 11) room_and_time_orig -> room_and_time_split(room,time,room,time...), time, building
        if course_data_df.iloc[row,11] != '':
            room_and_time_orig = course_data_df.iloc[row,11]
            room_and_time_split = re.split('\t|\n', course_data_df.iloc[row,11] )
            time = ''
            building =''
            for i in range(0, len(room_and_time_split)-1):
                if i%2 == 1:
                    time = time + room_and_time_split[i]
                else:
                    toRemove = -1
                    for j in range(len(room_and_time_split[i])-1, 0, -1):
                        if ( ord(room_and_time_split[i][j])>=48 and ord(room_and_time_split[i][j])<=57 ) or ( ord(room_and_time_split[i][j])>=65 and ord(room_and_time_split[i][j])<=90 ) or room_and_time_split[i][j].isdigit():
                            toRemove = j
                        else:
                            break
                    if building == '':
                        building = building + room_and_time_split[i][:toRemove]
                    else:
                        building = building + ' ' + room_and_time_split[i][:toRemove]
            
        
        # --------------------------------------------------------------------------------------- (col. 12) instructor
        instructor = course_data_df.iloc[row,12][:-1]
        
        
        
        
        
        # -------------------------------------------------------------------------------------------------------------------------------------------------- display_note
        # --------------------------------------------------------------------------------------- (col. 11) memo (備註)
        memo = course_data_df.iloc[row,9]
    
        # --------------------------------------------------------------------------------------- (col. 13) prerequisite
        prerequisite = course_data_df.iloc[row,13].replace('<div>', '').replace('<br>', '').replace('<BR>', '').replace('</div>', '').replace('  ', '')[1:]
        
        # --------------------------------------------------------------------------------------- (col. 14) limitation
        limitation = course_data_df.iloc[row,14]
        
        # --------------------------------------------------------------------------------------- (col. 15) speciality
        speciality = course_data_df.iloc[row,15].replace('\t', '/').replace('(第一專長)', '(一)').replace('(第二專長)', '(二)')
        
        # --------------------------------------------------------------------------------------- (col. 16) program
        program = course_data_df.iloc[row,16]
        
        # --------------------------------------------------------------------------------------- (col. 17) extra_enrollment
        if(course_data_df.iloc[row,17]=='《不接受加簽 No extra selection》'):
            extra_enrollment = 'X 不接受 Not Allowed'
        elif(course_data_df.iloc[row,17]==''):
            extra_enrollment = 'O 接受 Allowed'
        else:
            extra_enrollment = error_message
        
        # --------------------------------------------------------------------------------------- (col. 18) required_or_elective
        required_or_elective = course_data_df.iloc[row,18].replace('  ', '').replace(' ', '').replace('\t', '/')[:-1]
        
        
        
        
        
        
        # -------------------------------------------------------------------------------------------------------------------------------------------------- from curriculum_df
        # --------------------------------------------------------------------------------------- (col. 8) spots_avl
        
        if(selection_system_on):
            dummy=1
        else:
            if len( course_curriculum_df.loc[course_curriculum_df[0] == course_ID_full_orig][8] ) == 0:
                current_enrollment = '-'
                spots_avl = '-'
            else:
                current_enrollment = int( course_curriculum_df.loc[course_curriculum_df[0] == course_ID_full_orig][8].values[0] )
                if limit != '-' and type(current_enrollment) == int:
                    spots_avl = int(limit) - current_enrollment
                else:
                    spots_avl = '-'
            
            pending_enrollment = '-'
            chance = '-'
        
        
        
        
        
        
        # -------------------------------------------------------------------------------------------------------------------------------------------------- display output for table
        display_course = course_ID + '\n' + course_title_zh + '\n' + course_title_eng
        
        
        
        display_info = '<人限 Limit / 新生保留 New Only>' + '\n' + str(limit) + ' / ' + str(new_only) + '\n' \
                     + '<剩餘名額 Spots AVL / 待亂數 Pending>' + '\n' + str(spots_avl) + ' / ' + str(pending_enrollment) + '\n' \
                     + '<學分數 Credit unit>' + '\n' + str(credit_units) + '\n' \
                     + '<授課語言 Language>' + '\n' + language + '\n' \
                     + '<教師 Instructor>\n' + instructor  + '\n' \
                     + '<教室 Room & 時間 Time>\n' + room_and_time_orig
        
        display_note = '<加簽 Extra Enrollment>\n' + extra_enrollment + '\n'\
                     + '<備註 Memo>\n' + memo + '\n'\
                     + '<限制 Limitation>\n' + limitation + '\n'\
                     + '<擋修 Prerequisite>\n' + prerequisite + '\n'\
                     + '<專長 Speciality>\n' + speciality + '\n'\
                     + '<學程 Program>\n' + program + '\n'\
                     + '<必選修 Required or Elective>\n' + required_or_elective + '\n'\
                            
        display_gen_cat = '-' if (gen_cat =='') else gen_cat
        
        
        
        
        
        
        newData.append([display_course, display_info, display_note, display_gen_cat, chance, '', department, course_ID, building, time, language, extra_enrollment])
        
        
        
        
    course_merged = pd.DataFrame(data=newData)
    course_merged.columns = ['課程\nCourse', '資訊\nInformation', '備註\nNote', '通識 GE', '選上機率\nChance', '重設\nReset', '系所 Department', '課程 Course ID', '教室大樓 Building', '時間 Time', '授課語言 Language', '加簽 Extra Enrollment']
    
    return course_merged