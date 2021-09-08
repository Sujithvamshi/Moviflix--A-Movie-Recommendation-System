from flask import Flask,render_template,request
from requests.api import post
import homefn
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def cosinesim(name):
    df = pd.read_csv('model/features.csv')
    cv = CountVectorizer(max_features = 5000, stop_words = 'english')
    vectors = cv.fit_transform(df['tags']).toarray()
    similarity = cosine_similarity(vectors)
    name = name.lower()
    df['title']=df['title'].str.lower()
    if name not in df['title'].unique():
        return ('Try Aboslute Spelling or it may not be in our database')
    else:
        i = df.loc[df['title']==name].index[0]
        mov_id = list(enumerate(similarity[i]))
        mov_id = sorted(mov_id,key = lambda x:x[1],reverse=True)
        mov_id = mov_id[0:11]
        rec_id = []
        for i in range(len(mov_id)):
            a = mov_id[i][0]
            rec_id.append(df['id'][a])
        return rec_id

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    dis_im,dis_name = homefn.discover()
    pop_im,pop_name = homefn.popular()
    length = len(dis_im)
    return render_template(
        'main.html',length= length,dis_im=dis_im,dis_name = dis_name,
        pop_im=pop_im,pop_name=pop_name)

        
@app.route("/movieinfo",methods=['GET','POST'])
def movieinfo():
    movie_name = None
    return render_template('movieinfo.html',movie_name = movie_name)


@app.route("/predict",methods=['GET','POST'])
def predict():
    movie_name = request.form.get('movie')
    cos_id = cosinesim(movie_name)
    movie_id = cos_id[0]
    movie_data = homefn.movie_info(movie_id)
    cos_id = cos_id[1:]
    length = len(cos_id)
    rec_im,rec_name = homefn.recommendations(cos_id)
    if type(cos_id)==type('str'):
        return render_template('predict.html',length=length,movie_name=movie_name,
        rec_im=[''],rec_name=[''],message=cos_id,movie_data={'':''},backdrop_path = "https://image.tmdb.org/t/p/original"+movie_data['backdrop_path'])
    else :
        if type(movie_data['backdrop_path']) == type(None):
            return render_template(
                'predict.html',length=length,movie_name=movie_name,
                rec_im=rec_im,rec_name=rec_name,movie_data=movie_data,message='',backdrop_path = "/static/no-image-available-icon-photo-camera-flat-vector-illustration-132483141.jpeg",
                mov_len=len(movie_data['genres']),poster_path = "/static/no-image-available-icon-photo-camera-flat-vector-illustration-132483141.jpeg")
        else:
            return render_template(
                'predict.html',length=length,movie_name=movie_name,
                rec_im=rec_im,rec_name=rec_name,movie_data=movie_data,message='',backdrop_path = "https://image.tmdb.org/t/p/original"+movie_data['backdrop_path'],
                mov_len=len(movie_data['genres']),
                poster_path = "https://image.tmdb.org/t/p/original"+movie_data['poster_path'])


if __name__ == '__main__':
    app.run(debug=True)