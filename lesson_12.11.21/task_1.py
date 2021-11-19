res = []
with open('nginx_logs.txt', 'r', decode='utf-8') as f:
    for line in f:
        print(line)
        ln = line.split()
        print(ln)

#         res.append(ln[0])
#         res.append(ln[5].strip('"'))
#         res.append(ln[6])
# print(res)
