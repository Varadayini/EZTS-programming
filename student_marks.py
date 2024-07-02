class std:
    def __init__(self):
        self.name=None
        self.usn=None
        self.marks=[ ]
        self.percentage=None
        self.grade=None

    def std_input(self):
        self.name=input("enter your name : ")
        self .usn=int(input("enter your usn : "))
        for i in range(0,5):
            marks=int(input(f"enter your marks in sub {i+1}:"))
            self.marks.append(marks)
    
    def cal_percentage(self):
        sum=0
        for i in self.marks:
            sum+=int(i)
        self.percentage=(sum/500)*100

    def calc_grade(self):
        per=self.percentage
        if per<=100 and per>=80:
            self.grade="A"
        elif per<80 and per>=60:
            self.grade="B"
        elif per<60 and per>=40:
            self.grade="C"
        elif per<40 and per>=0:
            self.grade="D"
        else:
            self.grade="Invalid"

    def print_details(self):
        print("Name:",self.name)
        print("usn :",self.usn)
        print("marks in five subjects are :" ) 
        for i in range(0,5):
            print(f"subject  {i+1} = {self.marks[i]}")
        print("percentage:",self.percentage)
        print("grade : ",self.grade)    


    
        


st1=std()
st1.std_input()
st1.cal_percentage()
st1.calc_grade()
st1.print_details()

        
