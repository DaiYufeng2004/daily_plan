import random
import requests
import json

# -------------------------- 配置（你这两个地址不用改）--------------------------
WECHAT_WEBHOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=b3f75f1b-86ef-4971-845f-40a4150a9513"
DING_WEBHOOK   = "https://oapi.dingtalk.com/robot/send?access_token=f8a63727af370816515478bdf4f552e8de464dcf6f85f5f910df1a2c5a5647b5"

# -------------------------- 从文本文件随机读取一句 --------------------------
def get_random_quote():
    with open("quotes.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    return random.choice(lines)

# -------------------------- 发送企业微信 --------------------------
def send_wechat(content):
    data = {"msgtype": "text", "text": {"content": content}}
    headers = {"Content-Type": "application/json"}
    resp = requests.post(WECHAT_WEBHOOK, data=json.dumps(data), headers=headers)
    print("企微返回:", resp.text)

# -------------------------- 发送钉钉 --------------------------
def send_ding(content):
    data = {"msgtype": "text", "text": {"content": content}}
    headers = {"Content-Type": "application/json"}
    resp = requests.post(DING_WEBHOOK, data=json.dumps(data), headers=headers)
    print("钉钉返回:", resp.text)

# -------------------------- 主执行 --------------------------
if __name__ == "__main__":
    msg = get_random_quote()
    print("本次发送:", msg)
    send_wechat(msg)
    send_ding(msg)
