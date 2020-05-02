from django.shortcuts import render

# Create your views here.
def dailyreport(request):
    import requests
    import json
    response = requests.get('https://api.covid19india.org/data.json')
    data = response.json()
    for i in data['statewise']:
        if i['statecode'] == 'TT':
            print('ok')
            act = i['active']
            con = i['confirmed']
            rec = i['recovered']
            deat = i['deaths']

            # dc = i['deltaconfirmed']
            # dd = i['deltadeaths']
            # dr = i['deltarecovered']
            # lup = i['lastupdatedtime']
            break;
        else:
            print('not ok')
    ls_dailyconfirmed = []
    ls_date = []
    for j in data['cases_time_series']:
        ls_dailyconfirmed.append(j['dailyconfirmed'])
        ls_date.append(j['date'][0:6])

    print(ls_dailyconfirmed)
    print(ls_date)

    return render(request,'dailyreport.html',{'key1':data['cases_time_series'],'key2':con,'key3':act,'key4':rec,'key5':deat,'key6':ls_dailyconfirmed,'key7':ls_date})
