class marks:
    def __init__(self,name,standard):
        self.name=name
        self.standard=standard
        self.__marks=0
    def getmathmarks(self):
        print("The marks scored are : ",self.__marks)
    def setmathmarks(self,marks):
        self.__marks=marks
s1=marks("kouhsik",10)
print("The student name is :",s1.name)
s1.setmathmarks(100)
s1.getmathmarks()

