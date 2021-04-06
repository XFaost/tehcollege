def get_request_args(request):
    """
    Отримати аргументи з request

    Parameters:
        request: HttpRequest

    Return:
        dict
    """
    queryDict = None
    if request.method == 'POST':
        queryDict = request.POST
    elif request.method == 'GET':
        queryDict = request.GET
    return queryDict.dict()


def generate_url_args(request_args):
    """
    Згенерувати аргументи для посилання

    Parameters:
        request_args: dict
        
    Return:
        str
    """
    parameters_for_url = '?'
    for i in request_args:
        parameters_for_url += i + '=' + str(request_args[i]) + '&'
    return parameters_for_url[:-1]


def generate_url_args_with_changes(request_args, changed_args):
    """
    Згенерувати аргументи для посилання

    Parameters:
        request_args: dict
        changed_args: dict - аргументи, які потрібно змінити

    Return:
        str
    """
    for arg in changed_args:
        request_args[arg] = changed_args[arg]
    return generate_url_args(request_args)


def __get_request_arg(request, arg_name):
    """
    Отримати значення аргументу з request

    Parameters:
        request: HttpRequest
        arg_name: str

    Return:
        str
    """
    args = get_request_args(request)
    return args.get(arg_name, None)


def __var_is_have_value(var):
    return var is not None and len(var) > 0


def get_request_int_arg(request, arg_name, default_value):
    """
    Отримати значення аргументу з request у вигляді int

    Parameters:
        request: HttpRequest
        arg_name: str
        default_value: int

    Note:
         Якщо виникне помилка - повернеться default_value

    Return:
        int
    """
    var = __get_request_arg(request, arg_name)
    try:
        return int(var)
    except ValueError:
        pass
    except TypeError:
        pass
    return default_value


def get_request_str_arg(request, arg_name):
    """
    Отримати значення аргументу з request у вигляді str

    Parameters:
        request: HttpRequest
        arg_name: str

    Return:
        str
    """
    var = __get_request_arg(request, arg_name)
    if __var_is_have_value(var):
        return var
    return None


def get_request_list_arg(request, arg_name):
    """
    Отримати значення аргументу з request у вигляді list

    Parameters:
        request: HttpRequest
        arg_name: str

    Return:
        list
    """
    var = __get_request_arg(request, arg_name+'[]')
    if __var_is_have_value(var):
        return var
    return None
