import itchat
from loguru import logger
import init
import lib.reply

logger.add('log/runtime_{time}.log', rotation='00:00')
logger.info('Process starts')

itchat.auto_login(True)
itchat.run(True)

logger.info('Process ends')