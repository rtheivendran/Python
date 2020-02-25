
from csv import reader

#Load a CSV file
def load_csv(filename):
    try:
        file = open(filename,"r")
    except IOError as e:
        print("Error in load_csv ", e)
    else:
        lines = reader(file)
        dataset= list(lines)
        file.close()
        return dataset
    finally:
         print("Done load_csv...")

#Load a CSV file using with statement
def load_csv_with(filename):
    try:
        with open(filename,"r") as file:
            lines = reader(file)
            dataset = list(lines)
            return dataset
    except IOError as e:
        print("Error in load_csv_with ", e)
    finally:
         print("Done load_csv_with...")

#Load dataset
filename = './Data/pima-indians-diabetes.csv'

dataset = load_csv(filename)
if dataset != None:
    print ("Loaded data file {0} with {1} rows and {2} columns".format(filename,len(dataset), len(dataset[0])))

dataset = load_csv_with(filename)
if dataset != None:
    print ("Loaded data file {0} with {1} rows and {2} columns".format(filename,len(dataset), len(dataset[0])))
