#!/bin/bash

# This shell script takes a folder and then makes an iso from it. Then it generates
# profiles for all the apps in the iso.
# IMPORTANT: 
# The iso diretory must be placed in the ./dir/ folder and there
# should only be one directory in dir at a given time

APPROXILYZER="/shared/workspace/aditikg2/Approxilyzer" # Set the approxilyzer path
DIRECTORY="./dir/"

# Make iso from a directory from dir
iso=$(basename $DIRECTORY/*)
mkisofs -RJ -o $APPROXILYZER/workloads/iso/$iso.iso  $APPROXILYZER/workloads/iso/$iso
$APPROXILYZER/approxilyzer.sh -I $iso

# Loop through each script file in the iso
for file in `find $DIRECTORY -type f -name "*.sh"`
do
    script=$(basename "${file}")
    script=${script%.*}
    app=$(basename $(dirname "${file}"))
    dir="${app}_${script}"

    # Make checkpoints and generate app_txt_info.py
    $APPROXILYZER/approxilyzer.sh -I $iso -c $script -a $app
    mkdir $APPROXILYZER/workloads/apps/$dir
    $APPROXILYZER/approxilyzer.sh -r prof -a $dir

    # Search disassembly file for start and end address of the application
    dis=`find $(dirname "${file}") -type f -name "*.dis"`
    start=`grep 0x*: $dis | head -1`
    start=${start:4:11}
    end=`grep 0x*: $dis | tail -1`
    end=${end:4:11}

    # Replace the start and end in app_txt_info.py
    sed -i.bak "0,/0xdeadbeef/s//$start/" $APPROXILYZER/workloads/apps/$dir/app_txt_info.py
    sed -i.bak "0,/0xdeadbeef/s//$end/"$APPROXILYZER/workloads/apps/$dir/app_txt_info.py
    sed -i.bak "0,/0xdeadbeef/s//$start/" $APPROXILYZER/workloads/apps/$dir/app_txt_info.py
    sed -i.bak "0,/0xdeadbeef/s//$end/" $APPROXILYZER/workloads/apps/$dir/app_txt_info.py

    # Run profile again to generate profile
    $APPROXILYZER/approxilyzer.sh -r prof -a $dir
done