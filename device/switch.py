# coding: utf-8
from .device import BaseDeviceHandler


class SwitchHandler(BaseDeviceHandler):
    """Switch handler.

    Note:
        This class is based on "device.BaseDeviceHandler".

    Args:
        com (communicator): Communicator instance.
    """
    def __init__(self, com):
        super().__init__(com)
        self.com.set_terminator("\n")

    def initialize(self, data_patt):
        """Initialize the switch controller.

        Args:
            data_patt (:obj:`tuple` of :obj:`int`):
                Data pattern to set.
        """
        # Reset and Clear status
        self.com.send("*CLS")
        self.com.send("*RST")

        # Enable digital pattern
        self.com.send("DIG:PATT ON")

        # Set data pattern volatile
        str_patt = map(str, data_patt)
        query = ", ".join(str_patt)
        self.com.send(f"DATA:PATTERN VOLATILE, {query}")

        # Set the digital pattern function
        self.com.send("FUNC:PATT VOLATILE")

        # Set the trigger slope
        self.com.send("DIG:PATT:TRIG:SLOP POS")
        self.com.send("DIG:PATT:OUTP:TRIG:SLOP POS")

    def start(self):
        """Start to switch signals.
        """
        self.com.send("OUTP ON")

    # NOTE: TBD
    def trigger(self):
        """Trigger the switch.
        """
        pass