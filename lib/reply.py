import itchat
import time
from itchat.content import *
from lib.common import *
from loguru import logger


# 自动回复
@itchat.msg_register(TEXT)
def text_reply(msg):
    logger.debug('From:{} Text:{}', msg.user['NickName'], msg.text)
    parts = msg.text.split()
    str = parts[0]
    reply = None
    if str == '菜单':
        reply = '''by：不舍温柔.
QQ：2152598815
ping：ping xxx
chatgpt： chat xxx
热点新闻：新闻'''
        msg.user.send(reply)
    elif str == 'ping':
        if len(parts) >= 2:
            reply = ping_test(parts[1])
            msg.user.send(reply)
        else:
            msg.user.send('参数不能为空')
    elif str == "chat":
        if len(parts) >= 2:
            reply = chatgpt_reply(parts[1])
            msg.user.send(reply)
        else:
            msg.user.send('参数不能为空')
    elif str == "新闻":
        reply = hot_news()
        msg.user.send(reply)
    else:
        reply = random_txt()
        msg.user.send('要开心哦~')
        msg.user.send('赠你一段话：')
        msg.user.send(reply)
    if reply:
        logger.debug('To:{} Text:{}', msg.user['NickName'], reply)


# 自动同意好友验证
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')
