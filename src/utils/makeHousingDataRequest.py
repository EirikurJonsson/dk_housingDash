def makeHousingDataRequest(postCodeRequest: int, page: int):
    import requests
    import random
    import pandas as pd
    import os
    print(os.getcwd())
    url = f'https://api.boliga.dk/api/v2/search/results?pageSize=500&sort=street-a&zipCodes={postCodeRequest}&page={page}'
    url = f"https://api.boliga.dk/api/v2/search/results?pageSize=500&sort=daysForSale-a&propertyType=1,2,3,4,6&zipCodes={postCodeRequest}&searchArchive=false&page={page}&includeds=1"
    df = pd.read_csv('./src/assets/Firefox.txt', sep = '\t', header = None)
    user_agent_list = df.iloc[:, 0].to_list()
    payload = {}
    headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
          'Accept': 'application/json, text/plain, */*',
          'Accept-Language': 'en-US,en;q=0.5',
          'Accept-Encoding': 'gzip, deflate, br',
          'Referer': 'https://www.boliga.dk/',
          'Origin': 'https://www.boliga.dk',
          'Sec-Fetch-Dest': 'empty',
          'Sec-Fetch-Mode': 'cors',
          'Sec-Fetch-Site': 'same-site',
          'Connection': 'keep-alive'
    }
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

    proxies = {
      'http': 'http://10.10.1.10:3128',
      'https': 'http://10.10.1.10:1080',
    }
    response = requests.request("GET", url, headers=headers, data=payload, proxies = proxies)
    return response.json()
