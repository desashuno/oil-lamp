from tkinter import Tk
from search_engine import SearchEngine
from get_list import GetList
from tkinter_gui import TkinterGui


class Main:
    def __init__(self):
        self.bible = []
        self.start_app()
        
    def start_app(self):
        self.get_list = GetList(self)
        self.search_engine = SearchEngine(self)
        self.launch_gui()
        
    def run(self):
        self.get_list.run()
        
    def launch_gui(self):
        self.tkiner_gui = TkinterGui(self)
        self.tkiner_gui.mainloop()

        


if __name__ == '__main__':
    main = Main()
    main.run()