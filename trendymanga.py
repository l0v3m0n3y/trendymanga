import requests
class Client():
	def __init__(self):
		self.api="https://api.trendymanga.com"
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
	def login(self,email,password):
		data={"username":email,"password":password}
		req=requests.post(f"{self.api}/auth/login",json=data,headers=self.headers).json()
		self.headers["Authorization"]=req["access_token"]
		return req
	def register(self,email,password,username):
		data={"email":email,"password":password,"username":username}
		return requests.post(f"{self.api}/auth/register",json=data,headers=self.headers).json()
	def search(self,page:int=1,size:int=50,artist:str=None,name:str=None,author:str=None,tags:str=None,publishers:str=None):
		data={"page":page,"limit":size,"sortBy":"CREATED_AT","direction":"desc","author":"","artist":"","name":"","publishers":"","tags":""}
		if artist:data["artist"]=artist
		if name:data["name"]=name
		if author:data["author"]=author
		if tags:data["tags"]=[tags]
		if publishers:data["publishers"]=[publishers]
		return requests.post(f"{self.api}/titles/search",json=data,headers=self.headers).json()
	def comment(self,title_id,message):
		data={"titleId":title_id,"text":message}
		return requests.post(f"{self.api}/comments",json=data,headers=self.headers).json()
	def comments_list(self,title_id):
		return  requests.get(f"{self.api}/comments/title/{title_id}",headers=self.headers).json()
	def reply_comment(self,comment_id,message):
		data={"text":message}
		return requests.post(f"{self.api}/comments/{comment_id}/reply",json=data,headers=self.headers).json()
	def vote_comment(self,comment_id):
		return  requests.post(f"{self.api}/comments/{comment_id}/upvote",headers=self.headers).json()
	def unvote_comment(self,comment_id):
		return requests.post(f"{self.api}/comments/{comment_id}/downvote",headers=self.headers).json()
	def chapters_like(self,chapters_id,title_id):
		return requests.post(f"{self.api}/titles/{title_id}/chapters/{chapters_id}/like",headers=self.headers).json()
	def bookmark(self,type,title_id):
		data={"type":type}
		return requests.post(f"{self.api}/titles/{title_id}/bookmark",json=data,headers=self.headers).text
	def tags_list(self,size:int=10,start:int=0):
		return requests.get(f"{self.api}/tags?offset={start}&limit={size}",headers=self.headers).json()
	def genres_list(self,size:int=10,start:int=0):
		return requests.get(f"{self.api}/genres?offset={start}&limit={size}",headers=self.headers).json()
	def publishers(self,size:int=10,start:int=0):
		return requests.get(f"{self.api}/publishers?offset={start}&limit={size}",headers=self.headers).json()
	def top_titles(self,size:int=10):
		return requests.get(f"{self.api}/titles/top?period=all-time&limit={size}",headers=self.headers).json()
	def last_updates(self,size:int=10,start:int=0):
		return requests.get(f"{self.api}/titles/lastUpdates?limit={size}&offset={start}",headers=self.headers).json()