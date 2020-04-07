import requests

class VKAPI:
    def __init__(self, token, group_id):
        self.token = token
        self.group_id = group_id

    def updateLongpoll(self):
        api_url = 'https://api.vk.com/method/groups.getLongPollServer?access_token={0}&group_id={1}&v=5.102'.format(self.token, self.group_id)
        response = requests.get(api_url).json()
        print(response)

        server_url = response['response']['server']
        key = response['response']['key']
        ts = response['response']['ts']

        return server_url, key, ts

    def checkLongpoll(self):
        server_url, key, ts = self.updateLongpoll()
        longoll_url = '{0}?act=a_check&key={1}&wait=25&mode=2&ts={2}'.format(server_url, key, ts)
        longoll_get = requests.get(longoll_url).json()
        ts = longoll_get['ts']
        updates = longoll_get['updates']

        return updates

    def listenServer(self):
        while True:
            for event in self.checkLongpoll():
                yield event
    
    def sendMessage(self, message, peer_id, random_id):
        url_send = 'https://api.vk.com/method/messages.send?message={0}&peer_id={1}&access_token={2}&random_id={3}&v=5.103'.format(message, peer_id, self.token, random_id)
        response_send = requests.get(url_send).json()
        

api = VKAPI(
    token='93254544a3262cc3baf3a0ba22a18575f9579fdedb680f37813955cb52c75e162a0788f5db0ffa241d63f',
    group_id='191469579'
)