'''
after Exception try except

file handling - working with files(.txt , .py , .json ,html etc  )using 
python to create, update, delete permanently

syntax :
var_name = open(filename, mode)

mode : 
read  - r
write - w
read + write - r+
appebd - a 
read binary - rb 

'''
# read mode

# next -----text.txt

read_data = open("File handling/text.txt","r")
print(read_data.read(20))
read_data.close()

print()

read_data1 = open("File handling/text.txt","r")
print(read_data1.readlines())
read_data1.close()

print()

read_data2 = open("File handling/text.txt")
print(read_data2.readlines())
read_data2.close()

# write mode - no need of file existence

write_data = open("file.py","w")
write_data.write("'''This is write mode file!!'''")
write_data.close()

#  read binary  and read + write 
#  like image upload---hw