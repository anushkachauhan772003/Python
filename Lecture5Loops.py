# i=1
# while(i<=5):
#     print("MAyank", i)
#     i+=1
#print the square 1-10
# i=1
# list=[]
# while(i<=10):
#     list.append(i*i)
#     i+=1
# print(list)
#search for a no. X in this tuple using loop
# tup=(1,4,9,16,25,36,49,64,81,100)
# value=int(input("enter no u are looking for "))
# indx=0
# while(indx<len(tup)):
#     if(tup[indx]==value):
#         print("found on ", indx)
#     indx+=1
#use of break and continue
i=1
while(i<=10):
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1
    
