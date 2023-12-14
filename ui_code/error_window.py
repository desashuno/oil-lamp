import tkinter as tk
from tkinter import ttk

class ErrorWindow(tk.Toplevel):
    def __init__(self, parent, error_code, error_name):
        super().__init__(parent)

        self.geometry('300x100')
        self.title(error_name)

        ttk.Button(self, text='close',command=self.destroy).pack(expand=True)


