
#* Author : eXit-guy
#* API : https://corona-stats.online

import time
import requests
import json
import dateutil.parser

line_url = 'https://notify-api.line.me/api/notify'

line_token = 'Enter your token'

line_headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+line_token}

def getDataFromWeb():
    return json.loads(requests.get('https://corona-stats.online/Thailand?format=json').text)

def main():
    while(True):
        try :
            response = getDataFromWeb()
            #print(response)
            report = 'Covid-19\nDev : eXit-Guy\nData : https://corona-stats.online\n\n'
            report += response['data'][0]['country'] + '\n';
            report += 'confirmed : ' + str(response['data'][0]['confirmed']) + '\n';
            report += 'recovered : ' + str(response['data'][0]['recovered']) + '\n';
            report += 'deaths : ' + str(response['data'][0]['deaths']) + '\n';
            #report += 'lastUpdated : ' + str(dateutil.parser.parse(response['data'][0]['lastUpdated']).strftime("%m/%d/%Y, %H:%M:%S %Z")) + '\n';
            print(report)
            r = requests.post(line_url, headers=line_headers , data = {'message':report})
            print(r.text)
        except:
            print('Something went wrong')
        time.sleep(43200) # 12 HR.

if __name__ == '__main__':
    main()