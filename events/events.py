# TODO add filter functionality use decorator (multipy) chce od daty do daty trwajace 30 min
from filtering import Filter
from sorting import Sort


class Events:
    def __init__(self):
        self._events = []
        self.sort_config = []
        self.filter_config = []

    def add_event(self, event):
        self._events.append(event)

    def get_events(self):
        return self._events

    def get_event(self, idx):
        result = list(filter(lambda x: x.id == idx, self._events))
        try:
            return result[0]
        except IndexError:
            return False

    def delete_event(self, idx):
        event = self.get_event(idx)
        if event:
            self._events.remove(event)
            return True
        return False

    def update_event(self, idx, config):
        event = self.get_event(idx)
        for item in range(len(config)):
            if event:
                key = [*config][item]  # list(config.keys())[0]
                setattr(event, key, config[key])

    @Sort.sort
    def sort_events(self):
        return self._events

    @Filter.filter
    def filter_events(self):
        return self._events
