import requests
import sqlalchemy as db
import pandas as pd

token = "BQD_FbxCYtfnOeBB4rFbZBgmiYzLmRevrLoN7w-uPyNCvuaOkHopVGLMWZBM51UULVeN7KmLrl3C0Bvwo6uZptlUzvax7bO3mSgJBy2X2Oz7YEVCj2qynPL4_XWFz0VQvSZJV43_cEQ"

id = "3Z7onAknzpinUu3KtmgeZb?si=f1d98XYWT3aUadCfkI8krQ"

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


