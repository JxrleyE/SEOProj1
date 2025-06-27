import requests

token = "BQBSAkwdCTrHkHkI-BXVkuPCo81ktPhSNhLlYF3Bx03laQV9d0sd11DTnP4lD6ZTvC2sT6Yde6jQt9ccb8woq7IlhYwilryqgPdDj2dCInAFp10aqcHGMkHWZ4Pp_KHqxt6Yqnmu_gQ"

id = "3Z7onAknzpinUu3KtmgeZb?si=f1d98XYWT3aUadCfkI8krQ"

url = f"https://api.spotify.com/v1/artists/{id}"

headers = {
  "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)

data = response.json()

print(data)



