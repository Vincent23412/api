import requests 

url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=CWB-1E39B8CB-0ED8-427C-9921-DADF005A3BAC&elementName=TEMP'
params = {
    'Authorization': 'CWB-1E39B8CB-0ED8-427C-9921-DADF005A3BAC'
}



# 發送HTTP GET請求
response = requests.get(url, params=params)

try :
    data = response.json()
    print(data)

except Exception as e :
    print(e)

