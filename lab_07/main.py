import json
from footballer import Footballer
from search import check_request, get_interval, search

with open('./footballer.csv', 'r') as file:
    data = file.read().replace('\n', '').split(';')
res_data = []
#print(len(data))
for i in range(0, len(data) - 3, 4):
    f = Footballer(data[i], data[i + 1], data[i + 2], data[i + 3])
    res_data.append(f)
data = res_data
# data = json.loads(data)
# for d in data:
#     r = d.get('result')
#     h = Human(r.get('name'), r.get('gender'), r.get('country'), r.get('skill'), r.get('height'))
#     item = {r.get('height'): h}
#     true_data.append(h)
#
# data = true_data


def main():
    print(data)
    request = input("Введите запрос: ")
    term = check_request(request)
    if not term:
         return
    interval, is_not = get_interval(term)
    result = search(data, interval, is_not)
    for footballer in result:
        print(footballer)

main()

# Футболист с высокой стоимостью