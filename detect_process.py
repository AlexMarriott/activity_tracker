from threading import Thread

from psutil import NoSuchProcess
from datetime import date

import json
import win32gui
import time
import psutil
import win32process
import os
import asyncio

class DetectProcess(Thread):
    def __init__(self):
        self.check = True
        self.win_gui = win32gui
        self.running_application = ''
        self.today = str(date.today())
        self.applications = {}

    def write_to_file(self, application, app_time):
        if not os.path.isfile("{0}.json".format(self.today)):
            with open("{0}.json".format(self.today), "w") as f:
                json.dump({self.today: {}}, f)
                f.close()
        with open("{0}.json".format(date.today()), 'r+') as file:
            data = json.load(file)
            try:
                new_time = data[self.today][application] + app_time
            except KeyError as e:
                print(e)
                new_time = app_time

            data[self.today][application] = new_time
            file.seek(0)
            json.dump(data, file)

    def get_running_process_name(self, pid):
        return psutil.Process(pid[-1]).name()

    def get_current_pid(self):
        return win32process.GetWindowThreadProcessId(self.win_gui.GetForegroundWindow())

    def stop(self):
        self.check = False

    async def run(self):
        while self.check:
            # Needs slightly delay as it will pick up a different pid number
            try:
                current_application = self.get_running_process_name(self.get_current_pid())
                current_application_pid = self.get_current_pid()[0]
                start = time.time()
                # Check if the pid is still alive
                while self.get_current_pid()[0] == current_application_pid:
                    time.sleep(0.5)
                    print("wait")
                end = time.time()
                self.applications[current_application] = round(end - start)

            except ValueError as e:
                print(e)
            except NoSuchProcess as no:
                print(no)

            self.write_to_file(current_application, self.applications[current_application])
            print(self.check)

        return True
