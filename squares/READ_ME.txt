This folder contains all of the files necessary for proving the square sum conjecture.

"squares_glue.sagews" is dedicated to finding glue and then creating a text file that can be read later.
"squares_base_cases.sagews" is dedicated to finding base cases for whatever glue is found and creating a text file that can be read later.
"squares_generate_sequences.sagews" is dedicated to creating sequences of any length using the text files created for glue and base cases.

The provided text files are sufficient to prove that it is possible to find a Hamiltonian path on the integers from 1 to n where they have an edge between them if they sum to a square number. The provided text files are also sufficient to show that it is possible to multiply sequences by only 9 and still find glue that can be used to prove the square sum conjecture.

The glue can be read as follows:
If the entry is an integer, then place that integer next in the sequence.
If the entry starts with T, then scale the tiny sequence appropriately and shift by the value given after the T before placing it next in the sequence.
If the entry starts with RT, then scale the tiny sequence appropriately, shift by the value given after the T, and then reverse it before placing it next in the sequence.
If the entry starts with L, then scale the long sequence appropriately and shift by the value given after the L before placing it next in the sequence.
If the entry starts with RL, then scale the long sequence appropriately, shift by the value given after the L, and then reverse it before placing it next in the sequence.
