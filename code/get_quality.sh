# !/bin/bash

INPUT="inputs/$2"
OUTPUT="outputs/$2_out"
   
rm ../parsec-3.0/pkgs/apps/blackscholes/src/blackscholes.gcda
$1 1 $INPUT $OUTPUT

COV_DIR="cov_info/"
COV="$2_cov"
SUM="$2_sum"

/shared/workspace/aditikg2/TESTING_STUFF/lcov-1.13/bin/lcov --capture --directory /shared/workspace/aditikg2/TESTING_STUFF/parsec-3.0/pkgs/apps/blackscholes/src --output-file "$COV_DIR$COV"

/shared/workspace/aditikg2/TESTING_STUFF/lcov-1.13/bin/lcov --summary "$COV_DIR$COV" &> "$COV_DIR$SUM"