import json, os

props = {}

for vmf in os.listdir('vmfs'):
    print(vmf)
    with open('vmfs/' + vmf) as data:
        data = data.read().split('.mdl')
        for x in data:
            x = x.split('"')[-1]
            if not x in props:
                props[x] = 1
            else:
                props[x] += 1

with open('props.json', 'w') as fp:
    json.dump(props, fp)
