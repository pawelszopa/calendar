from cli.cmds.abs_command import AbsCommand
from helpers.helpers import config_filter


class FilterEvents(AbsCommand):
    name = 'Filter Events'

    def execute(self):
        self.events.filter_config = config_filter()
