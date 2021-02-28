from datetime import datetime as dt
from datetime import timedelta
import logging

logger = logging.getLogger(__name__)


def get_auto_shutdown_time(minutes_til_shutdown: int) -> dt:
    # TODO time_shutdown = time_now - time_to_run
    """
    incomplete function, not implemented
    :return: it would be when to shutdown
    """
    try:
        logging.debug(f'get auto shutdown time using \'{minutes_til_shutdown}\'')
        if not isinstance(minutes_til_shutdown, int):
            raise TypeError(f'bad type \'{type(minutes_til_shutdown)}\' for \'{minutes_til_shutdown}\'')
        td_minutes_til_shutdown = timedelta(0, 0, 0, 0, minutes_til_shutdown, 0, 0)
        shutdown_time = dt.now() + td_minutes_til_shutdown
        return shutdown_time
    except Exception as e_err:
        print(e_err.args[0])
