import sys


class GetList:
    def __init__(self, main):
        self.main = main
        self.file_name = 'BIBLIA.txt'

    def run(self):
        txt_bible = self.open_file()
        list_bible = self.to_list(txt_bible)
        self.main.bible = list_bible
        

    def open_file(self):
        #try:
        file = open(self.file_name, mode='r', encoding='utf-8')
        content = file.read()
        return content
        file.close()


    def to_list(self, txt_bible):
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
    
    def to_dict(self, list_bible):
        pass
