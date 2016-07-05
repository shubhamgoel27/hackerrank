# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 18:21:46 2016

@author: Shubham
"""

class Student:
    def __init__(self,firstName,lastName,phone):
        self.firstName=firstName
        self.lastName=lastName
        self.phone=phone
    def display(self):
        print "First Name:",self.firstName
        print "Last Name:",self.lastName
        print "Phone:",self.phone
        
class Grade(Student): 
    def __init__(self, firstName, lastName, phone, score):
        while len(str(phone)) !=7:
            phone = int(raw_input())
        while len(firstName) >10 or len(firstName)<4:
            firstName = raw_input().strip()
        while len(lastName) >10 or len(lastName)<4:
            lastName = raw_input().strip()
        
        Student.__init__(self, firstName, lastName, phone)
        self.score = score
        
    def calculate(self):
        if self.score<=100 and self.score>=90:
            self.grade = 'O'
        elif self.score<90 and self.score>=75:
            self.grade= 'E'
        elif self.score<75 and self.score>=60:
            self.score = 'A'
        elif self.score<60 and self.score>=40:
            self.score = 'B'
        else:
            self.score = 'D'
        
        return self.grade


firstName=raw_input().strip()
lastName=raw_input().strip()
phone=int(raw_input())
score=int(raw_input())
stu=Grade(firstName,lastName,phone,score)
stu.display()
print "Grade:",stu.calculate()           