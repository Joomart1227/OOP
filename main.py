import requests
import json

from api.mixins import CreateMixin, ReadMixin, RetrieveMixin, UpdateMixin, DeleteMixin


HOST = 'http://3.67.196.232/'

class InterFace(CreateMixin, ReadMixin, RetrieveMixin, UpdateMixin, DeleteMixin):
    pass

interface = InterFace()

while True:
    print('Dlia dobovlenia todo: add\nDlia prosmotra vceh todo: read\nDlia procmotra opredelennogo todo: retrieve\nChtoby obnovit todo: update\nDlia udalenia todo: delete\nDlia vyhoda iz programmy: quit')
    choice_com = input('print command: ')
    if choice_com == 'add':
        interface.create_todo(HOST)
    elif choice_com == 'read':
        interface.get_all_todos(HOST)
    elif choice_com == 'retrieve':
        interface.retrieve_todo(HOST)
    elif choice_com == 'update':
        interface.update_todo(HOST)
    elif choice_com == 'delete':
        interface.delete_todo(HOST)
    elif choice_com == 'quit':
        break
    else:
        print('Napishite comandu iz spiska')



interface.create_todo(HOST)
interface.get_all_todos(HOST)
interface.retrieve_todo(HOST)
interface.update_todo(HOST)
interface.delete_todo(HOST)