from datetime import datetime

class Filter:
    @staticmethod
    def filter(fn):
        def inner(obj):

            filtered_tasks = []

            conditions = obj.filter_config.keys()

            for event in fn(obj):
                counter = 0

                for condition in conditions:
                    min_val = obj.filter_config[condition]['min']
                    max_val = obj.filter_config[condition]['max']

                    value = getattr(event, condition)
                    min_val = value if min_val is None else min_val
                    max_val = value if max_val is None else max_val

                    if min_val <= value <= max_val:
                        counter += 1

                if counter == len(conditions):
                    filtered_tasks.append(event)

            return filtered_tasks
        return inner





'''
class Filter:
    @staticmethod
    def filter(fn):
        def inner(obj):

            def custom_filter(event):

                min_val = obj.filter_config['duration']['min']
                max_val = obj.filter_config['duration']['max']

                value = getattr(event, list(obj.filter_config.keys())[0])
                min_val = value if min_val is None else min_val
                max_val = value if max_val is None else max_val

                return min_val <= value <= max_val

            result = filter(custom_filter, fn(obj))
            return result
        return inner
'''


'''
class Filter:
    @staticmethod
    def filter(fn):
        def inner(obj):
            config = []
            counter = 0
            for item in range(len(list(obj.filter_config[0].items()))):
                key, value = list(obj.filter_config[0].items())[counter]
                config.append((key, value))
                counter += 1
            print(config)

            iteration = 0
            final_result = []
            for tuples in config:
                # print(tuples)
                key, value = tuples

                try:
                    item = datetime.strptime(value[0], "%d/%m/%y  %H:%M")
                except Exception:
                    item = value[0]

                if iteration == 0:
                    funct = fn(obj)
                else:
                    funct = result

                if value[1] == "<":
                    result = list(filter(lambda x: getattr(x, key) < item, funct))
                    final_result.append(result)

                elif value[1] == ">":
                    result = list(filter(lambda x: getattr(x, key) > item, funct))
                    final_result.append(result)

                elif value[1] == "=":
                    result = list(filter(lambda x: getattr(x, key) == item, funct))
                    final_result.append(result)

                elif value[1] == "<=":
                    result = list(filter(lambda x: getattr(x, key) <= item, funct))
                    final_result.append(result)

                elif value[1] == ">=":
                    result = list(filter(lambda x: getattr(x, key) >= item, funct))
                    final_result.append(result)

                iteration += 1

            return final_result[-1]

        return inner
'''

'''
class Filter:
    @staticmethod
    def filter(fn):
        def inner(obj):
            key, value = list(obj.filter_config[0].items())[0]
            print(value)
            try:
                item = datetime.strptime(value[0], "%d/%m/%y  %H:%M")
                print(type(item))
            except:
                item = value[0]
            if value[1] == "<":
                return filter(lambda x: getattr(x, key) < item, fn(obj))
            elif value[1] == ">":
                return filter(lambda x: getattr(x, key) > item, fn(obj))
            elif value[1] == "=":
                return filter(lambda x: getattr(x, key) == item, fn(obj))
            elif value[1] == "<=":
                return filter(lambda x: getattr(x, key) <= item, fn(obj))
            elif value[1] == ">=":
                return filter(lambda x: getattr(x, key) >= value[0], fn(obj))

            # return filter(lambda x: [getattr(x, condition) for condition in obj.filter_config],fn(obj))
            # return filter(fn(obj), key=lambda x: [getattr(x, condition) for condition in obj.sort_config])
            # sorted()

        return inner
'''
