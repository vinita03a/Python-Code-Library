'''
03-03-26--holi
04-03-2026
next fileExistprogram.py

write a FH program to copy one data of file to another
'''

import os 

def Read_File_Data(filename):
    if(os.path.exists(filename)):
        with open(filename,"r") as data:
            file_data = data.read()

        Paste_File_Data(file_data)

def Paste_File_Data(content):
    with open("File handling/file3.txt","w") as copy_data:
        copy_data.write(content)
    print("Content has been copeid successfully!!")

fileName = input("Enter file name : ")
Read_File_Data(fileName)