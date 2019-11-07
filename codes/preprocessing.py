import pandas as pd
import xlwings as xw

def KBpriceindex_preprocessing(path,data_type):
    wb = xw.Book(path)
    sheet = wb.sheets[data_type]
    row_num = 410
    data_range = 'A2:GE'+str(row_num)
    raw_data = sheet[data_range].options(pd.DataFrame, index=False, header=True).value

    bignames = '서울 대구 부산 대전 광주 인천 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주도 6개광역시 5개광역시 수도권 기타지방 구분 전국'
    bignames_list = bignames.split(' ')
    big_col = list(raw_data.columns)
    small_col = list(raw_data.iloc[0])

    for num,gu_data in enumerate(small_col):
        if gu_data == None:
            small_col[num] = big_col[num]
        check = num
        while True:
            if big_col[check] in bignames_list:
                big_col[num] = big_col[check]
                break
            else:
                check = check - 1


    big_col[129]= '경기'
    big_col[130]= '경기'
    big_col[185]= '서귀포'

    raw_data.columns = [big_col,small_col]
    new_col_data = raw_data.drop([0,1])

    index_list = list(new_col_data['구분']['구분'])
    new_index =[]

    for num, raw_index in enumerate(index_list):
        temp = str(raw_index).split('.')
        if int(temp[0])>12:
            if len(temp[0]) == 2:
                new_index.append('19'+temp[0]+'.'+temp[1])
            else:
                new_index.append(temp[0]+'.'+temp[1])
        else:
            new_index.append(new_index[num-1].split('.')[0]+'.'+temp[0])

    new_col_data.set_index(pd.to_datetime(new_index),inplace = True)
    cleaned_data = new_col_data.drop(('구분','구분'),axis=1)
    return cleaned_data

new_path = r'/Users/simjaegwang/Desktop/kbdatas.xls'
new_data = '매매종합'
print(KBpriceindex_preprocessing(new_path,new_data))