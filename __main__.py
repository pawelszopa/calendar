from user import User
from event import Event
from random import randint

user = User('Pawel', 'pawele@gmail.com')
print(user)

event = Event('meeting', '6/11/20 15:00', 30, "", '', '')
print(event)

events_list = []
for idx in range(50):
    event = Event(f'Kebab {idx}', f'{randint(1, 25)}/{randint(1, 11)}/21 {randint(0, 23)}:30',
                  {randint(6, 200)}, '', '', '')
    events_list.append(event)

for event in events_list:
    print(event)
