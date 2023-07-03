#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 16:48:22 2023

@author: nahidferdous
"""

class Student:
    
    def __init__(self,name,age,student_id,department):
        self.name=name
        self.age=age
        self.student_id=student_id
        self.department=department
    
    def departments(self):
        
        print("The name of the department : ", self.department)
        print("Student Name : ", self.name)
        print("Student age : ", self.age)
        print("Student ID : ", self.student_id)
        
class StudentAddress(Student):
    
    def __init__(self, name, age, student_id, department, parents_name,address):
        Student.__init__(self, name, age, student_id, department)
        self.parents_name=parents_name
        self.address=address
        
    def printAddress(self):
        Student.departments(self)
        print("Student parents name: ",self.parents_name )
        print('Student parents address: ', self.address)


def main():
    name= input("Student name: ")
    age= input("Stydent age: ")
    student_id= input("Student ID: ")
    department=input("Student Department: ")
    parents_name=input("Student parents name : ")
    address=input("Student parents address: ")
    s_parents=StudentAddress(name, age, student_id, department, parents_name,address)
    s_class=Student(name, age, student_id, department) 
    print("\n         PrintAddress          ")
    s_parents.printAddress()
    print("         Department          ")
    s_class.departments()

main()