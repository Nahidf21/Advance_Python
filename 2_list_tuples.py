# lists are mutable 
# tuples are not mutable 

MylistOne = [1,2,3,45,67,8,3.5]
print(MylistOne)


MylistOne[1]=12
print(MylistOne[1])
print(MylistOne *2)

# Tuples - Read only list 

myTupleOne= (4,"Nahid",3,12)
myTupleTwo= (5,"Ferdous",3,13)

print(myTupleOne)
print(myTupleOne[0:2])
print(myTupleOne *2)
myTupleOne[1]=3
