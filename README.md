# Graecum est; non legitur
Decoding Homework Assignment for ENGN1931Z

A key problem in communication is encoding. Devices need to have a shared methods of representing information, such as text. As you can imagine, there are lots of ways to use binary bits to represent language. Some of the most common are ASCII and UTF-8 which we will discuss in class.

Unfortunately, sometimes the codes get corrupted. For example, I should you this PDF printout problem during the first day of class. Fear not though! Since language itself has structure, we can sometimes decode even corrupted text. To demonstrate how, we will consider a simple example where the character coding has been shifted by a random integer.

Your task is to write code in Python that :

1. Queries the following URL with a HTTP Get request: [http://goo.gl/RssCBE](http://goo.gl/RssCBE)
2. Analyze the returned string to find the random shift value.
3. Correct the string to determine to what the text says.

`hw_decoding.py` is a template code for the assignment. **Please review the comments at the top of that file.**
`submit.py` is the script that will submit your code to the autograder.
`token` is a file needed for submission.

Please note you are welcome to try this assignment as many times as you would like. (There is no penalty for failed attempts, because I wanted to encourage you to practice, test, and debug.) **However, please make sure to obey the class collaboration policy --- do not share your code with others; please write and debug on your own!**
# hwDecoding
