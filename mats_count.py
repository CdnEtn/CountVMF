import json, os

mats = {}

for vmf in os.listdir('vmfs'):
    print(vmf)
    with open('vmfs/' + vmf) as data:
        data = data.read().split('"material"')[1:]
        for x in data:
            x = x.split('"')[1]
            if not x in mats:
                mats[x] = 1
            else:
                mats[x] += 1

with open('mats.json', 'w') as fp:
    json.dump(mats, fp)
