class Student:
    def __init__(self,Name='',Age='',Type=''):
        self.Name=Name
        self.Age=Age
        self.Type=Type

class Undergraduate(Student):
    def __init__(self,Name='',Age='',Type='',Specialty=''):
        Student.__init__(self,Name,Age,Type)
        self.Specialty=Specialty

class Graduate(Student):
    def __init__(self,Name='',Age='',Type='',Direction=''):
        Student.__init__(self,Name,Age,Type)
        self.Direction=Direction

op_n1=int(input())
student_list={}

for _ in range(op_n1):
    name,age,type,extra=input().split()
    if type=='Undergraduate':
        student_list[name]=Undergraduate(name,age,type,extra)
    if type=='Graduate':
        student_list[name]=Graduate(name,age,type,extra)

op_n2=int(input())
res=[]

for _ in range(op_n2):
    name,quest=input().split()
    if name in student_list:
        res.append(getattr(student_list[name],quest,'none'))
    else:
        res.append('none')

for x in res:
    print(x)