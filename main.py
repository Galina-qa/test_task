import requests
import json


def load_record(person_name): #функция для получения json-объекта
    res = requests.get('https://api.agify.io/?name='+person_name) #запрос данных с сервера
    person_record = json.loads(res.text)
    return person_record


names = ['ivan', 'galina', 'timon', 'tasya', 'nikolay']
records = []

for name in names:
    record = load_record(name)
    records.append(record)


myFile = open('data.csv', 'w')

for record in records:
    myFile.write(record['name']+';'+str(record['age'])+';'+str(record['count'])+'\n')

