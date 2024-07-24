from django.shortcuts import render
import requests
from django.http import JsonResponse

# Create your views here.
def call_external_api(request, item_id):
    url = f'http://127.0.0.1:8000/api/items/{item_id}'

    # make the get req
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        datas=[]
        datas.append({
            'id': data['id'],
            'name': data['name'],
            'description': data['description']
        })

        return render(request, 'frontend/display.html', {"datas": datas})

    else:
        return JsonResponse({'error': 'Failed to fetch data from API'}, status=response.status_code)
    

def call_all_items(request):
    url = 'http://127.0.0.1:8000/api/items'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # datasList = []
        # for content in data:
        #     ContentList = {
        #         'id': content['id'],
        #         'name': content['name'],
        #         'description': content['description']
        #     }
        #     datasList.append(ContentList)

        return render(request, 'frontend/display-all.html', {'data': data })
    else:
        return JsonResponse({'error': 'Failed to fetch data from API'}, status=response.status_code)