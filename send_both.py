import random
import requests
import json
import time
import hmac
import hashlib
import base64
import urllib.parse

# -------------------------- 你的配置不变 --------------------------
WECHAT_WEBHOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=b3f75f1b-86ef-4971-845f-40a4150a9513"
DING_WEBHOOK_BASE = "https://oapi.dingtalk.com/robot/send?access_token=f8a63727af370816515478bdf4f552e8de464dcf6f85f5f910df1a2c5a5647b5"
DING_SECRET = "SECcf3d754f687c331542aed29d76a910814347a426b46cb0c3fbbdc73454731b5d"

# -------------------------- 随机读语录 --------------------------
def get_random_quote():
    with open("quotes.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    return random.choice(lines)

# -------------------------- 企业微信 --------------------------
def send_wechat(content):
    data = {"msgtype": "text", "text": {"content": content}}
    headers = {"Content-Type": "application/json"}
    resp = requests.post(WECHAT_WEBHOOK, json=data, headers=headers)
    print("企微返回:", resp.text)

# -------------------------- 钉钉（带签名，修复不发消息） --------------------------
def send_ding(content):
    timestamp = str(round(time.time() * 1000))
    secret_enc = DING_SECRET.encode("utf-8")
    string_to_sign = "{}\n{}".format(timestamp, DING_SECRET)
    string_to_sign_enc = string_to_sign.encode("utf-8")
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

    url = f"{DING_WEBHOOK_BASE}&timestamp={timestamp}&sign={sign}"

    data = {"msgtype": "text", "text": {"content": content}}
    headers = {"Content-Type": "application/json"}
    resp = requests.post(url, json=data, headers=headers)
    print("钉钉返回:", resp.text)

# -------------------------- 执行 --------------------------
if __name__ == "__main__":
    msg = get_random_quote()
    print("发送内容:", msg)
    send_wechat(msg)
    send_ding(msg)
