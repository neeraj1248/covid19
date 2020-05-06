from django.shortcuts import render

# Create your views here.
def state_input (request):
    import requests
    import json
    response = requests.get('https://api.covid19india.org/state_district_wise.json')
    data = response.json()
    ls = []
    for i in data.keys():
        ls.append(i)

    # print(ls)
    # print("-------------------------------------------------------------------------")
    # print(ls.sort())
    # print(len(ls))
    # print(ls)
    ls.sort()



    if request.method == "POST":
        rel =  request.POST.get('selectinp')
        # print(rel)

        ls_dict = []

        for i in data[rel]['districtData']:
            ls_dict.append(i)

        list_dictrict_data = []
        ls_graph_active = []

        ls_graph_district = ls_dict

        for i in ls_dict:
            dic = {}
            # print(i,' - ',data[rel]['districtData'][i]['active'])
            dic['dictrict'] = i
            dic['confirmed'] = data[rel]['districtData'][i]['confirmed']
            dic['active'] = data[rel]['districtData'][i]['active']
            ls_graph_active.append(data[rel]['districtData'][i]['active'])          #Append into list for the Graph data Purpose.
            dic['recovered'] = data[rel]['districtData'][i]['recovered']
            dic['deaths'] = data[rel]['districtData'][i]['deceased']
            dic['deltaconfirmed'] = data[rel]['districtData'][i]['delta']['confirmed']
            dic['deltarecovered'] = data[rel]['districtData'][i]['delta']['recovered']
            dic['deltadeaths'] = data[rel]['districtData'][i]['delta']['deceased']

            list_dictrict_data.append(dic)

        # print(list_dictrict_data)
        final_data = {}
        final_data['case'] = list_dictrict_data
        # print(final_data)



        response2 = requests.get('https://api.covid19india.org/data.json')
        data2 = response2.json()

        # print(data2['statewise'])
        for l in data2['statewise']:
            if l['state'] == rel:
                sc = l['confirmed']
                sa = l['active']
                sr = l['recovered']
                sd = l['deaths']

                sdc = l['deltaconfirmed']
                sdr = l['deltarecovered']
                sdd = l['deltadeaths']

        return render(request,'state_input_report.html',{'key1':rel,'key3':final_data['case'],'key4':sc,'key5':sa,'key6':sr,'key7':sd,'key8':sdc,'key9':sdr,'key10':sdd,'key11':ls_graph_active,'key12':ls_graph_district})
    else:
        return render(request,'state_input.html',{'key1':ls})

# def state_district_wise_report(request):
#     return render(request,'state_input_report.html')
