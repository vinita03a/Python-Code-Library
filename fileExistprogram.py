'''
check lecture first ---pending
03-03-26--holi
04-03-2026
write a file handling program to check if file exist or not.

'''
import os 

def Check_File(filename):
    if(os.path.exists(filename)):
        print("File exist.")
    else:
        # print("Not exist.")
        create = open(filename,"w")
    
filename = input("Enter filename : ")
Check_File(filename)