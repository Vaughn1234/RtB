import json

import raw_queries as Q
import q_variables
import header
import requests

url = "https://www.warcraftlogs.com/api/v2/client"
V = q_variables.variables
token = header.headers


def filter_query():
    response = requests.post(url, json={'query': Q.filter_query_two, "variables": V}, headers = token)
    print(response.status_code)
    rtbdata = response.json()
    #print(rtbdata)
    with open('rtbdata.json', 'w') as fp:
        data_str = json.dump(rtbdata, fp)
    #json_data = json.loads(response.text)
    #print(json_data)
    #json_data = response.json()
    #with open('rtbdata.json') as f:
    #    data = json.load(f)
        #for (k, v) in data.items():
            #print("Key: " + k)
            #print("Value: " + str(v))
 

def get_start_and_end():
    response = requests.post(url, json={'query': Q.get_start_and_end, "variables": V}, headers = token)
    variableData = response.json()
    #print(variableData)
    print (variableData['data']['reportData']['report']['fights'])
    #print (variableData['data']['reportData']['report']['fights'])  
    """for i in response['data']['reportData']['report']:
        #if selection == i.get('name'):
        out=[i['startTime'],i['endTime'],i['encounterID']]
        print(out)
        V['start']=out[0]
        V['end']=out[1]
        V['EID']=out[2]
        print(V.start)
        return out"""


def get_report_ids():
    response = requests.post(url, json={'query': Q.get_report_ids}, headers = token)
    reportIDs = response.json()
    with open('reportIDs.json', 'w') as fp:
        data_str = json.dump(reportIDs, fp)

    



    
    

#get_start_and_end()
#get_report_ids()
filter_query()
r = requests.get(url, json={'query': Q.filter_query_two}, headers=header.headers)
r.text


