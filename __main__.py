from datetime import datetime

from events import Events
from user import User
from event import Event
from random import randint

user = User('Pawel', 'pawele@gmail.com')

events = Events()
for idx in range(50):
    event = Event(f'Kebab {idx}', f'{randint(1, 25)}/{randint(1, 11)}/21 {randint(0, 23)}:30',
                  randint(6, 200), '', '', '')
    events.add_event(event)

#  for event in events.get_events():
#    print(event)
# print(events.delete_event(3))
events.update_event(3, {'name': 'kolorowa', "duration": 30})
events.update_event(15, {'name': 'kolorowa', "duration": 30})
# events.update_event(3, {"duration": 15})
events.update_event(3, {"start_time": "3/5/21 15:00"})
# TODO add support for multiple updates {"duration": 15, 'name': 'kolorowa'}
# print(events.get_event(3))
events.sort_config = ['start_time']
# for event in events.sort_events():
#  print(event)

# events.filter_config = [{'duration': (45, ">"), "start_time": ("3/5/21 15:00", "<=")}]
events.filter_config = {
    'duration': {"min": 100, "max": None},
     'start_time': {"min": datetime.strptime('1.05.21', '%d.%m.%y'), "max": datetime.strptime('1.09.21', '%d.%m.%y')}
     }


for event in events.get_events():
    print(event)
print(len(list(events.get_events())))
'''
for event in events.filter_events():
    print(events.filter_config)
    for item in event:
        print(item)
'''

# events.filter_config = [{'duration':(30,"<")}]
# for event in events.filter_events():
#     print(event)
