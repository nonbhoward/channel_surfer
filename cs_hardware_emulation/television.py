from datetime import datetime
from remote_receiver import Receiver
from cs_media_library.vcr import VCR


class Television:
    def __init__(self, minutes_til_shutdown=0):
        """
        :param minutes_til_shutdown: if 0, disabled, else, retrieve a datetime to set as a shutdown threshold
        """
        self.power_on_time = datetime.now()  # used as a reference for resuming channels at a timestamp
        self.player = VCR()
        self.channels = self.player.vhs_tapes
        self.active_channel = self._get_startup_channel()
        self.remote_receiver = Receiver()
        if minutes_til_shutdown:
            self.auto_shut_down_time = self._get_auto_shutdown_time()

    def change_channel(self, remote_signal):
        # FIXME what 'event' triggers a change channel call?
        try:
            if remote_signal == self.remote_receiver.CHANNEL_UP:
                pass  # TODO change channel up
            elif remote_signal == self.remote_receiver.CHANNEL_DOWN:
                pass  # TODO change channel down
            else:
                pass  # TODO other cases
        except Exception as e_err:
            print(e_err.args[0])

    def play_time_of_day_channel(self):
        try:
            print(self)
        except Exception as e_err:
            print(e_err.args[0])

    @staticmethod
    def _get_auto_shutdown_time() -> datetime:
        # TODO time_shutdown = time_now - time_to_run
        """
        incomplete function, not implemented
        :return: it would be when to shutdown
        """
        try:
            time_now = datetime.now()
            return time_now
        except Exception as e_err:
            print(e_err.args[0])

    @staticmethod
    def _get_startup_channel():
        # TODO, restart from last state?
        try:
            pass
        except Exception as e_err:
            print(e_err.args[0])


if __name__ == '__main__':
    cm = Television()
    pass