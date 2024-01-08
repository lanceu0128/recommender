from flask import Flask, request, jsonify
import pandas as pd
from model import content_based_recommendations

app = Flask(__name__)
df = pd.read_csv("gamesdata_clean.csv", encoding="utf-8")


@app.route("/", methods=["GET"])
def index():
    try:
        if request.method == "GET":
            data = request.get_json()
            game_title = data.get("game_title")
            game_title, recommendations = content_based_recommendations(game_title, df)

            recommendations_json = recommendations.to_dict(orient='records')
            return jsonify(status=200, game_title=game_title, recommendations=recommendations_json)
    except Exception as e:
        return jsonify(status=500, error=str(e))


if __name__ == "__main__":
    app.run(debug=True)
