import os
from parse_cov import parse

dir_path = os.path.dirname(os.path.realpath(__file__))

def minimizer(app, inputs, constraints = 0, target_quality = 0):
    
    if target_quality == 0:
        target_quality = get_quality(app, *inputs);

    temp_quality = target_quality
    temp_in = ["temp_1", "temp_2"]
    temp_file = inputs[0]

    while(temp_quality >= target_quality):
        
        reduce_input("inputs/" + temp_file, constraints)
        temp_quality_1 = get_quality(app, temp_in[0])
        temp_quality_2 = get_quality(app, temp_in[1])

        if temp_quality_1 < temp_quality_2:
            temp_quality = temp_quality_2
            remove("inputs/" + temp_in[0])
            remove(dir_path + "/outputs/temp_1_out")
            remove(dir_path + "/cov_info/temp_1_cov")
            remove(dir_path + "/cov_info/temp_1_sum")
            temp_file = temp_in[1]
        else:
            temp_quality = temp_quality_1
            remove("inputs/" + temp_in[1])
            remove(dir_path + "/outputs/temp_2_out")
            remove(dir_path + "/cov_info/temp_2_cov")
            remove(dir_path + "/cov_info/temp_2_sum")
            temp_file = temp_in[0]

    print("The quality achieved is " + str(temp_quality))


def get_quality(app, *inputs):
    os.system('sh get_quality.sh ' + str(app) + ' ' + str(inputs[0]))
    return parse("cov_info/" + inputs[0] + "_sum")


def reduce_input(ref, constraints = 0):

    f = open(ref, 'r')
    lines = f.readlines()
    f.close()

    count = len(lines) - 1
    new_count = count/2

    global dir_path
    out_1 = "inputs/temp_1"
    out_2 = "inputs/temp_2"

    f_1 = open(out_1, 'w+')
    f_2 = open(out_2, 'w+')

    # This could become an error later so be careful
    # It wouldn't give you an actual error but you might miss a line
    if count % 2 == 0:
        f_2.write(str(new_count) + "\n")
    else:
        f_2.write(str(new_count + 1) + "\n")
    f_1.write(str(new_count) + "\n")

    n_line_1 = False
    count = count + 1

    for i in range(1, count):

        if i <= new_count:
            f_1.write(lines[i])
        if i > new_count:
            f_2.write(lines[i])


def remove(file):
    os.system("rm " + str(file))

#reduce_input("in_64000.txt")
#print("The coverage is " + str(get_quality("/shared/workspace/aditikg2/TESTING_STUFF/parsec-3.0/pkgs/apps/blackscholes/src/blackscholes", "temp_1")))
minimizer("/shared/workspace/aditikg2/TESTING_STUFF/parsec-3.0/pkgs/apps/blackschole\s/src/blackscholes", ("ref",))
