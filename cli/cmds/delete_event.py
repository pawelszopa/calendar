from cli.cmds.abs_command import AbsCommand


class DeleteEvent(AbsCommand):
    name = 'Delete Event'

    def execute(self):
        event = int(input("Which ID?\n"))
        print(f'removed id: {event}' if self.events.delete_event(event) else f'can not find id {event}')
