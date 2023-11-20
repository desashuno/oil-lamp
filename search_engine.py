class SearchEngine:
    def __init__(self, main):
        self.main = main
        self.bible_chapters = ['GÉNESIS', 'ÉXODO', 'LEVÍTICO']
    
    @staticmethod
    def make_search(bible, user_request):
        for i, value in enumerate(bible):
            if value == user_request:
                print(i)
                return value
        