class SearchEngine:
    def __init__(self, main):
        self.main = main
        self.bible_chapters = main.chapters
    
    @staticmethod
    def make_search(bible, user_request):
        for i, value in enumerate(bible):
            if value == user_request[0]:
                for i, value in enumerate(bible):
                    if value == str(user_request[0]).title() + ' ' + str(user_request[1]):
                        return str(bible[i + int(user_request[2])])
        
