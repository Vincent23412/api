from flask import Flask, jsonify
import requests


app = Flask(__name__)
url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-093?Authorization=CWB-1E39B8CB-0ED8-427C-9921-DADF005A3BAC&locationId=F-D0047-003'
params = {
    'Authorization': 'CWB-1E39B8CB-0ED8-427C-9921-DADF005A3BAC'
}

info = {}


# 發送HTTP GET請求
response = requests.get(url, params=params)

try :
    data = response.json()
    #print(data)
    for i in range(len(data['records']['locations'][0]['location'])) :
        detail = data['records']['locations'][0]['location'][i]
        
        place = detail['locationName']
        start_time = detail['weatherElement'][0]['time'][0]['startTime']
        probility = detail['weatherElement'][0]['time'][0]['elementValue'][0]['value']
        temperature = detail['weatherElement'][1]['time'][0]['elementValue'][0]['value']
        wind = detail['weatherElement'][4]['time'][0]['elementValue'][0]['value']
        
        
        info[place] = {'start_time':start_time ,
                       'probility':probility,
                      'temperature':temperature,
                      'wind':wind
                      }

        
        
        
except Exception as e :
    print(e)



@app.route('/')
def ans():
    # res = {
    #     'place':place , 
    #     'start_time':start_time,
    #     'probility':probility
    # }
    return jsonify(info)

if __name__ == '__main__':
    app.run()