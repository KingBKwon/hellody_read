from model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']

async def season_detail(series_id):
    collection = db['KIDS_SEASON']
    cursor = collection.find({'K_SERIES_ID': series_id}, {'_id': 0})
    vod_list = await cursor.to_list(length=100)
    print(vod_list)
    return vod_list
    