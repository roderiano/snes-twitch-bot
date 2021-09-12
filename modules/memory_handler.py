from ctypes import *
from ctypes.wintypes import *
from modules.config import get_config
import os

config = get_config(__file__)

class InvalidEmulator(Exception):
    def __init__(self):
        self.message = 'No valid emulator found'
    def __str__(self):
        return self.message


class MemoryHandler(object):
    def __init__(self):
        self.pid = self.get_emulator_pid()


    def get_emulator_pid(self):
        ...
