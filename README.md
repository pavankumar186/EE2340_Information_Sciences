# EE2340_Information_Sciences
Program written in python for calculating the entropy of file
The given problem statement was as follows

1.6. Write a program to do the following: given an input text file , compute the empirical
pmf/histogram of the characters in the file (i,e., the fraction of ‘a’, ‘b’, etc.). The program should print the
empirical pmf as a 26-length vector corresponding to letters in the English alphabet.

The empirical pmf of a sequence is also called the type of the sequence.

2.7. In the previous assignment, you wrote a program to compute the empirical pmf/frequency
of letters in a text file. Modify that program to first compute the frequency of all ASCII characters (all
256 possible ASCII characters including newline, space, carriage return) in the file, and then compute the
entropy of the text file (be careful with 0 log 0 errors). Also count the total number of characters in the file.
Your program should print the number of ASCII characters in the file, and the entropy. Attach the program
as a separate file.
Note that typically each ASCII character is represented using 1 byte (8 bits). This should give a lower bound
on the compressed file size if the characters are iid:

optimal compressed filesize in bytes = number of characters in file  * entropy/8

Compute the entropy for the two attached text files file1.txt (consists of randomly generated iid ASCII
characters) and file2.txt (a copy of the book “War and Peace” by Leo Tolstoy). Also compress them using
zip and compare the filesizes with what you have from the above.
Is there a significant difference between the zipped file and the computed optimal compressed filesize for the
two cases? Why?
