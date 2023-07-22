def getHousingData(asPandas: bool, postCode: int):
    import requests
    from .makeHousingDataRequest import makeHousingDataRequest
    if asPandas:
        import pandas as pd

    pages = 1
    tmp = makeHousingDataRequest(postCodeRequest = postCode, page = pages) 
    pages += 1
    jDicts = [tmp]
    dfs = [pd.DataFrame.from_dict(tmp['results'])]
    totalPages = tmp['meta']['totalPages']
    
    for i in (pages, totalPages + 1):
        moreData = makeHousingDataRequest(postCodeRequest = postCode, page = pages)
        dfs.append(pd.DataFrame.from_dict(moreData['results']))
        jDicts.append(moreData)
    if asPandas:
        return pd.concat(dfs)
    else:
        return jDicts
