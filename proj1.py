import requests
import sys
import sqlalchemy as db
import pandas as pd

# print msg and exit if input is wrong
if len(sys.argv) != 3:
    print("Invalid. Please follow the format:\n")
    print("python script.py <token> <spotify_artist_id>")
    sys.exit(1)

token = sys.argv[1]
id = sys.argv[2]

url = f"https://api.spotify.com/v1/artists/{id}/top-tracks"

headers = {
  "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)

data = response.json()

newDF = pd.DataFrame.from_dict(data['genres'])

engine = db.create_engine('sqlite:///TEST1.db')

newDF.to_sql('table_name', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
   print(pd.DataFrame(query_result))


