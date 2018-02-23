# Cryptography

Here is the a little bit of code to crack some coded messages (simple ones of course). 

It includes : Cesar codage, Scytale, codage by affine function, Vigenere and one by frequencies analysis on a text coded with an unknow algorithm. 

They all are about monoalphabetic coding exept Vigenere which is polyalphabetic. 
The idea is to make an automatic analysis of frequencies in order to reduce the number of possibles decoded messages, the program will choose the one that contains the most french words. So this only works with french messages, but in order to fit to other language, you can easily replace the file liste_français.txt by a file containing words in another language, you should also replace the dictionary in loss() function that contains frequency of letter in a french message. 

The messages should be without spaces, non case-sensitive, so symbols are in [a, ..., z], exept in the UnknowSource file in which coded messages should contain spaces. 

Feel free to use it, diffuse it, transform it or whatever you want. 