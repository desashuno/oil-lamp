import tkinter as tk
from tkinter import *
from tkinter import ttk

class TkinterGui(tk.Tk):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.text_label_output = 'hello'
        
        self.title('Oil lamp')
        self.geometry('300x250')
        
        self.label_title = ttk.Label(self, text='Buscador de versiculos', font=("Arial", 14)).pack()
        
        # select books
        self.combobox_book = ttk.Combobox(self, state='readonly', values=['1', '2'])
        self.combobox_book.current(0)
        self.combobox_book.pack()
        # select chapters
        
        #select versicle
        
        
        # button for seach
        self.button_search = ttk.Button(self, text='buscar')
        self.button_search['command'] = self.search_button
        self.button_search.pack()
        #self.button_search = tk.Button(self, text='Buscar', command=self.search_button).pack()
        
        self.label_output = tk.Label(self, text=self.text_label_output, font=("Arial", 14)).pack()
        
    def search_button(self):
        #call the serch engine
        self.text_label_output = self.combobox_book.get()
        print(type(self.text_label_output))
        #self.label_output["text"] = self.text_label_output
        
        