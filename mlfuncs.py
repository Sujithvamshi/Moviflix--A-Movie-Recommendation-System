import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def cosinesim(name):
    df = pd.read_csv('model/features.csv')
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['overview'])
    sim = cosine_similarity(count_matrix)
    name = name.lower()
    df['title']=df['title'].str.lower()
    if name not in df['title'].unique():
        return ('Try Aboslute Spelling or it may not be in our database')
    else:
        i = df.loc[df['title']==name].index[0]
        mov_id = list(enumerate(sim[i]))
        mov_id = sorted(mov_id,key = lambda x:x[1],reverse=True)
        act_id = mov_id[0]
        mov_id = mov_id[1:11]
        rec_id = []
        for i in range(len(mov_id)):
            a = mov_id[i][0]
            rec_id.append(df['id'][a])
        return act_id,rec_id