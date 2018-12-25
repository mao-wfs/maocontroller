# coding: utf-8
from datetime import datetime
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

    def start(self):
        """Start cross correlation .
        """
        now = datetime.now().timetuple()
        date_str = f"{now.tm_year}y{now.tm_yday}d{now.tm_hour}h{now.tm_min}m{now.tm_sec - 1}"
        ret = self.com.query(f"ctl_corstart={date_str}:0x10")
        return ret