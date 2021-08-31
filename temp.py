import json
import requests
import working
apikey = "aa865550facea4479a134ae752aa82ef"
data = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=aa865550facea4479a134ae752aa82ef&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate').text
json_data = json.loads(data)
a,b=working.posters_list(json_data)
print(b)