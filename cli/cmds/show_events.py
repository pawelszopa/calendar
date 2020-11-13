from cli.cmds.abs_command import AbsCommand


class ShowEvents(AbsCommand):
    name = 'Show Events'

    def execute(self):
        print("it works, events")