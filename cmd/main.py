import requests
import read_json
import json

chat_history = {}

if __name__ == '__main__':
    a = read_json.read_json()
    print("自定义代理服务器名称列表：")
    for i in a:
        print(i)
    a = a[input("请输入自定义代理服务器名称：")]
    model = input("请输入模型：")
    url = a['url']+"chat/completions"
    api_key = a['key']
    while True:
        text = input("请输入问题：")
        if text == "exit":
            break
        messages = []
        for question in chat_history.keys():
            value = chat_history[question]
            messages.append({"role": "user", "content": question})
            messages.append({"role": "assistant", "content": value})
        
        messages.append({"role": "user", "content": text})
        info = {
            "model": model,
            "messages": messages
        }
        response = requests.post(
            url=url,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            data=json.dumps(info),
            timeout=100
        )
        chat_history[text] = response.json()["choices"][0]["message"]["content"]
        print(response.json()['choices'][0]['message']['content'])