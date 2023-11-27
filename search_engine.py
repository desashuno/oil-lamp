class SearchEngine:
    def __init__(self, main):
        self.main = main
        self.bible_chapters = main.chapters
        self.actual_chapter = None

    @staticmethod
    def make_search(bible, user_request):
        for i, value in enumerate(bible):
            if value == user_request[0]:
                for i, value in enumerate(bible):
                    if value == str(user_request[0]).title() + ' ' + str(user_request[1]):
                        return str(bible[i + int(user_request[2])])
                        

    @staticmethod
    def back_and_next(bible, user_request):
        if user_request == False:
            print('back')
        if user_request == True:
            print('next')
        

