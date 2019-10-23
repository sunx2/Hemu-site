from requests import get

class Youtube(object):
    def __init__(self,key,channel):
        self.key = key
        self.channel = channel
    
    def get_all_videos(self):
        params = {
            "key": self.key,
            "channelId": self.channel,
            "part":"snippet",
            "order": "date",
            "maxResults": 9
        }
        url = "https://www.googleapis.com/youtube/v3/search"
        return get(url=url,params=params)
    
    def get_channel_data(self):
        url = "https://www.googleapis.com/youtube/v3/channels"
        params = {
            "key":self.key,
            "id":self.channel,
            "part":"snippet"
        }
        return get(url=url,params=params)
