



class practise:

    def __init__(self):
        print("this is constructor :: ")

    def add(self):
        print("this add method ")


a=practise()
a.add()


class emp:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("name is :: {} and age is {}".format(self.name,self.age))

b=emp("saurabh",33)
b.display()


class add:

    numb2=10
    print("numb2 ", numb2)

    def __init__(self,numb1):
        self.numb1=numb1

    def display(self):
        numb=self.numb1+self.numb2
        print("sum of two number :: {} and {} is {}".format(self.numb1,self.numb2,numb))

    print("numb1 ", numb2)
c=add(33)
c.display()








