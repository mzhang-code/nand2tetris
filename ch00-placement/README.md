
Fall 2014 Intro to Computer System Project 0 
============================================

Author:     Mengyu Zhang
Mail:       mengyuzhang@uchicago.edu
Date:       Oct 15 2014

Project 0 is an utilty that remove whitespace and inline comments in the input file, and then put processed text into a target file. 

Get Started
-----------

The project is implemented in pure bash scripts, which is compatible with Linux and BSD Unix like Mac OS. There's no need to compile for use, but it has to be mentioned that because of the difference of `sed` in Linux and Max OS, I turned to `perl` command line utilty for text processing, which means `perl` is a requirement. However it should be fine because `perl` is a common pre-installed utilty in most Unix-like systems. 

Usage
-----

```
bash src/proj_0.sh file_name.in [no-comments] 
``` 

Finally, an output file named *file_name.out* will be generated in the same directory with the input file. 

Pitfalls
--------

- `echo "$str"` to keep line breaks while printing. 
- `sed` on BSD does not fully support regex matching. 

