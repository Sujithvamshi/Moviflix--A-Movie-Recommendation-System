import json
import requests
apikey = "aa865550facea4479a134ae752aa82ef"
data = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=aa865550facea4479a134ae752aa82ef&language=en-US&page=1').text
pop_data = json.loads(data)
print(pop_data['results'][0]['poster_path'])