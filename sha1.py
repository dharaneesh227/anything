from Crypto.Hash import SHA1
h1=SHA1.new()
h2=SHA1.new()

file1=input("Enter the name of file 1 : ")

file2 = input("Enter the name of file2 : ")

file1= open(file1,"r").read()
print("File 1 Contents :\n ",file1)

file2 = open(file2,"r").read()
print("File 2 Contents :\n ",file2)

h1.update(file1.encode("utf-8"))

h2.update(file2.encode("utf-8"))

if(h1.hexdigest()==h2.hexdigest()):
	print("The files match")
else:
	print("The files do not match")