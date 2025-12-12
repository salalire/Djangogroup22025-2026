class library:
    def __init__(self):
        self.booklsit=[]
    def add_books(self,book):
        self.booklsit.append(book)
    def show_books(self):
        for book in self.booklsit:
            print(book)
            
            
l=library()
l.add_books("extremeseries")
l.add_books("sciencebooks")
l.add_books("fictions")
l.show_books()
        
