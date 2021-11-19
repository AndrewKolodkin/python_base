res = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        element = [line[:line.index('-') - 1]]
        line = line[line.index('"') + 1:]
        element.append(line[:line.index(' ')])
        element.append(line[line.index('/'):line.index('H') - 1])
        res.append(tuple(element))
print('[')
for el in res:
    print(el, end=',\n')
print(']')
