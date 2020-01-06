import requests
from wxpy import *
import logging


def get_news():
    """获取金山词霸每日一句"""
    url = "http://open.iciba.com/dsapi/"
    r=requests.get(url)
    json = r.json()['content']
    note = r.json()['note']
    return json,note

def send_news():
    bot = Bot()
    try:
        content,note=get_news()
        print(bot.friends)
    except:
        pass

if __name__ == '__main__':
    # logging.basicConfig(
    #     format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
    # level=logging.WARN)
    # logging.warning('warning 信息')
    # logging.error('error 信息')
    # logging.critical('critial 信息')
    # print(get_news())
    send_news()