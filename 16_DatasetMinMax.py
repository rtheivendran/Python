from csv import reader

#Load a CSV file using with statement and removing any empty lines
def load_csv_with(filename):
    try:
        dataset = list()
        with open(filename,"r") as file:
            csv_reader = reader(file)
            for row in csv_reader:
                if not row:
                    continue
                dataset.append(row)
        return dataset
    except IOError as e:
        print("Error in load_csv_with ", e)
    finally:
         print("Done load_csv_with...")


# Min max of a dataset
def min_max(dataset):
    minmax = list()
    for i in range(len(dataset[0])):
        col_values = [ row[i] for row in dataset]
        #print(col_values)
        min_value = min(col_values)
        max_value = max(col_values)
        print("Column {0} : Min and Max values are [{1}, {2}]".format(i, min_value, max_value))
        minmax.append([min_value, max_value])
    return minmax

# Load dataset
filename = './Data/pima-indians-diabetes.csv'
dataset = load_csv_with(filename)

if dataset != None:
    print ("Loaded data file {0} with {1} rows and {2} columns".format(filename, len(dataset), len(dataset[0])))
    print(dataset[0])
    minmax = min_max(dataset)
    print(minmax)

