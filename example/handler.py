
def handle(data, client):
    print("Hello")
    
    asset = client.assets.retrieve(id=370758465950)
    return {
        "result": asset.id,
        "assetName": asset.desciption,
    }
