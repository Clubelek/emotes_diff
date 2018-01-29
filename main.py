from pprint import pprint

from rocketcomm import RocketComm
import ids
import re

config = ids.config
chn = 'CwSqCZR6S5TEEqWCX'

	
def getEmotes():
	reg = "title=\"(:.*?:)\""

	with open('RocketChat.html', 'r') as fhtml:
		html=fhtml.read().replace('\n', '')

	p = re.compile(reg)
	return set(p.findall(html))
	
def diffAndSave(all, defined):
	ld = len(defined)
	diff = all-defined
	lt = len(diff)
	
	print("Currently "+str(ld)+" emotes")
	print("Need "+str(lt)+" mores :")
	pprint(diff)
	
	return

rc = RocketComm(config)
rc.login()

all = []
defined = getEmotes()
chns = rc.retrieve_channel_list()
for chn in chns:
	print("Doing #"+chn+" ...")
	all.extend(rc.get_emotes(chn))
all = set(all)

diffAndSave(all, defined)

rc.logout()
