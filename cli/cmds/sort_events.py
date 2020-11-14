from cli.cmds.abs_command import AbsCommand



class SortEvents(AbsCommand):
    name = 'Sort Events'

    def execute(self):
        key = ''
        config=[]
        while True:
            key = input("Podaj po czym chcesz sortować - type exit to end")
            if key == "exit":
                break
            config.append(key)
        self.events.sort_config = config


