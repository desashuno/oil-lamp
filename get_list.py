import sys
import os


class GetList:
    def __init__(self, main):
        self.main = main
        name_file = 'BIBLIA.txt'
        self.file_path = self.get_path(name_file)
        #self.file_path = name_file

        self.run()

    def get_path(self, name_file):
        print(sys.platform)
        except_mesage = 'File not found, using default path'
        if sys.platform == 'win32':
            try:
                bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
                file_path = os.path.abspath(os.path.join(bundle_dir, name_file))
                return file_path
            except:
                print(except_mesage)
                file_path = name_file
                return file_path

        elif sys.platform == 'linux':
            print(except_mesage)
            file_path = name_file
            return file_path


    def run(self):
        txt_bible = self.open_file()
        list_bible = self.create_list(txt_bible)
        books = self.get_books(list_bible)
        dict_bible = self.create_dict(list_bible, books)
        self.main.bible = list_bible
        self.main.chapters = books 


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


    def create_dict(self, list_bible, books):
        #create dict lists
        dict_bible = {}
        for i, value in enumerate(books):
            dict_bible[value] = []
        
        #put versicles and chapters
        for i, value in enumerate(list_bible):
            list_index = (len(list_bible) - 1) - i
            list_value = list_bible[list_index]
            cache_versicle_list = []
            
            #detects books (valtasar)
            if list_value in books:
                pass

            #detects chapters (gaspar)
            if 
            #detect versicles (melchor)
            

    def get_books(self, list_bible):
        chapters = []
        for i, value in enumerate(list_bible):
            if value == value.upper() and value != '':
                chapters.append(value)
        return chapters


