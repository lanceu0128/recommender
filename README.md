# steam recommender

An implementation of content-based filtering on the Steam game database using scikit-learn's KNN algorithm. The process was documented in a Jupyter notebook and the model can be accessed via a HTTP API endpoint hosted using AWS Lambda and Serverless framework. To try, send a HTTP request with body {"game_title": "game_here"} to https://ac4s67dn01.execute-api.us-east-1.amazonaws.com 
