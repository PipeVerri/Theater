from flask import Flask
import recommender

app = Flask(__name__)


@app.route("/recommended")
def recommended_movies():
    return recommender.get_popular_media()


app.run(debug=True)
