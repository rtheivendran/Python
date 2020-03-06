
def check_string_in_file(filename, search):
  
    with open(filename, 'r') as reader:
        # Read all lines in the file one by one
        for line in reader:
            # For each line, check if line contains the string
            if search in line:
                return True
    return False
 
 
def search_string_in_file(filename, search_string):

    line_number = 0
    results = []
 
    with open(filename, 'r') as reader:
        # Read all lines in the file one by one
        for line in reader:
            # For each line, check if line contains the string
            line_number += 1
            if search_string in line:
                # If yes, then add the line number & line as a tuple in the list
                results.append((line_number, line.rstrip()))
 
    # Return list of tuples containing line numbers and lines where string is found
    return results
 
 
def search_strings_in_file(filename, string_list):
    
    line_number = 0
    results = []
   
    with open(filename, 'r') as reader:
        # Read all lines in the file one by one
        for line in reader:
            line_number += 1
            # For each line, check if line contains any string from the list of strings
            for search_string in string_list:
                if search_string in line:
                    # If any string is found in line, then append that line along with line number in list
                    results.append((search_string, line_number, line.rstrip()))
 
    # Return list of tuples containing matched string, line numbers and lines where string is found
    return results


print('Example 1: Check if a string exists in a file \n')

if check_string_in_file('data.txt', 'is'):
    print('Yes, string found in file')
else:
    print('String not found in file')


print('Example 2: search for a string in file & get all lines containing the string along with line numbers \n')

matches = search_string_in_file('data.txt', 'is')

print('Total Matched lines : ', len(matches))
for elem in matches:
    print('Line Number = ', elem[0], ' :: Line = ', elem[1])


print('Example 3: Search for multiple strings in a file and get lines containing string along with line numbers \n')

matches = search_strings_in_file('data.txt', ['is', 'That', 'was'])

print('Total Matched lines : ', len(matches))
for elem in matches:
    print('Word = ', elem[0], ' :: Line Number = ', elem[1], ' :: Line = ', elem[2])