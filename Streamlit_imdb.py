
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image





st.markdown("""

# **Webscraping  of Top 100 Adventure Movies in IMDB**

### The things to webscrape from IMDB are
###### 1. Movie name\n
###### 2. Description\n
###### 3. Release Date\n
###### 4. Director Name\n
###### 5. Rating\n
###### 6. Duration\n
###### 7. Genre\n
###### 8. Stars (Actors)\n
###### 9. Filming Dates






""")

st.header("Webscraping Data")

data = pd.read_csv("data_imdb_adventure.csv")
data

# it used to make selectbox
# data_select =st.sidebar.selectbox("Select your Visualization", ("Movie ratings by year of release", "Movies in top 100 by Actor", "Movies in top 100 by Director"))

# def load_data(data_select):
#     if data_select == "Movie ratings by year of release":
# st.title("Visualization of Movie ratings by year of release")
# st.pyplot('release_date', 'rating')



# imdb_movie = plt.scatter(data['release_date'], data['rating'])
# st.title("Visualization of Movie ratings by year of release")
# st.pyplot(imdb_movie)

st.title("Visualization of Movie ratings by year of release")
fig = plt.figure(figsize = (10, 8))
ax = fig.add_subplot(1,1,1)

ax.scatter(
        data["release_date"],
        data["rating"],
        c = data['votes'], cmap='RdYlBu_r'
    )

ax.set_xlabel("Year of release")
ax.set_ylabel("Movie rating")
ax.set_title("Movie rating over time")
st.write(fig)


movie_actors_dict = {}
for movie, actors in zip(data['movie_name'], data['actors']):
    movie_actors_dict[movie] = actors.split(',')

st.title("Visualization of Movie in top 100 by Actor")
fig = plt.figure(figsize = (10, 8))


ax.bar(
        data["actors"],
        data["actors"]
        
    )

ax.set_xlabel("Actor's name")
ax.set_ylabel("Number of movies")
ax.set_title("")
st.write(fig)
