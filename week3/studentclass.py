class student:
    def __init__(self,grade):
        self.__grade=grade
    def set_grade(self,mark):
        self.__grade=mark
    def get_grade(self):
        print(self.__grade)
        
s1=student(23)
s1.set_grade(78)
s1.get_grade()
