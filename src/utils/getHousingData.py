def getHousingData(asPandas: bool, postCode: int):
    import requests
    if asPandas:
        import pandas as pd
    

    url = f"https://api.boliga.dk/api/v2/search/results?pageSize=500&sort=daysForSale-a&propertyType=1,2,3,4,6&zipCodes={postCode}&searchArchive=true&includeds=1"

    payload = {}
    headers = {
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://www.boliga.dk/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    tmp = response.json()
    if tmp['meta']['totalPages'] > 1:
        print('there is more data to get')
        pass
    if asPandas:
        return pd.DataFrame.from_dict(tmp['results'])
    else:
        return tmp
