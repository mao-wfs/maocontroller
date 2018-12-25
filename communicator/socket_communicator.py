# coding: utf-8
import socket
from .communicator import BaseCommunicator


class SocketCommunicator(BaseCommunicator):
    """Communicator with the device via "Socket".

    This is a child class of the base class "client.BaseClient".

    Args:
        host (str): IP address of the device.
        port (int): Port of the device.
        timeout (float): The read timeout value.
            Defaults to 1.0.

    Attribute:
        is_connected (bool): Connection indicator.
            If it is true, the connection has been established.
        terminator (str): Terminator character.
    """
    def __init__(self, host, port, timeout=1.):
        self.host = host
        self.port = port
        self.timeout = timeout

    def open(self):
        """Open the connection to the device.

        Note:
            This method override the "open" in the base class.
        """
        if not self.is_connected:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(self.timeout)
            self.sock.connect((self.host, self.port))
            self.is_connected = True

    def close(self):
        """Close the connection to the device.

        Note:
            This method override the "close" in the base class.
        """
        self.sock.close()
        del(self.sock)
        self.is_connected = False

    def send(self, msg):
        """Send a message to the device.

        Note:
            This method override the "send" in the base class.

        Args:
            msg (int): A message to send the device.
        """
        self.sock.send((msg + self.terminator).encode())

    def receive(self, byte=1024):
        """Receive the response from the device.

        Note:
            This method override the "receive" in the base class.

        Args:
            byte (int): Bytes to read. Defaults to 4096.

        Return:
            ret (bytes): The response from the device.
        """
        ret = self.sock.recv(byte)
        return ret