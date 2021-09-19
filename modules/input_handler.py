import time
import ctypes
from modules.config import get_config
from enums.virtual_keys import VirtualKey

emulator_handler = 0
config = get_config(__file__)


class NoCompatibleEmulatorFound(Exception):
    def __init__(self):
        self.message = 'No SNES emulator found!'

    def __str__(self):
        return self.message


class InputHandler():
    def __init__(self):
        self.find_emulator_handler()
        self.input_duration = config['input_duration']

    def right(self):     
        """
            Method to send right input
        """

        ctypes.windll.user32.SetForegroundWindow(emulator_handler)
        ctypes.windll.user32.keybd_event(VirtualKey.RIGHT.value, 0, 0, 0)
        time.sleep(self.input_duration)
        ctypes.windll.user32.keybd_event(VirtualKey.RIGHT.value, 0, 2, 0)


    def left(self):     
        """
            Method to send left input
        """

        ctypes.windll.user32.SetForegroundWindow(emulator_handler)
        ctypes.windll.user32.keybd_event(VirtualKey.LEFT.value, 0, 0, 0)
        time.sleep(self.input_duration)
        ctypes.windll.user32.keybd_event(VirtualKey.LEFT.value, 0, 2, 0)


    def up(self):     
        """
            Method to send up input
        """

        ctypes.windll.user32.SetForegroundWindow(emulator_handler)
        ctypes.windll.user32.keybd_event(VirtualKey.UP.value, 0, 0, 0)
        time.sleep(self.input_duration)
        ctypes.windll.user32.keybd_event(VirtualKey.UP.value, 0, 2, 0)


    def down(self):     
        """
            Method to send down input 
        """

        ctypes.windll.user32.SetForegroundWindow(emulator_handler)

        ctypes.windll.user32.keybd_event(VirtualKey.DOWN.value, 0, 0, 0)
        time.sleep(self.input_duration)
        ctypes.windll.user32.keybd_event(VirtualKey.DOWN.value, 0, 2, 0)


    def a(self):     
        """
            Method to send A input 
        """

        ctypes.windll.user32.SetForegroundWindow(emulator_handler)

        ctypes.windll.user32.keybd_event(VirtualKey.V.value, 0, 0, 0)
        time.sleep(self.input_duration)
        ctypes.windll.user32.keybd_event(VirtualKey.V.value, 0, 2, 0)


    def b(self):     
        """
            Method to send B input 
        """
    
        ctypes.windll.user32.SetForegroundWindow(emulator_handler)
        
        ctypes.windll.user32.keybd_event(VirtualKey.Z.value, 0, 0, 0)
        time.sleep(self.input_duration)
        ctypes.windll.user32.keybd_event(VirtualKey.Z.value, 0, 2, 0)


    def x(self):     
        """
            Method to send X input 
        """
    
        ctypes.windll.user32.SetForegroundWindow(emulator_handler)
        
        ctypes.windll.user32.keybd_event(VirtualKey.C.value, 0, 0, 0)
        time.sleep(self.input_duration)
        ctypes.windll.user32.keybd_event(VirtualKey.C.value, 0, 2, 0)


    def y(self):     
        """
            Method to send Y input 
        """
    
        ctypes.windll.user32.SetForegroundWindow(emulator_handler)
        
        ctypes.windll.user32.keybd_event(VirtualKey.X.value, 0, 0, 0)
        time.sleep(self.input_duration)
        ctypes.windll.user32.keybd_event(VirtualKey.X.value, 0, 2, 0)
    

    def find_emulator_handler(self):
        """
            Method to find a compatible emulator window handler
        """

        global emulator_handler

        enum_windows_proc = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
        ctypes.windll.user32.EnumWindows(enum_windows_proc(self.enum_func), 0)

        if emulator_handler == 0:
            raise NoCompatibleEmulatorFound


    @staticmethod
    def enum_func(hwnd, lParam):
        global emulator_handler

        if ctypes.windll.user32.IsWindowVisible(hwnd):
            length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            ctypes.windll.user32.GetWindowTextW(hwnd, buff, length + 1)

            if buff:
                for emulator in config['compatible_emulator']:
                    if emulator in buff.value:
                        emulator_handler = ctypes.windll.user32.FindWindowW(None, buff.value)