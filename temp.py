import json
import requests
from homefn import poster_list
data = requests.get('https://api.themoviedb.org/3/movie/863?api_key=aa865550facea4479a134ae752aa82ef&language=en-US').text
rec_data = json.loads(data)
print(rec_data['title'])