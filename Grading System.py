from collections import namedtuple 
import numpy as np


Student = namedtuple('Student',['studentID','fullname','dob','gender','contact'])
students = [] # list to store student details

with open('HackathonPrep\students.txt', 'r') as file:
    for line in file:
        info = line.strip().split(',')# using a , based on how the .txt filed was written, splitting the lines on every comma
        students.append(Student(*info)) #*data makes sure all the fields in the Student namedtuple are filled otherwise you get a missing argument error
        

for student in students:
    print(student)