
def sortList(listy):
    copy = []
    listy.sort(key=lambda x:x[1])
    for i, ele in enumerate(listy):
        if ele[1] == ele:


    return listy


test = ['redundant', 'profuse', 'humdrum', 'common', 'obey',
'receive', 'young', 'business', 'join', 'bad',
'observe', 'smooth', 'mighty', 'page', 'simplistic',
'rifle', 'true', 'class', 'thundering', 'nostalgic',
'play', 'seemly', 'fumbling', 'rabbits', 'abstracted',
'soap', 'teeny', 'probable', 'enthusiastic', 'ubiquitous']

print(sortList(test))



