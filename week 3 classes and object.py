class Person :

    def __init__(self,n,g,a):
        self.name=n
        self.gender=g
        self.age=a

    def talk(self):
        print("Hi I'm ", self.name) 

    def vote(self):
        if self.age<18 :
            print("I am not eligible to vote")
        else :
            print("I am eligible to vote")

obj1= Person("Gurpreet","Male",20)
obj2=Person("Jesse","Female",16)
obj1.talk()
obj1.vote()

obj2.talk()

