from cli.cmds.abs_command import AbsCommand


class CreateEvent(AbsCommand):
    name = 'Create Task'

    def execute(self):
        print("it works")