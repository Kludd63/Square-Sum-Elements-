This folder contains all of the files necessary for proving that there are infinitely many sequences where pairs of integers sum to cubes instead of squares.

"cubes.sagews" has all of the functions necessary for creating a text file and generating infinitely many viable sequences.

The provided text file is sufficient to prove that there are infinitely many Hamiltonian paths on the integers from 1 to n where there is an edge between them if they sum to a cube by reusing an existing base case and glue over and over again.

The glue can be read as follows:
If the entry is an integer, then place that integer next in the sequence
If the entry starts with T, then the scale the sequence appropriately and shift by the value given after the T
If the entry starts with RT, then the scale the sequence appropriately, shift by the value given after the T, and then reverse it
