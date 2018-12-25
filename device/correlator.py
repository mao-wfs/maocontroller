# coding: utf-8
from .device import BaseDeviceHandler


class CorrelatorHandler(BaseDeviceHandler):
    """Correlator handler.

    Note:
        This class is based on "device.BaseDeviceHandler".

    Args:
        com (communicator): Communicator instance.
    """
    def __init__(self, com):
        super().__init__(com)
        self.com.set_terminator(";")

    # NOTE: TBD
    def initialize(self):
        """Initialize the correlator.
        """
        pass