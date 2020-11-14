from cli.cmds.abs_command import AbsCommand
from helpers.helpers import config_update


class UpdateEvent(AbsCommand):
    name = 'Update Event'

    def execute(self):
        event = int(input("ktore id?"))
        config = config_update()

        self.events.update_event(event, config)
