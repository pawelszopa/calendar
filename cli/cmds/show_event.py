from cli.cmds.abs_command import AbsCommand


class ShowEvent(AbsCommand):
    name = 'Show Event'

    def execute(self):
        event = int(input("Which ID?"))
        print(self.events.get_event(event))
