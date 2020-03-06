import sys

#Function to read a txt file
def readFile(file_name):
    if len(file_name) == 0:
        print("Next time please enter a valid filename")
        sys.exit()
    try:
        file = open(file_name, "r")
    except IOError:
        print("There was an error reading file :", file_name)
        sys.exit()
    else:
        file_text = file.readline()
        #while file_text != '':
        while file_text:
            print(file_text)
            file_text = file.readline()
        file.close()
    finally:
        print("Done reading...")

#Function to write a txt file
def writeFile(file_name):
    file_finish = "done"

    if len(file_name) == 0:
        print ("Next time please enter a valid filename")
        sys.exit()

    try:
        fp = open(file_name, "w")
    except IOError:
        print ("There was an error opening file for write", file_name)
        sys.exit()
    else:
        print ("Enter {0} when finished".format(file_finish))
        file_text = input("Enter text: ")
        while True:
            if file_text.lower() == file_finish:
                break
            fp.write(file_text)
            fp.write("\n")
            file_text = input("Enter text: ")
        fp.close()
    finally:
        print("Done writing...")

file_name = input("Enter filename: ")
writeFile(file_name)
readFile(file_name)
