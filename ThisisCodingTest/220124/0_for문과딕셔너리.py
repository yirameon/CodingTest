# 딕셔너리 선언
dict_a={
    'name':'Yerang',
    'type':'Student',
    'gender':'Female'
}
for i in dict_a:
    print(i,':',dict_a[i])

# 연습문제
pets=[
    {'name':'구름','age':5},
    {'name':'구름','age':3},
    {'name':'아지','age':1},
    {'name':'호랑이','age':1}
]
for i in pets:
    print(i['name'],i['age'],'살')
for i in pets:
    print('{} {}살'.format(i['name'],i['age']))
for i in pets:
    print(i['name'],str(i['age'])+'살')