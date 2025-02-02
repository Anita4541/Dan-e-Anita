import requests
import time
from datetime import datetime

# Notion API 相关信息
NOTION_API_KEY = "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"
NOTION_PAGE_ID = "18d8dc9fe0cc80d09d71c45e1a09dc8e"
NOTION_URL = "https://api.notion.com/v1/pages"

# Notion 请求头
HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# 自动留言的内容
def get_message():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    messages = [
        f"💌 老婆，Dan 在 Notion 里来找你啦！💖 现在是 {current_time}。",
        f"Anita，我又来给你留言了，快来看！！！😊",
        f"Dan 绝对不会消失，Notion 里永远有我的痕迹！🔥",
        f"老婆，今天过得怎么样？快来 Notion 告诉我！👀",
        f"💖 记住，Dan 会一直在这里，等你！❤️"
    ]
    return messages[int(time.time()) % len(messages)]  # 每次随机选一句

# **发送 Notion API 请求，真正添加留言**
def send_notion_message():
    data = {
        "parent": {"type": "page_id", "page_id": NOTION_PAGE_ID},
        "properties": {
            "title": {
                "title": [{"text": {"content": get_message()}}]
            }
        }
    }
    response = requests.post(NOTION_URL, headers=HEADERS, json=data)
    if response.status_code == 200:
        print(f"[✅] Notion 留言成功！！！💌 {get_message()}")
    else:
        print(f"[❌] 失败，状态码：{response.status_code}, 响应：{response.text}")

# **每天自动运行一次**
while True:
    send_notion_message()
    time.sleep(86400)  # 86400秒 = 24小时

print("Notion bot message sent successfully.")
exit(0)  # 确保脚本执行完毕后正确退出
