#Print Generators Performance
import random
import time
#import memory_profiler

names=['Mark','Steve','Charles','Ramesh','Tom']
majors=['Computer Science','Math','Biology','Chemistry','Art','Electrical']

def person_list(num):
    result = []
    for i in range(num):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)

                 }
        result.append(person)
    return result

def person_generator(num):
    for i in range(num):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)

                 }
        yield person

print ("Using list to create 1M items...")
start_time = time.clock()
team = person_list(1000000)
end_time = time.clock()

#print("Memory usage : {} Mb".format(memory_profiler.memory_usage()))
print("Took {} Seconds".format(end_time - start_time))

print ("Using generator to create 1M items...")
start_time = time.clock()
team = person_generator(1000000)
end_time = time.clock()

#print("Memory usage : {} Mb".format(memory_profiler.memory_usage()))
print("Took {} Seconds".format(end_time - start_time))





