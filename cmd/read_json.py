import json

def read_json():
    with open('cmd\info.json', 'r') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    a = read_json()
    for i in a:
        name = i
        url = a[i]['url']
        key = a[i]['key']
        print(name, url, key)