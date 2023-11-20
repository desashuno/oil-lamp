import tkinter as tk
from tkinter import ttk

class TkinterGui(tk.Tk):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.text_label_output = 'buscar'
        
        self.title('Oil lamp')
        self.geometry('500x250')
        
        self.label_title = ttk.Label(self, text='Buscador de versiculos', font=("Arial", 14)).pack()
        
        # select books
        self.label_book = ttk.Label(self, text='Libro', font=("Arial", 12)).pack()
        self.combobox_book = ttk.Combobox(self, state='readonly', values=self.main.search_engine.bible_chapters)
        self.combobox_book.current(0)
        self.combobox_book.pack()
        
        # select chapters
        self.label_chapter = ttk.Label(self, text='Capitulo', font=("Arial", 12)).pack()
        self.str_chapter_imput = tk.StringVar()
        self.entry_chapter = ttk.Entry(self)
        self.entry_chapter["textvariable"] = self.str_chapter_imput
        self.entry_chapter.pack()
    
        # select versicle
        self.label_versicle = ttk.Label(self, text='Versiculo', font=("Arial", 12)).pack()
        self.str_versicle_imput = tk.StringVar()
        self.entry_versicle = ttk.Entry(self)
        self.entry_versicle["textvariable"] = self.str_versicle_imput
        self.entry_versicle.pack()
        
        # button for seach
        self.button_search = ttk.Button(self, text='buscar')
        self.button_search['command'] = self.search_button
        self.button_search.pack()
        
        # label output
        self.label_output = tk.Label(self, text=self.text_label_output, font=("Arial", 14))
        self.label_output.pack()
        
    def search_button(self):
        #call the serch engine
        self.text_label_output = self.combobox_book.get()
        #self.label_output["text"] = self.text_label_output
        self.engine_response = self.main.search_engine.make_search(self.main.bible, self.text_label_output)
        self.label_output['text'] = self.engine_response
        
        