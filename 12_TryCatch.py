#Example 1: Simple try except
try:
    #f = open('test.text')
    x = y
except IOError:
    print("File Not Found....")
except Exception:
    print("Generic exception...")


#Example 2: Simple try except
try:
    #f = open('test.text')
    x = y
except IOError as e:
    print("IOError:", e)
except NameError as e:
    print("NameError: ", e)
except Exception as e:
    print("Generic Exception :",e)


#Example 1: Simple try except finally
file_name = 'data.txt'
try:
    f = None
    if (len(file_name) == 0):
        raise Exception('Invalid file name...')
    f = open(file_name)
except IOError as e:
    print("IOError....", e)
except Exception as e:
    print(e)
else:
    print(f.read())
finally:
    if f != None:
        f.close()
        print('File closed...')
    print('Finally...')
