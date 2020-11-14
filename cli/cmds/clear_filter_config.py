from cli.cmds.abs_command import AbsCommand


class ClearFilterConfig(AbsCommand):
    name = 'Clear Filter Settings'

    def execute(self):
        self.events.filter_config = {}
