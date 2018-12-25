# coding: utf-8
from abc import ABCMeta, abstractmethod


class BaseCommunicator(object, metaclass=ABCMeta):
    """Base communicator with the device.

    This is the base class of the device client.

    Note:
        This class itself is not used, but it is inherited by
        child classes and used.

    Args:
        *args: Valiable length arguments.

    Attribute:
        is_connected (bool): Connection indicator.
            If it is true, the connection has been established.
        terminator (str): Terminator character.
    """
    is_connected = False
    terminator = ""

    def __del__(self):
        if self.is_connected:
            self.close()

    @abstractmethod
    def open(self):
        """Open the connection to the device.

        Note:
            This method must be overridden in the child class.
        """
        pass

    @abstractmethod
    def close(self):
        """Close the connection to the device.

        Note:
            This method must be overridden in the child class.
        """
        pass

    @abstractmethod
    def send(self, msg):
        """Send a message to the device.

        Note:
            This method must be overridden in the child class.

        Args:
            msg (str): A message to send the device.
        """
        pass

    @abstractmethod
    def receive(self, byte=1024):
        """Receive the response from the device.

        Note:
            This method must be overridden in the child class.

        Args:
            byte (int): Bytes to read.
        """
        pass

    def query(self, msg, byte=1024):
        """Query a message to the device.

        Args:
            msg (str): A message to query the device.
            byte (int): Bytes to read.

        Return:
            ret (bytes): The response from the device.
        """
        self.send(msg)
        ret = self.receive(byte)
        return ret

    @classmethod
    def set_terminator(cls, term_char):
        """Set the terminator character.

        Args:
            term_char (str): A termination character.
        """
        cls.terminator = term_char