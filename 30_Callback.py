from time import sleep

def callback_function(i, result):
    print("Items processed: {}. Running result: {}.".format(i, result))

def square(i):
    return i * i

def processor(process, times, report_interval, callback):

    print("Entered processor(): times = {}, report_interval = {}, callback = {}".format(
    times, report_interval, callback.__name__))

    result = 0
    print("Processing data ...")
    for i in range(1, times + 1):
        result += process(i)
        sleep(1)
        if i % report_interval == 0:
            callback(i, result)

processor(square, 20, 5, callback_function)
