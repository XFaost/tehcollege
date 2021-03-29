from django.utils.safestring import SafeString
import json

from navigation.models import *

def get_navigation():
    """Отримати навігацію сайту з json-файла"""
    f = open(NAVIGATION_JSON_PATH, "rb")
    return json.loads(f.read().decode('utf8'))

def __item_navigation_to_json_item(item):
    """Отримати json-формат даного елемента навігації"""
    return '{' + '\"name\":\"' + item.name + '\",\"url\":\"' + item.url + '\",\"children\":' + __get_children_of_item_navigation(item.get_children()) + '},'

def __get_children_of_item_navigation(items):
    """Отримати потомків даного елемента навігації з БД у форматі json"""

    item_json = ''

    for item in items:
        item_json += __item_navigation_to_json_item(item)
    
    return '['+item_json[:-1]+']'
    
def __navigation_to_json():
    """Отримати навігацію з БД у форматі json"""

    navigation = Navigation.objects.filter(parent=None)

    return __get_children_of_item_navigation(navigation)
        
def navigation_to_json_file():
    """Зберегти навігацію у json-файл"""

    navigation_json = __navigation_to_json()

    f = open(NAVIGATION_JSON_PATH, 'wb')
    f.write(navigation_json.encode('utf8'))
    f.close()


