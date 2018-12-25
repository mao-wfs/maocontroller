# coding: utf-8
class BaseDeviceHandler(object):
    """Base device handler.

    This is the base class of device handlers.

    Note:
        This class itself is not used, but it is inherited by
        child classes and used.

    Args:
        com (communicator): Communicator instance.
    """
    def __init__(self, com):
        self.com = com
        self.open()

    def open(self):
        """Open the connection to the device.

        Note:
            This method uses the one of "com".
        """
        self.com.open()

    def close(self):
        """Close the connection to the device.

        Note:

            This method uses the one of "com".
        """
        self.com.close()