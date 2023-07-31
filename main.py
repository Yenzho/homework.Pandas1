import pandas as pd

def find_best_film():
    df = pd.read_csv("ml-25m\\ratings.csv", sep=',')
    sorted_by_rating = df[df.rating == 5.0]["movieId"].value_counts()

    db = pd.read_csv("ml-25m\\movies.csv", sep=',')
    print(db[db.movieId == sorted_by_rating.idxmax()])

find_best_film()           #Первое задание

def sum_filtered_countries():
    df = pd.read_csv("ml-25m\\power.csv", sep=',')
    filtered = df[(
                                (df['country'] == 'Latvia') |
                                (df['country'] == 'Lithuania') |
                                (df['country'] == 'Estonia')
                        ) &
                        (
                                (df['category'] == 4) |
                                (df['category'] == 12) |
                                (df['category'] == 21)
                        ) &
                        (
                                (df.year >= 2005) & (df.year <= 2010)
                        ) & (df.quantity >= 0)]
    print(sum(filtered.quantity))

sum_filtered_countries()                  #Второе заданиe

table = pd.read_html("https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html")
df = table[0]
print(df.head())                          #Третье задание





