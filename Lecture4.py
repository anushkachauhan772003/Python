info={
    "key":"value",
    "name":"anushka Chauhan",
    "subjects":["Python", "java", "C"],#list
    "topics":("dict","set"),#tuples
    "learning":"coding",
    "age":23,
    "isAdult":True,
    "Profession":"Looking for job"
}
info["name"]="Rashi"
print(info)#Dict has no index so there is no order,MUTABLE, Duplicates not possible
#Nested dictionary
student={
    "name":"Mohit",
    "subjects":{
        "Maths":99,
        "Physics":72,
        "Chemistry":84,
    }
}
# pairs=list(student.items())
# print("pairs in dic student: ",pairs[1])
# print(student["subjects"]["Maths"])
print("USe of get method: ", student.get("name1"))# through none meanwhile will run the after code
#print("Without use of get method: ", student["name1"])#since student dic doesn't have name1 it will through error and the codes below it will stop
student.update({"city":"Delhi"})
print("updated list: ",list(student.items()))
# print(list(student.values()))
# print("items in student dict: ",list(student.items()))