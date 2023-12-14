import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.bible = main.bible
        self.actual_chapter = self.main.search_engine.actual_chapter
        self.text_label_output = 'buscar'
        
        self.title('Oil lamp')
        self.geometry('500x250')
        self.label_title = ttk.Label(self, text='Buscador de versiculos', font=("Arial", 14)).pack()
        self.main_page()

    def main_page(self):
        # select books
        self.label_book = ttk.Label(self, text='Libro', font=("Arial", 12)).pack()
        self.combobox_book = ttk.Combobox(self, state='readonly', values=self.main.chapters)
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
        
        # button for next versicle
        self.button_next = ttk.Button(self, text='siguiente')
        self.button_next['command'] = self.next_button
        self.button_next.pack()

        # button for back versicle
        self.button_back = ttk.Button(self, text='anterior')
        self.button_back['command'] = self.back_button
        self.button_back.pack()

        # label output
        self.label_output = tk.Label(self, text=self.text_label_output, font=("Arial", 14))
        self.label_output.pack()
        
### BUTTONS ###
    def search_button(self):
        
        user_request = [] 
        user_request.append(self.combobox_book.get())
        user_request.append(self.str_chapter_imput.get()) 
        user_request.append(self.str_versicle_imput.get())
        engine_response, self.actual_chapter = self.main.search_engine.make_search(
                                                    self.bible, user_request, self.actual_chapter)
        self.label_output['text'] = engine_response
        
    def next_button(self):
        user_request = True
        engine_response, self.actual_chapter = self.main.search_engine.back_and_next(
                                                    self.bible, user_request, self.actual_chapter)
        self.label_output['text'] = engine_response


    def back_button(self):
        user_request = False
        engine_response, self.actual_chapter = self.main.search_engine.back_and_next(
                                                    self.bible, user_request, self.actual_chapter)
        self.label_output['text'] = engine_response

