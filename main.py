import json

from requests.models import codes

import raw_queries as Q
import q_variables
import header
import requests


url = "https://www.warcraftlogs.com/api/v2/client"
V = q_variables.variables
token = header.headers

q_variables.codeList.clear()

# The actual query to get the Roll the Bones outcomes. Exports them into rtbdata.json.

def filter_query():
    response = requests.post(url, json={'query': Q.filter_query, "variables": V}, headers = token)
    print(response.status_code)
    rtbdata = response.json()['data']['reportData']['report']['events']['data']
    #print(rtbdata)
    with open('rtbdataraw.json', 'a') as fp:
        json.dump(rtbdata, fp)
    q_variables.indexNum += 1
    print(f'indexNum: {q_variables.indexNum}')

# Fills "start" and "end" variables in variables dict with the startTime and endTime of a report. Requires reportID.

def get_start_and_end():
    response = requests.post(url, json={'query': Q.get_start_and_end, "variables": V}, headers = token)
    print(response.status_code)
    variableData = response.json()
    for i in variableData['data']['reportData']['report']['fights']:
        times = [i['startTime'],i['endTime']]
        q_variables.start = times[0]
        q_variables.end = times[1]

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

get_report_ids()    

def run_functions():
    i = 0
    while i < 99:
        get_start_and_end()
        q_variables.code = q_variables.codeList[q_variables.indexNum]
        V["code"] = q_variables.code
        V["start"] = q_variables.start
        V["end"] = q_variables.end
        filter_query()
        i += 1

run_functions()

with open('rtbdataraw.json', 'r') as infile, open('rtbdata.json', 'w') as outfile:
    temp = infile.read().replace("[", "").replace("]", "").replace("}{", "}, {")
    outfile.write(temp)

#with open('reportIDsraw.json', 'r') as infile, open('reportIDs.json', 'w') as outfile:
    #temp = infile.read().replace("[", "").replace("]", "").replace("}{", "}, {").replace("'", "")
    #outfile.write(temp)
   
r = requests.get(url, json={'query': Q.filter_query_two}, headers=header.headers)
r.text
print(q_variables.indexNum)


