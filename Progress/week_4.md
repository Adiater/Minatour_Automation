## Week 4 Progress Report
##### 13 Feb, 2019 to 19 Feb, 2019

* This week I implemented an end-to-end minimizer for Blackscholes.
  The minimizer (file minimizer.py) works with the following functions:
  * minimizer: This function is the wrapper function and also the function that is actually called by minimizer.py.
  * get_quality: This function first calls a shell script to get the quality of the input given to it (In case of blackscholes this is simply the line coverage). Then it calls a parser to actually get this quality. It returns this quality.
  * reduce_input: This is a function specifically written for Blackscholes. It cuts the input into half and returns the two halves in files temp_1 and temp_2.
<<<<<<< HEAD
  * remove: This function deletes the file given.

=======
  * remove: This function removes a given file.
  
>>>>>>> 47c4f81f83079ad5389e8ea2c2ab77192edac478
One point to note for all these files is that all paths are given relative to the folder minimizer.py is in.
