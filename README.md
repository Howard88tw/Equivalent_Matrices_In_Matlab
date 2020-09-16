# Equivalent_Matrices_In_Matlab

This is a small Python script that generates equivalent input syntax for a matrix in MATLAB. The inspiration comes from the difficulties of checking students' answer for Linear Algebra exam on Canvas. 

Usage:
```
$ python generateAns.py
Please enter the matrix as MATLAB notation without any unnecessary space or commas. E.g. [3;5;6]
<< Enter your matrix in MATLAB syntax here! >>
```

Then an output file named "allPossibleAns.txt" will be generated with all equivalent syntax.

Sample run:
```
$ python generateAns.py
Please enter the matrix as MATLAB notation without any unnecessary space or commas. E.g. [3;5;6]
[1 2.3 -4;4 5 6]

# output
[ 1 2.3 -4 ; 4 5 6]
[ 1 2.3 -4 ; 4 5 6 ]
[ 1 2.3 -4 ;4 5 6]
[ 1 2.3 -4 ;4 5 6 ]
[ 1 2.3 -4; 4 5 6]
[ 1 2.3 -4; 4 5 6 ]
[ 1 2.3 -4;4 5 6]
[ 1 2.3 -4;4 5 6 ]
[1 2.3 -4 ; 4 5 6]
[1 2.3 -4 ; 4 5 6 ]
[1 2.3 -4 ;4 5 6]
[1 2.3 -4 ;4 5 6 ]
[1 2.3 -4; 4 5 6]
[1 2.3 -4; 4 5 6 ]
[1 2.3 -4;4 5 6]
[1 2.3 -4;4 5 6 ]
```


Suggestions are welcome : )
Also let me know if there's a bug. 
