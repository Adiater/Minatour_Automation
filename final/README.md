# Make profile

## What does it do?
The `make_profile.sh` run script creates simics profiles for a folder full of applications. It takes in a directory containing folders of various applications. These app folders must contain a disassembly file (to be run of SPARC machine) and it should also contain shell scripts to run the program.

## How to use it?
There are just two important things one must keep in mind while using this script. One is that the aforementioned directory must be in a folder called `dir` (this folder should be in the folder containing the script). Two is that there can only be one directory in `dir` for a given run of the script.

## Examples...
An example folder is present in the `dir_example` folder to demonstrate the structure of the aforementioned directory.
