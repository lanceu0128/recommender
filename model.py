import pandas as pd
import numpy as np
from fuzzywuzzy import process, fuzz
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors


def content_based_recommendations(title, df):
    # find game index
    try:
        index = df[df['title'] == title].index[0]
    except IndexError:
        # use fuzzywuzzy if the user types the name wrong
        title = process.extractOne(
            title, df['title'], scorer=fuzz.token_set_ratio)[0]
        index = df[df['title'] == title].index[0]

    print(f"Recommendations for {title}")

    # create count matrix from df
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(df['soup'])

    # fit KNN model to count_matrix
    knn_model = NearestNeighbors(n_neighbors=10, metric='cosine')
    knn_model.fit(count_matrix)

    # get indices of nearest neighbors from KNN model
    _, indices = knn_model.kneighbors(count_matrix[index])

    # use indices to get recommended titles from the dataframe
    indices = indices.squeeze()[1:]
    recommended_titles = df.loc[indices, 'title'].values.tolist()

    # return dataframe with recommended titles
    # change this to return different data
    columns = ["title", "developer", "genres", "release_date"]
    return title, df[df['title'].isin(recommended_titles)][columns]


if __name__ == "__main__":
    df = pd.read_csv("gamesdata_clean.csv", encoding="utf-8")
    title, result_df = content_based_recommendations(
        "Team Fortress 2", df)  # testing
    print(title, result_df)
