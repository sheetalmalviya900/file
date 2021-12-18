# file=open("file-question3.txt","w")
# my_file=file.write("Kotak,\nHDFC,\nRBL,\nSBI,\nBank of Baroda")
# file.close()




# f=open("sanjana.txt","w")
# file=f.write("sanjana\nsanjana\nsanjana\nsanjana\nsanjana")
# f.close()


# f=open("sanjana.txt","a")
# file=f.write("\nyes")
# f.close()


# f=open("people_places.txt","w")
# f.write("rishabh - meerut\nrati - shimla\nayishah - delhi\nraghu - shimla\nnaseer - kanpur\nkarthikeyan - delhi\nsalma - jaipur\npankaj - delhi\nbrijesh - delhi\ngovind - delhi\npuneet - shimla\nsiddhi - delhi\nsuman - jaipur\nrajeev - shimla\nmohinder - delhi\nrajendra - jaipur\npriyanka - shimla\nneela - delhi\nsashi - jaipur\nsarika - delhi\ndeepti - shimla\nharshad - delhi\ntrishna - raipur\npradeep - jaipur\nsekhar - delhi\nnand - delhi\nanoop - delhi\nbalwinder - tokyo")
# f.close()

file=open("people_places.txt","r")
for i in file:
    if "delhi" in i:
        delhi=open("delhi.txt","a")
        delhi.write(i)
        # delhi.close()
    elif "shimla" in i:
        sh=open("shimla.txt","a")
        sh.write(i)
        # sh.close()
    else:
        other=open("other.txt","a")
        other.write(i)
        # other.close()
# print(my_file)
file.close()    