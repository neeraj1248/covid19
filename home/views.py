from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.
def index(request):
    import requests
    import json
    response = requests.get('https://api.covid19india.org/data.json')
    data = response.json()
    for i in data['statewise']:
        if i['statecode'] == 'TT':
            print('ok')
            act = i['active']
            con = i['confirmed']
            deat = i['deaths']
            dc = i['deltaconfirmed']
            dd = i['deltadeaths']
            dr = i['deltarecovered']
            rec = i['recovered']
            lup = i['lastupdatedtime']
            break;
        else:
            print('not ok')

    ls_statecode = []
    ls_activecase =[]
    for i in data['statewise']:
        ls_statecode.append(i['statecode'])
        ls_activecase.append(i['active'])
    ls_statecode = ls_statecode[1:]
    ls_activecase = ls_activecase[1:]
    return render(request,'index.html',{'key1':data['statewise'][1:],'key2':con,'key3':act,'key4':rec,'key5':deat,'key6':dc,'key7':dr,'key8':dd,'key9':ls_statecode,'key10':ls_activecase})
