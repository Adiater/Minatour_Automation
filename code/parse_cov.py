import sys

def parse(file_name):

    print("The file name is " + file_name)
    
    f = open(file_name)
    lines = f.readlines()
    f.close()

    number = ""
    count = 0

    for line in lines:        
        if count == 2:
            is_point = False
            for i in line:
                if i.isdigit():
                    number += i
                    is_point = True
                if (i == ".") and is_point:
                    break
            break
        count += 1

    #print(number)
    return int(number)

#parse(sys.argv[1])
