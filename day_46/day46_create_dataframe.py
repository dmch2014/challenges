# Create a Dataframe using pandas. You are going to create a
# code to put the following into a Dataframe. You will use the
# information in the table below. Basically, you are going to
# recreate this table using pandas. Use the information in the table
# to recreate the table.
# year Title genre
# 2009 Brothers Drama
# 2002 Spider-Man Sci-fi
# 2009 WatchMen Drama
# 2010 Inception Sci-fi
# 2009 Avatar Fantasy


import pandas as pd
def create_movie_dataframe():
    tabla = [[2009,"Brothers", "Drama"], [2009, "Spider-Man", "Sci-fi"]
        , [2009,"WatchMen", "Drama" ], [2010, "Inception", "Sci-fi" ] , [2009, "Avatar", "Fantasy"]]
    movie_df = pd.DataFrame(tabla, columns=["Year", "Title", "Genre"])
    print(movie_df)
