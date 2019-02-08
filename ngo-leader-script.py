import json
import requests

#this is the search method of finding the info
#use '%20' for spaces and '%22' for quotes around phrases to get exact word order reponses
search_url = 'https://projects.propublica.org/nonprofits/api/v2/search.json?q=%22public%20knowledge%22&state%5Bid%5D=DC'
#creates the object holding the response from the API
search_response = requests.get(search_url)
#checks for errors
search_response.raise_for_status()
#assigns the json to ngoData
ngoSearchData = json.loads(search_response.text)






print(ngoSearchData)
