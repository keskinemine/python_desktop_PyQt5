import requests
import json


class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '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'
        self.username = 'keskinemine'

    def getUser(self, username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()

    def getRepositories(self,username):
        response = requests.get(self.api_url+'/users/repos'+username+'/repos')
        return response.json()

    def createRepository(self, name):
        username = 'keskinemine'
        headers = {'Authoization': 'token ' + self.token}
        repo = name
        description = 'Created with api'
        payload = {'name': repo, 'description': description, 'auto_init': 'true'}
        response = requests.post(self.api_url + '/user/repos',  auth=(name, self.token), data= json.dumps(payload) )
       
    
        return response.json()
    
github = Github()
username = 'sharpfa'


while True:
    secim = input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçim: ')

    if secim == '4':
        break
    else:
        if secim == '1':
            username = input('username: ')
            result = github.getUser(username)
            print(f"name: {result['name']} public repos: {result['public_repos']} follower: {result['followers']}")
        elif secim == '2':
            username = input('username: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])
        elif secim == '3':
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result)
        else: 
            print('yanlış seçim')