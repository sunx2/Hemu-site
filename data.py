from requests import get
from api import Youtube
import json

class Extractor(object):
    def __init__(self,key,channelid):
        self.id = 1
        self.key = key
        self.channelname = channelid
    
    def channel(self):
        a = Youtube(self.key,self.channelname).get_channel_data().json()
        #print(a)
        curl = f"https://www.youtube.com/channel/{self.channelname}/featured"
        ctitle = a['items'][0]["snippet"]["title"]
        cemail = a['items'][0]["snippet"]["description"].split("\n")[8].split(": ")[1]
        cphone = a['items'][0]["snippet"]["description"].split("\n")[9].split(":")[1]
        cinsta = a['items'][0]["snippet"]["description"].split("\n")[11].split("Instagram:")[1]
        cfacebook = a['items'][0]["snippet"]["description"].split("\n")[14].split("Facebook:")[1]
        cdesc = a['items'][0]["snippet"]["description"].split("For others enquiry")[0]
        cimage = a["items"][0]["snippet"]["thumbnails"]["high"]["url"]
        params = {
            "url": curl,
            "image": cimage,
            "description": cdesc,
            "title": ctitle,
            "contacts": {
                "mail":cemail,
                "phone":cphone
            },
            "social":{
                "facebook": cfacebook,
                "insta": cinsta
            }
        }

        return json.dump(params,open("channel.json",'w'))

    def video(self):
        a = Youtube(self.key,self.channelname).get_all_videos().json()
        params = {}
        for i in a["items"]:
            params[f'https://www.youtube.com/embed/{i["id"]["videoId"]}'] = {
                "title": i["snippet"]["title"],
                "description": i["snippet"]["description"],
                "image": i["snippet"]["thumbnails"]["medium"]["url"],
                "image_high": i["snippet"]["thumbnails"]["high"]["url"],
            }
        return json.dump(params,open("video.json",'w'))

