import sys

binary_year=b'\xC4\xEA' 
binary_month=b'\xD4\xC2' 
binary_day=b'\xC8\xD5'  

Year=binary_year.decode('gbk')
Month=binary_month.decode('gbk')
Day=binary_day.decode('gbk')

class Date:
    def __init__(self,op,date_str):
        if op=='1':
            month,day,year=date_str.split()
            self.day=int(day)
            self.month=int(month)
            self.year=int(year)
        elif op=='2':
            month_name,day,year=date_str.split()
            month_names=['January','February','March','April','May','June','July','August','September','October','November','December']
            self.month=month_names.index(month_name)+1
            self.day=int(day)
            self.year=int(year)
        elif op=='3':
            self.year=int(date_str[:date_str.find('年')])
            self.month=int(date_str[date_str.find('年')+1:date_str.find('月')])
            self.day=int(date_str[date_str.find('月')+1:date_str.find('日')])

    def show1(self):
        print(f'{self.month:02}/{self.day:02}/{self.year}')

    def show2(self):
        month_names=['January','February','March','April','May','June','July','August','September','October','November','December']
        month_name=month_names[self.month - 1]
        print(f'{month_name} {self.day:02}, {self.year}')

    def show3(self):
        print(f'{self.year}年{str(self.month)}月{str(self.day)}日')

    def show(self,op):
        if op=='1':
            self.show1()
        elif op=='2':
            self.show2()
        elif op=='3':
            self.show3()


    
sys.stdout.reconfigure(encoding='GBK')
sys.stdin.reconfigure(encoding='GBK')        

op1=input()
date_input=input()
op2=input()

date=Date(op1,date_input)

date.show(op2)

