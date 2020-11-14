def gen_id():
    idx = 0

    def inner():
        nonlocal idx
        result = idx
        idx += 1
        return result

    return inner


uuid = gen_id()


def config_update():
    key = ''
    value = ''
    config = {}
    while True:
        key = input("Co chcesz zmienic - type exit to finish \n")
        if key == "exit":
            break
        value = input("na co chcesz zmienic? \n")
        config[key] = int(value) if value.isdigit() else value
    return config


# events.filter_config = {
#     'duration': {"min": 100, "max": None},
#      'start_time': {"min": datetime.strptime('1.05.21', '%d.%m.%y'), "max": datetime.strptime('1.09.21', '%d.%m.%y')}
#      }


def config_filter():
    key = ''
    user_min = ''
    user_max = ''
    config = {}
    while True:
        key = input("Po czym chcesz filtrować - type exit to finish \n")
        if key == "exit":
            break

        user_min = input("Podaj Min - type None if it is not relevant \n")
        user_max = input("Podaj Max - type None if it is not relevant \n")
        user_min = int(user_min) if user_min.isdigit() else user_min
        user_max = int(user_max) if user_max.isdigit() else user_max
        user_min = None if user_min == 'None' else user_min
        user_max = None if user_max == 'None' else user_max
        config[key] = {'min': user_min, 'max': user_max}
    return config
