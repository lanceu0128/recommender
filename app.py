from flask import Flask, render_template, request, jsonify
import pandas as pd
from model import content_based_recommendations

app = Flask(__name__)
df = pd.read_csv("gamesdata_clean.csv", encoding="utf-8")


@app.route("/", methods=["POST"])
def index():
    if request.method == "POST":
        game_title = request.form["game_title"]
        game_title, recommendations = content_based_recommendations(
            game_title, df)

        return jsonify(status=200, game_title=game_title, recommendations=recommendations)


if __name__ == "__main__":
    app.run(debug=True)
