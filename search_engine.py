class SearchEngine:
    def __init__(self, main):
        self.main = main
        self.bible_chapters = main.chapters
        self.actual_chapter = None

    @staticmethod
    def make_search(bible, user_request, actual_chapter):
        for i, value in enumerate(bible):
            if value == user_request[0]:
                for i, value in enumerate(bible):
                    if value == str(user_request[0]).title() + ' ' + str(user_request[1]):
                        actual_chapter = i + int(user_request[2])
                        return str(bible[i + int(user_request[2])]), actual_chapter

    @staticmethod
    def back_and_next(bible, user_request, actual_chapter):
        if user_request == False:
            actual_chapter -= 1
            return bible[actual_chapter], actual_chapter
        if user_request == True:
            actual_chapter += 1
            return bible[actual_chapter], actual_chapter
        

