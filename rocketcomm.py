from rocketchat_API.rocketchat import RocketChat
import re


############################
# ROCKETCHAT COMMUNICATION #
############################

class RocketComm:
	rocket = None

	def __init__(self, config):
		self.user = config['user']
		self.password = config['pass']
		self.URL = config['type'] + '://' + config['host']

	def login(self):
		self.rocket = RocketChat(self.user, self.password, self.URL)

	def logout(self):
		self.rocket.logout()

	def _retrieve_msgs(self, chn):
		hist = self.rocket.channels_history(chn, count=10000).json()
		msgs = hist['messages']

		return msgs
		
	def retrieve_channel_list(self):
		ids = []
	
		list = self.rocket.channels_list(count=10000).json()
		
		for chn in list["channels"]:
			id = chn['_id']
			ids.append(id)
			
		return ids

	def get_emotes(self, chn):
		emotes = []

		msgs = self._retrieve_msgs(chn)
		p = re.compile(":\w+?:") #emotes tracker
		
		for msg in msgs:
			rmsg = msg['msg']
			emote = p.findall(rmsg)
			emotes.extend(emote)

		return set(emotes)
