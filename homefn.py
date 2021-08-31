import json
import requests
apikey = "aa865550facea4479a134ae752aa82ef"
def poster_list(json_data):
    posters = []
    names=[]
    for i in json_data['results']:
        posters.append(i['poster_path'])
        names.append(i['title'])
    return posters,names
def discover():
    data = requests.get('https://api.themoviedb.org/3/discover/movie?api_key='+apikey+'&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate').text
    dis_data = json.loads(data)
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
