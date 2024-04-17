import webbrowser
from pynput.keyboard import Key, Controller
import time
from tkinter import messagebox
import tkinter as tk
import random
from selenium import webdriver


class MyGUI:
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("400x625")
        self.root.title("MS_GP-Daily")

        self.describe = tk.Label(self.root, text="Welcome to the MS_GP-Helper!", font=("Arial", 18))
        self.describe.pack(padx=20, pady=20)
        self.d_checkbox = tk.Label(self.root, text="Please select the delay(only check 1 Box): ", font=("Arial", 14))
        self.d_checkbox.place(x=25, y=100)
        self.d_Number = tk.Label(self.root, text="How many searches? ", font=("Arial", 14))
        self.d_Number.place(x=25, y=245)
        self.d_Used = tk.Label(self.root, text="Used Words: ", font=("Arial", 14))
        self.d_Used.place(x=25, y=300)

        self.input_num = tk.Entry(self.root, width=20, bg="#f7ffde")
        self.input_num.place(x=240, y=250)
        self.input_delay = tk.Entry(self.root, width=20, bg="#f7ffde")
        self.input_delay.place(x=240, y=215)

        self.listbox = tk.Listbox(self.root, bg="#f7ffde")
        self.listbox.place(x=45, y=335, height=200, width=320)

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="1S", font=("Arial", 14), variable=self.check_state)
        self.check.place(x=50, y=150)

        self.check_state_2 = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="3S", font=("Arial", 14), variable=self.check_state_2)
        self.check.place(x=125, y=150)

        self.check_state_3 = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="5S", font=("Arial", 14), variable=self.check_state_3)
        self.check.place(x=200, y=150)

        self.check_state_4 = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="10S", font=("Arial", 14), variable=self.check_state_4)
        self.check.place(x=275, y=150)

        self.check_state_5 = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Custom Delay", font=("Arial", 14), variable=self.check_state_5)
        self.check.place(x=50, y=205)

        self.btn_1 = tk.Button(self.root, text="Start", font=("Arial", 18), command=self.BTN_function)
        self.btn_1.place(x=50, y=550, height=50, width=300)

        self.root.mainloop()

    def BTN_function(self):
        checkbox_num = (self.check_state.get() + self.check_state_2.get() +
                        self.check_state_3.get() + self.check_state_4.get() + self.check_state_5.get())

        if checkbox_num > 1:
            messagebox.showinfo(title="Message", message="Tick only one Box please.")
        elif self.input_num.get() == "":
            messagebox.showinfo(title="Message", message="How many searches?")
        elif self.check_state_5.get() == 1:
            if self.input_delay.get() == "":
                messagebox.showinfo(title="Message", message="please chose a custom delay.")
            else:
                delay = float(self.input_delay.get())
                print(delay)
                search_function(self, delay)
        else:
            if self.check_state.get() == 1:
                delay = 1
                search_function(self, delay)
            elif self.check_state_2.get() == 1:
                delay = 3
                search_function(self, delay)
            elif self.check_state_3.get() == 1:
                delay = 5
                search_function(self, delay)
            elif self.check_state_4.get() == 1:
                delay = 10
                search_function(self, delay)
            else:
                messagebox.showinfo(title="Message", message="Please chose one Box.")


def search_function(self, delay):
    keyboard = Controller()
    lower_L = "abcdefghijklmnopqrstuvwxyz"
    upper_L = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    sign = "!§$%&/()=*'-_<>?"
    rng_string = lower_L + upper_L + num + sign
    length = 16
    search_num = int(self.input_num.get())
    path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    webbrowser.register("edge",None, webbrowser.BackgroundBrowser(path))
    options = webdriver.FirefoxOptions()
    # options.add_argument("-headless")
    #driver = webdriver.Edge(options=options)

    if self.input_num.get() == "":
        messagebox.showinfo(title="Message", message="Please enter a Number of searches! ")
    else:
        webbrowser.get("edge").open_new("https://www.bing.com")
        #webbrowser.open_new("https://www.bing.com")
        #driver.switch_to.new_window('tab')
        # driver.get("https://www.bing.com")
        # driver.maximize_window()
        time.sleep(2)
        keyboard.press(Key.f5)
        time.sleep(1)
        for i in range(0, search_num):
            rng_search = "".join(random.sample(rng_string, length))
            keyboard.type(rng_search)
            keyboard.press(Key.enter)
            self.listbox.insert(0, rng_search)
            time.sleep(delay)
            if i == search_num - 1:
                messagebox.showinfo(title="Message", message="Done!")


MyGUI()
