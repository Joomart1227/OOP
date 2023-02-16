import requests
import json

HOST = 'http://3.67.196.232/'

class CreateMixin:
    def create_todo(self, url) -> None:
        data_ = {
            'title': input('Vvedite nazvanie: '),
            'is_done': False
        }
        respon = requests.post(url + 'todo/create', data=json.dumps(data_))
        if respon.status_code == 200:
            print(1)
        else:
            print(0)


class ReadMixin:
    def get_all_todos(self, url):
        respon = requests.get(url + 'todo/all')
        if respon.status_code == 200:
            print(json.loads(respon.text))
        else:
            print(Exception('Problema na storone servera'))

class RetrieveMixin:
    def retrieve_todo(self, url):
        id_int = input('Vvedite id: ')
        response = requests.get(url + f'todo/{id_int}')
        if response.status_code == 200:
            print(json.loads(response.text))
        elif response.status_code == 404:
            print(Exception('Net takoi zapisi'))
        else:
            print(Exception('Nepredvidennaia oshibka', response.status_code))


class UpdateMixin:
    def update_todo(self, url):
        id_ = input('Vvedite id: ')
        data_ = {
            'title': input('Vvedite nazvanie: '),
            'is_done': False
        }
        response = requests.put(url + f'todo/{id_}/update', data=json.dumps(data_))
        if response.status_code == 200:
            print(json.loads(response.text))
        elif response.status_code == 404:
            print(Exception('Net takoi zapisi'))
        else:
            print(Exception('Nepredvidennaia oshibka', response.status_code))

class DeleteMixin:
    def delete_todo(self, url):
        id_ = input('Введите id: ')
        response = requests.delete(url + f'todo/{id_}/delete')
        if response.status_code == 200:
            print(json.loads(response.text))
        elif response.status_code == 404:
            print(Exception('Net takoi zapisi'))
        else:
            print(Exception('Nepredvidennaia oshibka'))