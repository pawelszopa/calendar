from datetime import datetime
from cli.cmds.abs_command import AbsCommand
from event import Event


class CreateEvent(AbsCommand):
    name = 'Create Task'

    def execute(self):
        event_name = input("provide event name: \n")
        e = Event(event_name, '20/10/22 15:30', 30, '', '', '')
        self.events.add_event(e)
