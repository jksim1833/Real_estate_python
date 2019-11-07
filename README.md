# Real_estate_python_Jason Sim

위키북스 파이썬을 화용한 부동산 데이터 분석 활용해보기
-----------------------------------------
Daily report 을 본 파일로 정리해보고자 합니다.
-----------------------------------------
1. Day1 > Pandas 이해하기
    - series 함수를 사용해 1차원 datasheet 만들기(pd.Series([데,이,터,값])
    - index 혹은 Value를 사용하여 값 정리하기
    - dataframe을 사용해 2차원 datasheet 만들기(pd.DataFrame('칼럼이름':[데,이,터,값],index = [@,@,@,@])
    - dataframe_ex['칼럼이름']으로 인덱스 와 데이터로 정리하기
    - datasheet_series.sort_values(ascending=False) => 내림차순
    - datasheet_dataframe.sort_values(by = '칼럼이름',ascending=False) => 내림차순
1. Day2 > Data preprocessing 하기
    - Encryted 된 엑셀을 xlwings 모듈을 사용해 Data preprocessing 하기
    - xlwings 모듈 활용중 jupyter notebook 과 terminal , Vs code간 파이썬 버전이 동일하지 않아서 햇갈렸지만 /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7 로 통일
    - 두가지 임시변수 (index,data)를 가질 수 있는 enumerate 함수 배우고 활용하기
    - Original RAW data 추출 sheet[data_range].options(pd.DataFrame, index = False, header = True).value
    - split 함수 복습
    - @@.set_index & @@.colums & @@.drop 을 통한 데이터프레임 정리
