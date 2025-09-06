dic = {}
dic['name'] = '홍길동'
dic['birth'] = "1128"
dic["age"] = 30
print(dic)
b = list(dic.items())
dic.clear()
print(dic)
print(b)
del b[0]
print(b)
