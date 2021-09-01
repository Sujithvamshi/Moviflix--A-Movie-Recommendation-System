import json
import requests

def poster_list(json_data):
    posters = []
    names=[]
    for i in json_data['results']:
        posters.append(i['poster_path'])
        names.append(i['title'])
    return posters,names

apikey = "aa865550facea4479a134ae752aa82ef"

def popular():
    data = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=aa865550facea4479a134ae752aa82ef&language=en-US&page=1').text
    pop_data = json.loads(data) 
    pop_im,pop_name=poster_list(pop_data)
    return pop_im,pop_name


def discover():
    response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key='+apikey+'&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate').text
    dis_data = json.loads(response)
    dis_im,dis_name=poster_list(dis_data)
    return dis_im,dis_name
def tester():
    response = requests.get('https://api.themoviedb.org/3/movie/latest?api_key=aa865550facea4479a134ae752aa82ef&language=en-US').text
    dis_data = json.loads(response)
    dis_im,dis_name=poster_list(dis_data)
    return dis_im,dis_name

def recommendations(movie_id):
    rec_im = []
    rec_name=[]
    for i in movie_id:
        data = requests.get('https://api.themoviedb.org/3/movie/'+str(i)+'?api_key='+apikey+'&language=en-US').text
        rec_data = json.loads(data)
        rec_im.append(rec_data['poster_path'])
        rec_name.append(rec_data['title'])
    return rec_im,rec_name
