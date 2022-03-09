

# file=open("bank.txt","x")
# file=open("bank.txt","a")
# banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
# i=0
# a=""
# while (i<len(banks_list)):
#     a+=banks_list[i]+"\n"
#     i+=1
# file.write(a)

file=open("bank.txt","a")
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
for i in banks_list:
    file.write(i+"\n")
