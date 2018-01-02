#coding=utf8
import itchat

itchat.auto_login(True)

sincere_wish = u'祝%s新年快乐！'

friendList = itchat.get_friends(update=True)[1:]
for friend in friendList:
	print( (friend['DisplayName'] or friend['NickName']), friend['UserName'])
	# itchat.send(SINCERE_WISH % (friend['DisplayName'] or friend['NickName']), friend['UserName'])
