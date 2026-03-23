#List
marks1=94.4
marks2=87.5
marks3=65.5
marks4=34.4
marks5=45.6
#list
Marks=[94.4, 87.5, 65.5, 34.5, 45.6]
Cand1=["anushka", 23, 54.5]
str="Hello"
# str[0]='y'# strings are immutable whereas list are.
#List slicing 
# list_name=["str_index":end_Index]#endindex is not included
Marks[0:]
print(Marks)
list=[3,2,1,4,5]
list.append(4)
print("after eppending ",list)
list.pop(2)
print("after pop 2",list)
list.remove(3)
print("after removing index 3",list)

print(list.sort(reverse=True))#will print none, changes internally 
print(list)
print(Marks[4]) 
print("length of list: ", len(Marks))
print(str)