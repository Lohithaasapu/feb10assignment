#python program to find whether the student is pass or fail
sname=input('enter student name')
sno=int(input('enter student roll number'))
sgroup=input('enter student group')
sub1=int(input('enter English marks'))
sub2=int(input('enter Hindi marks'))
sub3=int(input('enter Evironmental Education marks'))
sub4=int(input('enter Maths marks'))
sub5=int(input('enter Physics marks'))
sub6=int(input('enter Computer Science marks'))
if  sub1>35 and sub2>35 and sub3>20 and sub4>35 and sub5>35 and sub6>35:
    print('pass')
else:
    print('fail')
