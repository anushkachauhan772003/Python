#Set is the collection of unordered items and unique and immutable
nums={1,2,3,4,5}
set2={1,222,222,2223}
#how to write empty set
collection={}#this is empty dictionary syntax
collection2=set()# this is synatx of empty set 
print(type(collection))
print(type(collection2))
# set is muatble meanwhile its elements is immutable
collection2.add(1)
collection2.add(2)
collection2.add(3)
collection2.add(4)
collection2.remove(4)
print("items in collection 2: ", collection2)
#Lets practice
DIC={
    "table": ["a peice of furniture", "list of facts and figures"],
    "cat": "a small animal"

}
print("items of DIC=",DIC.items())

subjects={
    "python","java","c++","python","javascript","java","python","java","c++","c"
}
print("subjects=",len(subjects))
#wap to take input of 3 subjetcs
subject={
    "chemistry": int(input("enter chemistry marks: ")),
    "Maths":int(input("enter marks of maths subject: ")),
    "Physics":int(input("enter marks of physics: "))
}
print(subject)