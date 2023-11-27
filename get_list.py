import sys
import os


class GetList:
    def __init__(self, main):
        self.main = main
        name_file = 'BIBLIA.txt'
        self.file_path = self.get_path(name_file)
        
        self.run()

    def get_path(self, name_file):
        if sys.platform == 'win32':
            try:
                bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
                file_path = os.path.abspath(os.path.join(bundle_dir, name_file))
                return file_path
            except:
                print('File not found')

    def run(self):
        txt_bible = self.open_file()
        list_bible = self.create_list(txt_bible)
        self.main.bible = list_bible
        self.main.chapters = self.get_chapters(list_bible) 

    def open_file(self):
        #try:
        file = open(self.file_path, mode='r', encoding='utf-8')
        content = file.read()
        return content
        file.close()


    def create_list(self, txt_bible):
        list_bible = []
        txt_bible = txt_bible.split('\n')

        # quits the enters
        for i, v in enumerate(txt_bible):
            if v != '':
                list_bible.append(v)

        # quits the spaces
        for i, v in enumerate(list_bible):
            list_bible[i] = v.strip()
        return list_bible
    
    def get_chapters(self, list_bible):
        chapters = []
        for i, value in enumerate(list_bible):
            if value == value.upper() and value != '':
                chapters.append(value)
        return chapters


