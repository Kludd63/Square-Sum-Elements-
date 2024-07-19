This folder contains all of the files necessary for proving that there are infinitely many sequences where pairs of integers sum to cubes instead of squares.

"cubes.sagews" has all of the functions necessary for creating a text file and generating infinitely many viable sequences.

The provided text file is sufficient to prove that there are infinitely many sequences of the integers from 1 to n where each consecutive pair sums to a cube by reusing an existing base case and glue over and over again.

The glue can be read using the following guidelines:
The beginning length can be determined by the number of integers present in the glue.
If the entry is an integer, then place that integer next in the sequence.
If the entry starts with T, then scale the sequence appropriately, shift by the value given after the T, and remove the proper number of starting integers before placing it next in the sequence.
If the entry starts with RT, then scale the sequence appropriately, shift by the value given after the T, remove the proper number of starting integers, and then reverse it before placing it next in the sequence.
