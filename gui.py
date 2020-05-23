from tkinter import Tk, Label, Button
from detect_process import DetectProcess

detect = DetectProcess()


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Start", command=self.start)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def start(self):
        self.greet_button['text'] = "Stop"
        self.greet_button['command'] = self.stop
        start_process()

    def stop(self):
        self.greet_button['text'] = "Start"
        self.greet_button['command'] = self.start
        stop_process()

async def start_process():
    await detect.run()

def stop_process():
    detect.stop()

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
