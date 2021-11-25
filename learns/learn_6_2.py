import json

params = {'зарплата': 50000, 'bonus': 20000}

# params_as_str = json.dumps(params)
# print(type(params), params)
# print(type(params_as_str), params_as_str)

with open('params.json', 'w', encoding='UTF-8') as f:
    # f.write(params_as_str)
    json.dump(params, f, indent=4)  # ensure_ascii=False
with open('params.json', 'r', encoding='UTF-8') as f:
    # params_as_str2 = f.read()
    # params2 = json.load(params_as_str2)
    params2 = json.load(f)

print(type(params2), params2)
