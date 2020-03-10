from telebot.telebot import Bot
import subprocess

 token = open('token.txt','r')
bot = Bot(token.read())
 token.close()

def execLua(code):
	try: return subprocess.check_output(['docker','run','-it','centos','lua','-e',code],stderr = w)
	except subprocess.CalledProcessError as e: return '`%s`'%e.output


def onMsg():
	chat = 123
	code = 'for k,v in pairs(_G) do print(k,v) end'
	answer = execLua(code)
	bot.sendMessage(chat,answer)

bot.onMessage = onMsg
