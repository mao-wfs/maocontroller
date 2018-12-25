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
        """Start cross correlation.
        """
        now = datetime.now().timetuple()
        date_str = f"{now.tm_year}y{now.tm_yday}d{now.tm_hour}h{now.tm_min}m{now.tm_sec - 1}"
        ret = self.com.query(f"ctl_corstart={date_str}:0x10")
        return ret

    def stop(self):
        """Stop correlation.
        """
        now = datetime.now().timetuple()
        date_str = f"{now.tm_year}y{now.tm_yday}d{now.tm_hour}h{now.tm_min}m{now.tm_sec - 1}"
        ret = self.com.query(f"ctl_colstop={date_str}")
        return ret

    def set_gigabit_ethernet_ip(self, ip):
        """Set the IP address of 1G port.

        Args:
            ip (str): IP address of 1G port.
        """
        ret = self.com.query(f"set_gbeip={ip}")
        return ret

    def set_ntp_ip(self, ip):
        """Set the IP address of NTP server.

        Args:
            ip (str): IP address of NTP server.
        """
        ret = self.com.query(f"set_ntp={ip}")
        return ret