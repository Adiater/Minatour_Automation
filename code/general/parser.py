import sys
import os
from programs import *

def get_rel_quality(fname, ref):
    
    cov = cov_parser(fname)
    #print(cov[0])

    l_cov = 0

    for l_num in ref:        
        if l_num in cov[0]:
            #print(l_num)
            l_cov += 1
            #print(l_cov)

    rel_quality = (float(l_cov)/float(len(ref))) * 100

    #print(rel_quality)

    return rel_quality, cov[1]
    

def cov_parser(cov_fname):

    f = open(cov_fname)
    lines = f.readlines()
    f.close()

    cov = {}

    for i in range(0, len(lines)-3):
        
        basic = lines[i].split(':')
        
        if basic[0] == 'DA':
            nums = basic[1].split(',')

            if int(nums[1]) > 0:
                cov[int(nums[0])] = int(nums[1])

    den = (lines[len(lines) - 3].split(':'))[1]
    num = (lines[len(lines) - 2].split(':'))[1]

    quality = (float(num)/float(den)) * 100

    #print(cov)
    #print(quality)

    return cov, quality

def get_quality(app_call, app_src,  *inputs):

    call = app_call_builder(app_call, *inputs)
    #print(call)

    # Call script to generate LCOV coverage file.
    os.system("sh gen_cov.sh " + "'" + str(call[0]) + "' " + str(call[1]) + " " + app_src)
    # Parse the output
    cov = cov_parser("cov_info/" + str(call[1]) + "_cov")
    os.system("rm cov_info/" + str(call[1]) + "_cov")
    print(cov[1])


def app_call_builder(app_call, *inputs):

    #print(inputs)
    #print(app_call)
    count = 0
    call = ""
    file_name = ""

    for i in app_call:
        if i == '$':
            if count >= len(inputs):
                print("The number of $ and number of inputs must match")
                return

            #print(inputs[count])
            call += str(inputs[count])
            count += 1
        else:
            call += i

    for i in inputs:
        for j in str(i):
            if (j != "/") and (j != "\\") and (j != "."):
                file_name += j

    return call, file_name



#ref = (cov_parser("cov_info/cov"))[0].keys()
#get_quality("cov_info/temp_1_cov", ref)

if len(sys.argv) < 2:
    print("Error: More arguments required")
    quit()

if sys.argv[1] not in app_call_dict:
    print("Give a valid name")
    quit()

get_quality(app_call_dict[str(sys.argv[1])], app_src_dict[str(sys.argv[1])], *sys.argv[2:])
