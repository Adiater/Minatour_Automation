# !/bin/bash

#echo "$# $1 $2 $3"

# Removes any old .gcda files
rm $3/*.gcda
# Call the function with the given inputs and read the output in the given output file. The output file is stored in "outputs/"
command="time $1"
#echo $command
eval $command

# Variables to get the coverage of a input.
COV_DIR="cov_info/"
COV="$2_cov"
SUM="$2_sum"

# Call LCOV to get coverage. Currently, the input is specific to blackscholes.
/shared/workspace/aditikg2/TESTING_STUFF/lcov-1.13/bin/lcov --capture --directory $3 --output-file "$COV_DIR$COV"

# Create LCOV summary file for parsing.
#/shared/workspace/aditikg2/TESTING_STUFF/lcov-1.13/bin/lcov --summary "$COV_DIR$COV" &> "$COV_DIR$SUM"