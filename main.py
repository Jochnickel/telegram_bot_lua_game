from telebot.telebot import Bot
import subprocess
import os

bot = None
try: os.mkdir('user')
except: pass


def main():
	token = open('token.txt','r')
	bot = Bot(token.read())
	token.close()
	if not 'users' in bot.customDB():
		bot.customDB()['users'] = {}
		bot.customDB.saveFile()
	bot.users = bot.customDB()['users']

	bot.onMessage = onMsg
	bot.onUpdate = onUpd
	bot.onCommand = None
	bot.newCommand_info = False
	bot.newCommand('/skip',cmdSkip)
	bot.newCommand('/level',cmdLevel)
	bot.newCommand('/hint',cmdHint)
	bot.newCommand('/info',cmdInfo)

def getLevel(bot, userid):
	userid = str(userid)
	print(bot.users)
	if not userid in bot.users:
		bot.users[userid] = {'level' : 0, 'solved' : {}, 'skipped':{}}
		bot.customDB.saveFile()
	return bot.users[userid]['level']

def setLevel(bot, userid, lvl = "1", relative = False):
	userid = str(userid)
	i = int(lvl)
	if "1"==lvl or relative:
		bot.users[userid]['level'] += i
		print(bot.users[userid]['level'])
	else:
		bot.users[userid]['level'] = i
	bot.customDB.saveFile()

def setSolved(bot,userid,lvl = None, solved = True):
	userid = str(userid)
	if None==lvl: lvl = getLevel(bot,userid)
	bot.users[userid]['solved'][lvl] = bool(solved)
	bot.customDB.saveFile()

def getSolved(bot,userid,lvl):
	userid = str(userid)
	s = bot.users[userid]['solved']
	return (lvl in s) and (s[lvl])

def skipLevel(bot, userid):
	l = self.getLevel(bot.iserid)
	self.setLevel(bot, userid, 1, relative = True)
	bot.users[userid]['skipped'][l] = True
	bot.customDB.saveFile()

def levelExists(bot,lvl):
	try:
		open('level/%s/wrap.lua'%lvl,'r').close()
		return True
	except: return False

def cmdSkip(bot, userid, params): pass
def cmdLevel(bot, userid, params):
	try:
		lvl = int(params)
		if getSolved(bot,userid,lvl):
			setLevel(lvl)
			announceRound(bot,userid)
	except:
		bot.sendMessage(userid, "current Level: %s"%getLevel(bot,userid))

def cmdHint(bot, userid, params): pass
def cmdInfo(bot, userid, params): pass

def hint(bot, userid, level):
	try:
		f = open('level/%s/hint.txt','r')
		t = f.read()
	except:
		t = 'No Message'
		if f: f.close()

	bot.sendMessage(userid,t)

def onUpd(bot,update):
	print("update")
#	print(update)



def onMsg(bot,update,msg):
	m_id = msg['message_id']
#	date = msg['date']
	chat = msg['chat']
	if 'text' in msg and 'from' in msg:
		from_ = msg['from']
		text = msg['text']
		userid = str(from_['id'])
		getLevel(bot,userid)

		if 'entities' in msg:
			ent = msg['entities'][0]
		playRound(bot,userid = userid,msg = text)


def announceRound(bot,userid):
	lvl = getLevel(bot,userid)
	txt = ""
	try:
		f = open('level/%s/info.txt'%lvl,'r')
		txt = f.read()
		f.close()
	except FileNotFoundError:
		txt = "No lvl Info"
	bot.sendMessage(userid,'`Level %s :  `*%s*   '%(lvl,txt),markdown = True)

def msgLvlNotFound(bot,userid):
	bot.sendMessage(userid,'`No level found.`\ntry __/level 0__', markdown = True)

def playRound(bot,userid,msg):
	level = getLevel(bot,userid)
	try: os.mkdir('user/%s/'%userid)
	except:	pass
	if not levelExists(bot,level):
		msgLvlNotFound(bot,userid)
		return
	try:
		usrFile = open('user/%s/play.lua'%userid,'w')
		usrFile.write(msg)
		usrFile.close()
	except:
		bot.sendMessage(userid,'Error writing File :(')

	errno, log = subprocess.getstatusoutput("tar -c level/%s/wrap.lua user/%s/play.lua | docker run -i --rm -w /home jochnickel/lua sh -c 'tar xf - --strip-components 2;lua wrap.lua'"%(level,userid))
	if errno:
		bot.sendMessage(userid,log)
		bot.sendMessage(userid,"`try again`",markdown = True)
		setLevel(bot,userid,level)
	else:
		bot.sendMessage(userid,log)
		bot.sendMessage(userid,"`level solved`",markdown = True)
		level += 1
		setLevel(bot,userid,level)
		print(userid,' finished!')

	if levelExists(bot,level):
		announceRound(bot,userid)
	else:
		msgLvlNotFound(bot,userid)
main()
