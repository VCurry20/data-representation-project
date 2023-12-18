import requests
import json

# Title: Preliminary Actual and Percentage Change in Population 2016 - 2022
# Census 2022 Households, Families and Childcare F3001 - Population

# potential URL's
#url = "https://api.artic.edu/api/v1/artworks"
#url =  "https://collectionapi.metmuseum.org/public/collection/v1"


# CSO URL
# url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/F3001/JSON-stat/2.0/en"


# this will work for any CSO database - just amend the ending
urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnding = "F3001/JSON-stat/2.0/en"
dataset = "F3001"

def getAll(dataset):
    url = urlBeginning + dataset + urlEnding
    response = requests.get(url)
   # we could do checking for correct response code here
    return response.json()
   # click Alt Shift F to view it properly


if __name__=="__main__":
    with open("cso.json", "wt") as fp:
      print(json.dumps(getAll()), file=fp)

