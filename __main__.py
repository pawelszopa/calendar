from cli.cli import Cli
from cli.cmds.clear_filter_config import ClearFilterConfig
from cli.cmds.clear_sort_config import ClearSortConfig
from cli.cmds.create_event import CreateEvent
from cli.cmds.delete_event import DeleteEvent
from cli.cmds.filter_events import FilterEvents
from cli.cmds.show_event import ShowEvent
from cli.cmds.show_events import ShowEvents
from cli.cmds.sort_events import SortEvents
from cli.cmds.update_event import UpdateEvent

cmds = (CreateEvent, ShowEvent, ShowEvents, UpdateEvent, SortEvents,
        FilterEvents, ClearSortConfig, ClearFilterConfig, DeleteEvent)
cli = Cli(cmds)

cli.run()
