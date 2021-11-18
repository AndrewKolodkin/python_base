import requests

url = requests.get(
    'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
res = []

with open('nginx_logs.txt', 'r+') as f:
    for f_log in url.content.decode(encoding='UTF-8'):
        f.write(f_log)
    for line in f:
        # print(line)
        ln = line.split()
        print(ln)
#         res.append(ln[0])
#         res.append(ln[5].strip('"'))
#         res.append(ln[5])
# print(res)
