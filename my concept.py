f=open("sheetal.txt","x")

f=open("sheetal.txt","w")
f.write ("my name is sheetal malviya")
f.close()

f=open("sheetal.txt","r")
print(f.read())