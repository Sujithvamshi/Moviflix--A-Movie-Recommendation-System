from flask import Flask,render_template
import json
import requests
from working import posters_list
movie_id = "8844"
apikey = "aa865550facea4479a134ae752aa82ef"
data = requests.get('https://api.themoviedb.org/3/discover/movie?api_key='+apikey+'&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate').text
json_data = json.loads(data)
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
    images,names = posters_list(json_data)
    length = len(images)
    return render_template('main.html',length= length,images=images,names = names)
if __name__ == '__main__':
    app.run(debug=True)
