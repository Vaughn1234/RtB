import json

import raw_queries as Q
import q_variables
import header
import requests


url = "https://www.warcraftlogs.com/api/v2/client"
V = q_variables.variables
token = header.headers


# The actual query to get the Roll the Bones outcomes. Exports them into rtbdata.json.

def filter_query():
    response = requests.post(url, json={'query': Q.filter_query, "variables": V}, headers = token)
    print(response.status_code)
    rtbdata = response.json()
    #print(rtbdata)
    with open('rtbdata.json', 'w') as fp:
        data_str = json.dump(rtbdata, fp)
    q_variables.indexNum += 1
    #json_data = json.loads(response.text)
    #print(json_data)
    #json_data = response.json()
    #with open('rtbdata.json') as f:
    #    data = json.load(f)
        #for (k, v) in data.items():
            #print("Key: " + k)
            #print("Value: " + str(v))
    print(f'indexNum: {q_variables.indexNum}')
    print(q_variables.code)
    print(q_variables.start)
    print(q_variables.end)

# Fills "start" and "end" variables in variables dict with the startTime and endTime of a report. Requires reportID.

def get_start_and_end():
    response = requests.post(url, json={'query': Q.get_start_and_end, "variables": V}, headers = token)
    print(response.status_code)
    variableData = response.json()
    #print(variableData)
    #print (variableData['data']['reportData']['report']['fights'][2])
    #print (variableData['data']['reportData']['report']['fights'])  
    for i in variableData['data']['reportData']['report']['fights']:
        times = [i['startTime'],i['endTime']]
        q_variables.start = times[0]
        q_variables.end = times[1]
        print(q_variables.start)
        print(q_variables.end)
        #if selection == i.get('name'):
        #out=[i['startTime'],i['endTime']]
        #print(out)
        #V[1]=out[0]
        #V[2]=out[1]
        #print(V[1])
        #print(V[2])
        #return out

# Gets the reportID of 100 reports that include an Outlaw Rogue from the EU server and exports them into reportIDs.json.

def get_report_ids():
    response = requests.post(url, json={'query': Q.get_report_ids}, headers = token)
    print(response.status_code)
    reportData = response.json()
    reportIDs = reportData['data']['worldData']['encounter']['characterRankings']['rankings']
    indexNum = 0
    listIDs = []
    #for i in reportIDs[indexNum]['report']['code']:
        #indexNum += 1
        #listIDs.append(i)
    #print(listIDs)
    indexNum = 0
    listIDs = []
    i = 0
    while i < 99:
        i += 1
        indexNum += 1
        listIDs.append(reportIDs[indexNum]['report']['code'])
    q_variables.codeList += listIDs
    with open('reportIDs.json', 'w') as fp:
        data_str = json.dump(reportIDs, fp)
    #print(q_variables.variables)

get_report_ids()    

def run_functions():
    i = 0
    while i < 5:
        get_start_and_end()
        filter_query()
        i += 1
        q_variables.start = int
        q_variables.end = int
        q_variables.code = q_variables.codeList[q_variables.indexNum]
        q_variables.variables = {
            "code": q_variables.code,
            "start": q_variables.start,
            "end": q_variables.end,
    #"filterExpression": filterExpression,
            }


run_functions()
   
    
#get_report_ids()
#get_start_and_end()
#filter_query()
r = requests.get(url, json={'query': Q.filter_query_two}, headers=header.headers)
r.text
print(q_variables.indexNum)


