# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, count=True):
    '''Возвращает n шуток из трех слов'''
    rand_lst = []
    for i in range(n):
        template = []
        if count > 5:
            count = False
        if count:
            new = random.choice(nouns)
            while new in rand_lst:
                new = random.choice(nouns)
            template.append(new)
            new = random.choice(adverbs)
            while new in rand_lst:
                new = random.choice(adverbs)
            template.append(new)
            new = random.choice(adjectives)
            while new in rand_lst:
                new = random.choice(adjectives)
            template.append(new)
        else:
            template.append(random.choice(nouns))
            template.append(random.choice(adverbs))
            template.append(random.choice(adjectives))
        rand_lst.append(' '.join(template))
        return rand_lst


print(get_jokes(5))
