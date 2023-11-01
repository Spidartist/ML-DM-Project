import requests
import json
from pprint import pprint

url = "https://api.inaturalist.org/v1/observations?verifiable=true&taxon_id=201973&locale=en-US&order_by=votes&quality_grade=research&term_id=9&term_value_id=10&page=1&per_page=10"

payload = {}
headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'If-None-Match': 'W/"139834-GiEtn20C77yMHPv3YcRJJuyvJQw"',
    'Origin': 'https://www.inaturalist.org',
    'Referer': 'https://www.inaturalist.org/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
    'X-Via': 'inaturalistjs',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("GET", url, headers=headers, data=payload)
raw_data = json.loads(response.text)["results"]

lst_url = []

for el in raw_data:
    lst = el["observation_photos"]
    # pprint(lst)
    for url in lst:
        if url["photo"]["url"].split(".")[-1] != "gif":
            print(url["photo"]["url"].replace("square", "medium"))

# pprint(raw_data)

print(len(raw_data))
