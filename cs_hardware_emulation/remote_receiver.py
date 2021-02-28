import logging
logger = logging.getLogger(__name__)


class Receiver:
    def __init__(self):
        self.CHANNEL_UP = 1
        self.CHANNEL_DOWN = 2
