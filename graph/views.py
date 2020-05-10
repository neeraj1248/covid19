from django.shortcuts import render

# Create your views here.
def graph(request):
    import requests
    import json
    response = requests.get('https://api.covid19india.org/data.json')
    data = response.json()

    ls_totalconfirmed = []
    ls_totaldeceased = []
    ls_totalrecovered = []
    ls_date = []

    ls_dailyconfirmed = []
    ls_dailydeceased = []
    ls_dailyrecovered = []
    for j in data['cases_time_series']:
        ls_totalconfirmed.append(j['totalconfirmed'])
        ls_totaldeceased.append(j['totaldeceased'])
        ls_totalrecovered.append(j['totalrecovered'])
        ls_date.append(j['date'][0:6])

        ls_dailyconfirmed.append(j['dailyconfirmed'])
        ls_dailydeceased.append(j['dailydeceased'])
        ls_dailyrecovered.append(j['dailyrecovered'])
    #
    #
    # print("-----------------1---------------------------")
    # print(ls_date)
    # print("-----------------2---------------------------")
    # print(ls_totalconfirmed)
    # print("-----------------3---------------------------")
    # print(ls_totaldeceased)
    # print("-----------------4---------------------------")
    # print(ls_totalrecovered)
    return render(request, 'graph.html',{'key1':ls_date[39:],'key2':ls_totalconfirmed[39:],'key3':ls_totaldeceased[39:],'key4':ls_totalrecovered[39:],'key5':ls_dailyconfirmed[39:],'key6':ls_dailydeceased[39:],'key7':ls_dailyrecovered[39:],})
