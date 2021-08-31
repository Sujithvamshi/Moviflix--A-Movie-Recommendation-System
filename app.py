from flask import Flask,render_template,request
import homefn
from mlfuncs import cosinesim,euclidsim
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
    dis_im,dis_name = homefn.discover()
    length = len(dis_im)
    return render_template(
        'main.html',length= length,dis_im=dis_im,dis_name = dis_name
        )
@app.route("/predict",methods=['GET','POST'])
def predict():
    movie_name = request.form.get('movie')
    cos_id = cosinesim(movie_name)
    euc_id = euclidsim(movie_name)
    length = len(cos_id)
    rec_im,rec_name = homefn.recommendations(cos_id) 
    if type(cos_id)==type('str') or type(euc_id)==type('str'):
        return render_template('predict.html',length=length,movie_name=movie_name,rec_im=[''],rec_name=[''],message=cos_id)
    else :
        return render_template('predict.html',length=length,movie_name=movie_name,rec_im=rec_im,rec_name=rec_name,message='')
if __name__ == '__main__':
    app.run(debug=True)
