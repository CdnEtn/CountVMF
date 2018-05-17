import json, operator

with open('skies.json') as f:
    x = json.load(f)

sort = sorted(x.items(), key=operator.itemgetter(1))
for i in range(1,21):
    print(sort[-i])
