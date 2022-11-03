from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse
import datetime as dt
from celestial_bodies.settings import NASA_API_KEY, NASA_API_ASTEROIDS_LIST_ADDRESS,NASA_API_ASTEROIDS_LIST_DATE_ADDRESS


def asteroid_with_dates(request):
    if request.method == 'POST':
        complete_url = NASA_API_ASTEROIDS_LIST_DATE_ADDRESS+'?start_date='+ request.POST['start_date'] +'&end_date='+ request.POST['end_date'] +'&api_key='+NASA_API_KEY
        r = requests.get(complete_url)
        response_object = r.json()['near_earth_objects']
        asteroid_list=[]
        for i in response_object:
            asteroid_list.extend(response_object[i])
            pass
        context={'asteroid_list':asteroid_list}
        pass
    elif request.method == 'GET':
        context={}
        pass
    return render(request,'index.html',context)

def asteroid_details(request,asteroid_id):
    r= requests.get('http://api.nasa.gov/neo/rest/v1/neo/' + str(asteroid_id) +'?api_key=' + NASA_API_KEY)
    asteroid = r.json()
    get_last_five_approach_dates(asteroid)
    context = {
        'asteroid':asteroid,
        'last_5_dates':get_last_five_approach_dates(asteroid)
    }
    return render(request,'asteroid_details.html',context)

def get_last_five_approach_dates(asteroid):
    last_five_approach_data = []
    
    for data in asteroid['close_approach_data']:
        splitted_date = data['close_approach_date'].split('-')
        if dt.date(int(splitted_date[0]),int(splitted_date[1]),int(splitted_date[2])) < dt.date.today():
            last_five_approach_data.append(
                {
                    'close_approach_date': data['close_approach_date'],
                    'close_approach_date_full': data['close_approach_date_full'],
                    'miss_distance_in_km': data['miss_distance']['kilometers'],
                    'miss_distance_in_mi': data['miss_distance']['miles'],
                    'miss_distance_in_astro': data['miss_distance']['astronomical'],
                    'miss_distance_in_luna': data['miss_distance']['lunar'],
                    'relative_velocity_in_km_per_hour': data['relative_velocity']['kilometers_per_hour'],
                }
            )
            pass
        pass
    return last_five_approach_data[-5:]
