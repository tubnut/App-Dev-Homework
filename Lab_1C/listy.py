def vowelCheck(char):
    vowels = ['a','e','i','o','u']
    if char in vowels:
        return True
    else:
        return False

def sortList(listy):
    copy = []
    expendables = []
    temp = ''
    listy.sort(key=lambda x:x[1])
    for i, ele in enumerate(listy):
        temp = listy[i + 1]
        if ele[1] == temp[1]:
            expendables.append(ele)
    return listy + copy


test = ['redundant', 'profuse', 'humdrum', 'common', 'obey',
'receive', 'young', 'business', 'join', 'bad',
'observe', 'smooth', 'mighty', 'page', 'simplistic',
'rifle', 'true', 'class', 'thundering', 'nostalgic',
'play', 'seemly', 'fumbling', 'rabbits', 'abstracted',
'soap', 'teeny', 'probable', 'enthusiastic', 'ubiquitous']

print(sortList(test))



