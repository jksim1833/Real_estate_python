import pandas as pd
series_ex= pd.Series([100,90,120,110,105],index =['월','화','수','목','금'])
#'print series only'
print(series_ex)

#print series by index'
print(series_ex['월'])

print(series_ex[series_ex >100])