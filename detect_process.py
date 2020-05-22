from psutil import NoSuchProcess
from datetime import date

import json
import win32gui
import time
import psutil
import win32process
import os

check = True
w = win32gui
running_application = ''
today = str(date.today())
applications = {}


def write_to_file(application, app_time):
    if not os.path.isfile("{0}.json".format(today)):
        with open("{0}.json".format(today), "w") as f:
            json.dump({today: {}}, f)
            f.close()
    with open("{0}.json".format(date.today()), 'r+') as file:
            data = json.load(file)
            try:
                new_time = data[today][application] + app_time
            except KeyError as e:
                print(e)
                new_time = app_time

            data[today][application] = new_time
            file.seek(0)
            json.dump(data, file)

def get_running_process_name(pid):
    return psutil.Process(pid[-1]).name()


def get_current_pid():
    return win32process.GetWindowThreadProcessId(w.GetForegroundWindow())

while check:
    # Needs slightly delay as it will pick up a different pid number
    try:
        current_application = get_running_process_name(get_current_pid())
        current_application_pid = get_current_pid()[0]
        start = time.time()
        # Check if the pid is still alive
        while get_current_pid()[0] == current_application_pid:
            time.sleep(0.5)
        end = time.time()
        applications[current_application] = round(end - start)

    except ValueError as e:
        print(e)
    except NoSuchProcess as no:
        print(no)

    write_to_file(current_application, applications[current_application])