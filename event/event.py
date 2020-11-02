from datetime import datetime


class Event:
    def __init__(self, name, start_time, duration, location, owner, participants):
        self.name = name
        self.start_time = datetime.strptime(start_time, "%d/%m/%y  %H:%M")
        self._duration = duration
        self.location = location
        self.owner = owner
        self.participants = participants
        self.created = datetime.now()

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, val):
        if val < 5:
            raise ValueError(f'Meetings duration lower that 5 makes no sense user value: ({val}).')
        self._duration = val

    @property
    def time_to_event(self):
        time=self.start_time - datetime.now()
        days=time.days
        hours, remainder = divmod(time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f'Time t o event: {days} days, {hours} hours,  {minutes}minutes'

    def __str__(self):
        return f'class Event(name:{self.name}, start time:{self.start_time}, created:{self.created}), ' \
               f'{self.time_to_event}'
