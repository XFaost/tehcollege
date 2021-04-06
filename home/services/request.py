from typing import Optional, Union


def __get_var_from_request(request, name_var: str) -> Optional[str]:
    """Отримати зміст аргументу з назвою name_var. Функція самостійно визначає request.method"""
    if request.method == 'POST':
        return request.POST.get(name_var)
    elif request.method == 'GET':
        return request.GET.get(name_var)
    else:
        return None


def __var_have_value(var: Union[str, list]) -> bool:
    if var is not None and len(var) > 0:
        return var
    return None


def get_int_from_request(request, name_var: str, default_value: int) -> int:
    """Отримати зміст аргументу з назвою name_var у вигляді int. Якщо виникла помилка - поверне default_value"""
    var = __get_var_from_request(request, name_var)
    try:
        return int(var)
    except ValueError:
        pass
    except TypeError:
        pass
    return default_value


def get_str_from_request(request, name_var: str) -> Optional[str]:
    """Отримати зміст аргументу з назвою name_var у вигляді str. Якщо виникла помилка - поверне None"""
    var = __get_var_from_request(request, name_var)
    if __var_have_value(var):
        return var
    return None


def get_list_from_request(request, name_var: str) -> Optional[list]:
    """Отримати зміст аргументу з назвою name_var[] у вигляді list. Якщо виникла помилка - поверне None"""
    var = __get_var_from_request(request, name_var + '[]')
    if __var_have_value(var):
        return var
    return None
