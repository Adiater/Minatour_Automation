## Follow these steps to run the program

The general command to get the quality is:

"python parser.py [keyword] [inputs]"

[keyword]:

* blackscholes
* swaptions
* streamcluster
* lu
* water
* fft

[inputs] : the inputs are specific to the app. The best way to understand the meaning of the inputs is to check out the comments of programs.py.

Following are a few examples of calls to a few apps:

* Blackscholes:
  
  python parser.py blackscholes 1 min_inputs/in_21.txt outputs/out
  
  In this command:
  
    * [keyword] = blackscholes
    * [inputs]:
      * number of threads = 1
      * input file = min_inputs/in_21.txt
      * output file = outputs/out
      
 * LU:
 
   python parser.py lu 512 1 16
   
   In this command:
  
    * [keyword] = lu
    * [inputs]:
      * matrix size [N] = 512
      * number of processors [P] = 1
      * blocksize [B] = 16   
