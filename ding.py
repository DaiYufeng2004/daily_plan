import requests
import json

url = "https://oapi.dingtalk.com/robot/send?access_token=f8a63727af370816515478bdf4f552e8de464dcf6f85f5f910df1a2c5a5647b5"

headers = {"Content-Type": "application/json"}

data = {
    "msgtype": "text",
    "text": {
        "content": "GitHub定时推送测试成功！"
    }
}

resp = requests.post(url, data=json.dumps(data), headers=headers)
print(resp.text)
