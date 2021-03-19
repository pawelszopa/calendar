from cli.cmds.abs_command import AbsCommand


class ClearSortConfig(AbsCommand):
    name = 'Clear Sort Settings'

    def execute(self):
        self.events.sort_config = []
