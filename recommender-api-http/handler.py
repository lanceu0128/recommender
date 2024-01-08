import pandas as pd
import json
from model import content_based_recommendations

df = pd.read_csv("gamesdata_clean.csv", encoding="utf-8")


def hello(event, context):
    originalEvent = event
    try:
        data = json.loads(event['body'])

        # return error if no event
        if 'game_title' not in data:
            response = {"statusCode": 400, "body": json.dumps({"error": "Error: 'game_title' is missing in the event."})}
            return response

        # call content_based_recommendations
        title = data['game_title']
        title, recommendations_df = content_based_recommendations(title, df)

        # prepare response body
        body = {
            "message": f"Recommendations for {title}",
            "recommendations": recommendations_df.to_dict(orient='records'),
        }

        response = {"statusCode": 200, "body": json.dumps(body)}

        return response
    except Exception as e:
        return f"Caught exception: {e} from {originalEvent}"


if __name__ == "__main__":
    print(hello('{"game_title": "Team Fortress 2"}', None))
    