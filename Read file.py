# file=open("people1-exercise.txt","r")
# my_file=file.read()
# print(my_file)
# file.close()



file=open("people2-excercise.txt","r")
count=0
for i in file:
    count+=1
print(count)
file.close()

