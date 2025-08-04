class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
   
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi",self.name,"your avg marks is",sum/3)
s1=Student("Saifaz",[95,90,91])
s1.get_avg()