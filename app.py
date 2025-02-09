from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

song_rec = pickle.load(open('model/song_list.pkl', 'rb'))  # our dataframe
similarity = pickle.load(open('model/similarity.pkl', 'rb'))
print(song_rec)

def get_recommendations(song_name):
    if song_name not in song_rec['song_name'].values:
        return []
    
    idx = song_rec[song_rec['song_name'] == song_name].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    
    recommended_songs = []
    for m_id in distances[1:6]:  # Top 5 recommendations
        recommended_songs.append(song_rec.iloc[m_id[0]]['song_name'])
    
    return recommended_songs

@app.route("/", methods=["GET", "POST"])
def home():
    sample_songs = song_rec['song_name'].sample(5).tolist()  # Select 10 random songs for testing

    if request.method == "POST":
        song_name = request.form["song_name"]
        recommendations = get_recommendations(song_name)
        return render_template("results.html", song_name=song_name, recommendations=recommendations, songs=sample_songs)
    
    return render_template("index.html", songs=sample_songs)


if __name__ == "__main__":
    app.run(debug=True)
