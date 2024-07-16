This folder contains all of the files necessary for proving that it is possible to prove a conjecture similar to the square sum conjecture but with multiples of powers of 3.

"powers_of_3_glue.sagews" is dedicated to finding glue and then creating a text file that can be read later.
"powers_of_3_base_cases.sagews" is dedicated to finding base cases for whatever glue is found and creating a text file that can be read later.
"powers_of_3_generate_sequences.sagews" is dedicated to creating sequences of any length using the text files created for glue and base cases.

The provided text files are sufficient to prove that it is always possible to find a Hamiltonian path on the integers from 1 to n where there is an edge between them if they sum to a power of 3, 5 times a power of 3, 7 times a power of 3, 13 times a power of 3, or 17 times a power of 3. While several multiples must be used to guarantee a path, it is likely possible to use fewer multiples although this combination results in few base cases and little glue.

The glue can be read using the following guidelines:
The beginning length can be determined by the number of integers present in the glue.
If the entry is an integer, then place that integer next in the sequence.
If the entry starts with T, then scale the tiny sequence appropriately, shift by the value given after the T, and remove the proper number of starting integers before placing it next in the sequence.
If the entry starts with RT, then scale the tiny sequence appropriately, shift by the value given after the T, remove the proper number of starting integers, and then reverse it before placing it next in the sequence.
If the entry starts with L, then scale the long sequence appropriately, shift by the value given after the L, and remove the proper number of starting integers before placing it next in the sequence.
If the entry starts with RL, then scale the long sequence appropriately, shift by the value given after the L, remove the proper number of starting integers, and then reverse it before placing it next in the sequence.
