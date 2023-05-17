import os

msg = '''content-length: 26
sec-ch-ua: "Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"
accept: application/json, text/plain, */*
content-type: application/json;charset=UTF-8
sec-ch-ua-mobile: ?0
authorization: 6508525923683601371858261555053-900-1440
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54
sec-ch-ua-platform: "macOS"
origin: https://glados.rocks
sec-fetch-site: same-origin
sec-fetch-mode: cors
sec-fetch-dest: empty
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'''
cookie = {'koa:sess':os.environ['SESS'],
'koa:sess.sig':os.environ['SIG'],
'_gid':'GA1.2.1787289856.1679884853',
'_ga_CZFVKMNT9J':'GS1.1.1679884852.12.1.1679884886.0.0.0',
'_ga':'GA1.1.711380114.1609501707'}
print(cookie)

def msg_to_map(msg):
    msg = msg.split('\n')
    msg = [x.split(': ') for x in msg]
    msg = {x[0]:x[1] for x in msg}
    # msg['content-length'] = int(msg['content-length'])
    return msg

msg = msg_to_map(msg)
print(msg)
import requests

url = 'https://glados.rocks/api/user/checkin'

r = requests.post(url, data='{"token":"glados.network"}', headers=msg, cookies=cookie)
print(r.text)

import json
try:
    data = json.loads(r.text)
except:
    data = {"message": r.text}
status = "Checkin! Get 1 Day" in data["message"]
send = requests.post('https://sctapi.ftqq.com/{}.send'.format(os.environ['SEND']), data={"title": "签到成功" if status else "签到失败", "desp": data["message"]})
print(send.text)
