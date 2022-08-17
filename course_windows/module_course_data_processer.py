import pandas as pd
import re
import html



dep_list = {
    "AES"  : "AES  分環所",
    "AIIM" : "AIIM AI智造暨聯網產碩專班",
    "AMEV" : "AMEV 電動載具先進製造產碩",
    "ANTH" : "ANTH 人類所",
    "ANTU" : "ANTU 人類所與交大合作課程",
    "ASTR" : "ASTR 天文所",
    "BAI"  : "BAI  智慧生醫博士學位學程",
    "BME"  : "BME  醫工所",
    "BMES" : "BMES 醫環系",
    "CF"   : "CF   大學中文",
    "CHE"  : "CHE  化工系",
    "CHEM" : "CHEM 化學系",
    "CL"   : "CL   中文系",
    "CLC"  : "CLC  華語中心",
    "CLU"  : "CLU  中文系與交大合作課程",
    "COM"  : "COM  通訊所",
    "CS"   : "CS   資工系",
    "CSR"  : "CSR  半導體研究學院",
    "DL"   : "DL   遠距課(同步/非同步)",
    "DMS"  : "DMS  醫科系",
    "E"    : "E    工學院",
    "ECON" : "ECON 經濟系",
    "EE"   : "EE   電機系",
    "EECS" : "EECS 電資院學士班",
    "EMBA" : "EMBA 高階經營管理碩士專班",
    "EMD"  : "EMD  EMBA雙聯學位學程",
    "EMIM" : "EMIM 智慧製造高階在職專班",
    "EMM"  : "EMM  EMBA亞太馬國境外專班",
    "EMS"  : "EMS  EMBA深圳境外專班",
    "ENE"  : "ENE  電子所",
    "ESS"  : "ESS  工科系",
    "EST"  : "EST  環境博士學位學程",
    "ESTU" : "ESTU 環境博士學程與台聯大",
    "FL"   : "FL   外語系",
    "FLU"  : "FLU  外語系與交大合作課程",
    "GE"   : "GE   通識中心",
    "GEC"  : "GEC  通識核心",
    "GEU"  : "GEU  通識中心與交大合作課",
    "GLLB" : "GLLB 學士後法律學士學位學",
    "GOM"  : "GOM  全球營運管理碩士學程",
    "GPTS" : "GPTS 台研教專班",
    "HBA"  : "HBA  健康經管碩士在職專班",
    "HIS"  : "HIS  歷史所",
    "HSS"  : "HSS  人社院學士班",
    "HSSU" : "HSSU 人社學士班與交大合作",
    "IACS" : "IACS 亞際文化碩士學程",
    "IACU" : "IACU 亞際文化與台聯大合作",
    "IBP"  : "IBP  清華學院國際學士班",
    "ICMS" : "ICMS 計科所",
    "IEEM" : "IEEM 工工系",
    "IEM"  : "IEM  工工在職專班",
    "IIS"  : "IIS  資安所",
    "IMBA" : "IMBA IMBA碩士班",
    "IMCT" : "IMCT 資通訊控制與熱流專班",
    "IMII" : "IMII AI製造與物聯網產碩班",
    "IMS"  : "IMS  跨院國際碩士學位",
    "IPE"  : "IPE  工學院學士班",
    "IPHD" : "IPHD 跨院國際博士學位",
    "IPIM" : "IPIM 智慧生產製造產碩專班",
    "IPNS" : "IPNS 原科院學士班",
    "IPT"  : "IPT  光電所",
    "IPTH" : "IPTH 清華學院學士班",
    "ISA"  : "ISA  資應所",
    "ISS"  : "ISS  服科所",
    "JAC"  : "JAC  藝術學院",
    "JAD"  : "JAD  藝設系",
    "JADN" : "JADN 藝設系在職專班",
    "JANT" : "JANT 科技藝術研究所",
    "JITA" : "JITA 藝術學院學士班",
    "JMU"  : "JMU  音樂系",
    "JMUN" : "JMUN 音樂系在職專班",
    "KCSN" : "KCSN 學前特教在職專班",
    "KEC"  : "KEC  環文系",
    "KECN" : "KECN 環文系在職專班",
    "KEE"  : "KEE  幼教系",
    "KEEN" : "KEEN 幼教系在職專班",
    "KEL"  : "KEL  教科系",
    "KELN" : "KELN 教科系在職專班",
    "KENI" : "KENI 英教系",
    "KHCT" : "KHCT 竹師教育學院",
    "KIPE" : "KIPE 竹師教育學院學士班",
    "KLST" : "KLST 學科所",
    "KMS"  : "KMS  數理所",
    "KMSN" : "KMSN 數理所在職專班",
    "KPC"  : "KPC  心諮系",
    "KPCN" : "KPCN 心諮系在職專班",
    "KPE"  : "KPE  體育系 (已停用 Deactivate)",
    "KSEN" : "KSEN STEAM碩士在職專班",
    "KSN"  : "KSN  新加坡心諮碩專班",
    "KSPE" : "KSPE 特教系",
    "KSS"  : "KSS  運科系",
    "KSSN" : "KSSN 運科系在職專班",
    "KTLT" : "KTLT 臺語所",
    "KWEN" : "KWEN 華德福碩士在職學程",
    "LANG" : "LANG 英語教育中心(110起)",
    "LE"   : "LE   語文中心",
    "LING" : "LING 語言所",
    "LS"   : "LS   生科系",
    "LSBI" : "LSBI 生技產業博士學程",
    "LSBS" : "LSBS 生資所",
    "LSBT" : "LSBT 生技所",
    "LSC"  : "LSC  生科院",
    "LSIN" : "LSIN 神經科學博士學程",
    "LSIP" : "LSIP 生科院學士班",
    "LSMC" : "LSMC 分生所",
    "LSMM" : "LSMM 分醫所",
    "LSSN" : "LSSN 系神所",
    "LST"  : "LST  科法所",
    "MATH" : "MATH 數學系",
    "MATU" : "MATU 數學系與交大合作",
    "MBA"  : "MBA  MBA專班",
    "MFB"  : "MFB  財金碩士專班",
    "MI"   : "MI   國防教育課",
    "MPM"  : "MPM  公共政策與管理專班",
    "MS"   : "MS   材料系",
    "NEMS" : "NEMS 奈微所",
    "NES"  : "NES  核工所",
    "NUCL" : "NUCL 原科院",
    "PE"   : "PE   體育室",
    "PE1"  : "PE1  大一體育",
    "PE3"  : "PE3  體育(校隊)",
    "PFMI" : "PFMI 前瞻產博學程",
    "PHIL" : "PHIL 哲學所",
    "PHYS" : "PHYS 物理系",
    "PHYU" : "PHYU 物理系與交大合作課程",
    "PME"  : "PME  動機系",
    "PMED" : "PMED 精準醫療博士學位學程",
    "QF"   : "QF   計財系",
    "RDDM" : "RDDM 半導體元件及製程專班",
    "RDIC" : "RDIC 積體電路設計專班",
    "RDPE" : "RDPE 產業研發碩士電力電子",
    "S"    : "S    理學院",
    "SCI"  : "SCI  理學院學士班",
    "SL"   : "SL   華文所",
    "SLS"  : "SLS  先進光源科技學位學程",
    "SNHC" : "SNHC 社群人智國際學程",
    "SOC"  : "SOC  社會所",
    "STAT" : "STAT 統計所",
    "STAU" : "STAU 統計所與交大合作課程",
    "TE"   : "TE   師培中心(中等教程)",
    "TEE"  : "TEE  師培中心(國小教程)",
    "TEG"  : "TEG  師培中心(一般課程)",
    "THC"  : "THC  清華學院",
    "THSM" : "THSM 學士後醫學系",
    "TIGP" : "TIGP 國際研究生學程",
    "TL"   : "TL   台文所",
    "TM"   : "TM   科管所",
    "TSE"  : "TSE  台北政經學院",
    "UPMT" : "UPMT 科管院學士班",
    "UPPP" : "UPPP 光電博士學程",
    "VA"   : "VA   合校過渡單位",
    "VGE"  : "VGE  南大校區原系統通識課",
    "W"    : "W    W課號課程 Interschool Courses",
    "WH"   : "WH   跨系統,台聯大&互惠課",
    "WW"   : "WW   陽明交大課程",
    "WZ"   : "WZ   外校課程",
    "X"    : "X    X抵免課程",
    "XA"   : "XA   抵免課程(大)",
    "XZ"   : "XZ   抵免課程(研)",
    "YZ"   : "YZ   課務組專用",
    "ZY"   : "ZY   服務學習"
}










def course_data_processer(data_folder_path, global_semester):
    
    

    course_data_df = pd.read_csv(data_folder_path + global_semester + '_course_data_downloaded.csv')

    
    
    newData = list()
        
    for row in range(0, course_data_df.shape[0]):
        # --------------------------------------------------------------------------------------- (col. 10) course_cancel 停開直接跳過
        course_cancel = course_data_df.iloc[row,10]
        if course_cancel == '停開':
            continue
        
        
        # --------------------------------------------------------------------------------------- (col. 0) course_ID_full_orig  -> course_ID, department
        course_ID_full_orig = course_data_df.iloc[row,0]
        
        course_ID = course_ID_full_orig.replace('  ', ' ')
        course_ID = course_ID.replace('  ', ' ')
        if course_ID.count(' ') == 0:
            course_ID = course_ID[:-6] + ' ' + course_ID[-6:]
        course_ID = course_ID[5:]
        
        course_num = course_ID[:-2].replace(' ', '')
        
        
        
        department = dep_list.get( course_ID[:-7] , 'ERROR' )
        
        
        # --------------------------------------------------------------------------------------- (col. 1) course_title_zh, (col. 2) course_title_eng
        course_title_zh = course_data_df.iloc[row,1]
        course_title_eng = course_data_df.iloc[row,2] if (course_data_df.iloc[row,2] != ' ') else  '--'
        
        
        # --------------------------------------------------------------------------------------- (col. 3) credit_unit
        credit_unit = course_data_df.iloc[row,3]
        
        
        # --------------------------------------------------------------------------------------- (col. 4) limit
        limit = '--' if ( pd.isna(course_data_df.iloc[row,4]) ) else int(course_data_df.iloc[row,4])
        
        
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
        elif course_data_df.iloc[row,7] == '人文學領域 Elective GE course: Humanities':
            gen_cat = '人文 Humanities'
        elif pd.isna(course_data_df.iloc[row,7]):
            gen_cat = '--'
        else:
            gen_cat = 'ERROR'
            
            
            
        
        # --------------------------------------------------------------------------------------- (col. 8) language
        if course_data_df.iloc[row,8] == '中':
            language = '中文 ZH'
        elif course_data_df.iloc[row,8] == '英':
            language = '英文 EN'
        else:
            language = 'other'
            
    
        # --------------------------------------------------------------------------------------- (col. 11) room_and_time_orig -> room_and_time_split(room,time,room,time...), time, building
        if pd.isna(course_data_df.iloc[row,11]):
            room_and_time_orig = '--'
            time = '--'
            building ='--'
        else:
            room_and_time_orig = course_data_df.iloc[row,11]
            room_and_time_split = re.split('\t|\n', course_data_df.iloc[row,11] )
            time = ''
            building =''
            for i in range(0, len(room_and_time_split)-1):
                if i%2 == 1:
                    time = time + room_and_time_split[i]
                else:
                    if ( not ( ( ord(room_and_time_split[i][-1])>=48 and ord(room_and_time_split[i][-1])<=57 ) or ( ord(room_and_time_split[i][-1])>=65 and ord(room_and_time_split[i][-1])<=90 ) or room_and_time_split[i][-1].isdigit() ) ):
                        if building == '':
                            building = building + room_and_time_split[i]
                        else:
                            building = building + ' ' + room_and_time_split[i]
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
        instructor = '--' if ( pd.isna(course_data_df.iloc[row,12]) ) else course_data_df.iloc[row,12][:-1]
        instructor = html.unescape(instructor)
        
        # -------------------------------------------------------------------------------------------------------------------------------------------------- display_note
        # --------------------------------------------------------------------------------------- (col. 9) memo (備註)
        memo = course_data_df.iloc[row,9] if (course_data_df.iloc[row,9] != ' ' and (not pd.isna(course_data_df.iloc[row,9]) ) ) else  '--'
        
        
    
        # --------------------------------------------------------------------------------------- (col. 13) prerequisite
        if ( pd.isna(course_data_df.iloc[row,13]) ):
            prerequisite = '--'
        else :
            prerequisite = course_data_df.iloc[row,13].replace('<div>', '').replace('<br>', '').replace('<BR>', '').replace('</div>', '').replace('  ', '')[1:]
        
        # --------------------------------------------------------------------------------------- (col. 14) limitation        
        if ( pd.isna(course_data_df.iloc[row,14]) ):
            limitation = '--'
        else :
            limitation = course_data_df.iloc[row,14]
        
        # --------------------------------------------------------------------------------------- (col. 15) speciality        
        if ( pd.isna(course_data_df.iloc[row,15]) ):
            speciality = '--'
        else :
            speciality = course_data_df.iloc[row,15].replace('\t', '/').replace('(第一專長)', '(一)').replace('(第二專長)', '(二)')
        
        
        # --------------------------------------------------------------------------------------- (col. 16) program        
        if ( pd.isna(course_data_df.iloc[row,16]) ):
            program = '--'
        else :
            program = course_data_df.iloc[row,16]
        
        
        # --------------------------------------------------------------------------------------- (col. 17) extra_enrollment
        if(course_data_df.iloc[row,17]=='《不接受加簽 No extra selection》'):
            extra_enrollment = 'X 不接受 Not Allowed'
        elif(pd.isna(course_data_df.iloc[row,17])):
            extra_enrollment = 'O 接受 Allowed'
        else:
            extra_enrollment = 'ERROR'
        
        # --------------------------------------------------------------------------------------- (col. 18) required_or_elective        
        if ( pd.isna(course_data_df.iloc[row,18]) ):
            required_or_elective = '--'
        else :
            required_or_elective = course_data_df.iloc[row,18].replace('  ', '').replace(' ', '').replace('\t', '/')[:-1]
        
        #                0                    1          2       3           4                5                 6            7      8         9        10        11                  12    13         14         15     16           17          18           19      20                21
        newData.append([course_ID_full_orig, course_ID, course_num, department, course_title_zh, course_title_eng, credit_unit, limit, new_only, gen_cat, language, room_and_time_orig, time, building, instructor, memo, prerequisite, limitation, speciality, program, extra_enrollment, required_or_elective])
        
    # --------------------------------------------------------------------------------------- end of for loop
    
    course_data_processed_df = pd.DataFrame(data=newData)
    course_data_processed_df.columns = ['course_ID_full_orig', 'course_ID', 'course_num', 'department', 'course_title_zh', 'course_title_eng', 'credit_unit', 'limit', 'new_only', 'gen_cat', 'language', 'room_and_time_orig', 'time', 'building', 'instructor', 'memo', 'prerequisite', 'limitation', 'speciality', 'program', 'extra_enrollment', 'required_or_elective']
    
    course_data_processed_df.to_csv(data_folder_path + global_semester + '_course_data_processed.csv', index=False)