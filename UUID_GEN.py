# Imports

from datetime import date
import time
import uuid
import random

i0 = int(input("(1 sets logs to true, 2 sets logs to false!)\nplease put 1 or 2> "))

if i0 == 1:
    logs = open("Log" + str(random.randint(1, 9999)) + ".txt", "w+")
    
    #    While loop that loops through new random uuid(s)
    #    (Universally unique identifier.)
    while True: 
        id = uuid.uuid4()    
        print ("The id generated using uuid4() : ",end="") 
        logs.write(str(id) + "\n")
        print (id)

    logs.close()
elif i0 == 2:
    print("No logs!")
    while True:
        id = uuid.uuid4()
        print ("The id generated using uuid4() : ",end="") 
        print (id)       
pass