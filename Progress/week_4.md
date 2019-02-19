## Week 4 Progress Report
##### 13 Feb, 2019 to 19 Feb, 2019

* This week I implemented an end-to-end minimizer for Blackscholes.
  The minimizer (file minimizer.py) works with the following functions:
  * minimizer: This function is the wrapper function and also the function that is actually called by minimizer.py.
  * get_quality: This function first calls a shell script to get the quality of the input given to it (In case of blackscholes this is simply the line coverage). Then it calls a parser to actually get this quality. It returns this quality.
  * reduce_input: This is a function specifically written for Blackscholes. It cuts the input into half and returns the two halves in files temp_1 and temp_2.
  * remove: This function removes a given file.
  
One point to note for all these files is that all paths are given relative to the folder minimizer.py is in.
