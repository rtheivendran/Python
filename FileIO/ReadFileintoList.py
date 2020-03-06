

print("Example 1: Reading a file content into a list...\n")

# Read lines in a file in a list 
fileList = list()        
with open ("data.txt", "r") as myfile:
    for line in myfile:
        fileList.append(line.strip()) 

print(fileList)


print("Example 2: Reading a file.....\n")

with open("data.txt", "r") as fileHandler:  
    # Read line
    line = fileHandler.readline()
    # check line is not empty
    while line:
        print(line.strip())
        line = fileHandler.readline()

# File should be closed so check to prove
if fileHandler.closed == False:
    print('File is not closed')
else:
    print('File is already closed')


print("Example 3: Reading a file and handling exception....\n")

# File will be closed before handling the exception
try:
    #using "with statement" with open() function
    with open('data.txt', "r") as fileHandler:
        # read file content
        data = fileHandler.read()
        # Raise a divide by zero error
        x = 1 / 0
        print(data)
except Exception as e:
    #handling exception
    print(e)
    if fileHandler.closed == False:
        print('File is not closed')
    else:
        print('File is already closed')



print("Example 4: Reading from and writing to a file...\n")

# Read from data.txt and write in outfile.txt
with open('outfile.txt', 'w') as fileW, open('data.txt', 'r') as fileR:
        data = fileR.read()
        fileW.write(data)
       
 