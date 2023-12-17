import requests
import json

# Title: Preliminary Actual and Percentage Change in Population 2016 - 2022

#url = "https://api.artic.edu/api/v1/artworks"

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/HEO14/JSON-stat/2.0/en"

def getAll():
    response = requests.get(url)
   # we could do checking for correct response code here
    return response.json()


if __name__=="__main__":
    with open("cso_json_all", "wt") as fp:
      print(json.dumps(getAll()), file=fp)