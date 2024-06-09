from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle

#loading models

df = pickle.load(open('df.pkl', 'rb'))  #read binary mode mein we are taking
similarity = pickle.load(open('similarity.pkl','rb'))


def recommendation(song):  # we made a function jismein song aa raha hoga
    idx = df[df['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=False,
                       key=lambda x: x[1])  # isse we will get the whole list/vector and last mein hum sorting kar denge
    songs = []  # we created an empty list jismein sab ultimately aa raha hoga
    for i in distances[1:21]:
        songs.append(df.iloc[i[0]].song)

    return songs
#flask app creating

app = Flask(__name__)
#paths
@app.route('/')
def index():
    names = list(df['song'].values)
    return render_template('index.html',name=names)
@app.route('/recom',methods=['POST'])
def mysong():
    user_song = request.form['names']
    songs = recommendation(user_song)

    #sending these songs to my html template
    return render_template('index.html', songs=songs)

# python kaa main bana kar usmein flask ko run karaya jaega ab
if __name__ == "__main__":
    app.run(debug=True)