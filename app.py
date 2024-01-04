from flask import Flask, render_template, request, jsonify
import pandas as pd
from model import content_based_recommendations
import awsgi

app = Flask(__name__)

# Load your DataFrame
df = pd.read_csv("gamesdata_clean.csv", encoding="utf-8")


@app.route("/", methods=["POST"])
def index():
    if request.method == "POST":
        game_title = request.form["game_title"]
        game_title, recommendations = content_based_recommendations(
            game_title, df)

        return jsonify(status=200, game_title=game_title, recommendations=recommendations)

    #     if recommendations.empty:
    #         # No recommendations found for the entered game title
    #         message = f"No recommendations found for '{game_title}'."
    #         return render_template("index.html", game_title=game_title, message=message)
    #     else:
    #         return render_template("index.html", game_title=game_title, recommendations=recommendations)

    # return render_template("index.html")


def handler(event, context):
    return awsgi.response(app, event, context)


if __name__ == "__main__":
    app.run(debug=True)
