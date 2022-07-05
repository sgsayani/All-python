class teacher:
    def __init__(self,name,subject):
        self.name= name
        self.subject=subject
    def show(self):
        print("name of the teacher is {} .He reades us {}".format(self.name,self.subject))

p1=teacher('saynai', 'CSE')
p1.show()