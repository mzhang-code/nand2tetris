
Py-hackasm
==========

The **Hack** machine language assembler implemented in Python. 

The **README** is written in _Markdown_, for better reading experience, please
redirect to github page https://github.com/my-zhang/nand2tetris/tree/master/ch06-assembler/py-hackasm

## Get Started 

Check the instructions. 

```
$ cd py-hackasm 
$ bash bin/hackasm.sh --help 

usage: cli.py [-h] [-o OUTPUT] asm_file

The Hack Assembler.

positional arguments:
  asm_file              The path of input asm source file.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Specify the output file name, default is *stdout*
``` 

Then we can simply run, 

```
$ bash bin/hackasm.sh <asm_file> 
``` 

which the output will be rendered on the standard ouput. 

By specifying the output file, we can generate a hack file. 

```
$ bash bin/hackasm.sh <asm_file> -o <hack_file> 
```

For example, the directory `test` contains all the test files, 

```
$ bash bin/hackasm.sh test/asm/Pong.asm -o Pong.hack
$ diff -u test/asm/Pong.hack Pong.hack 
```

## Install 

Optionally, the assembler can be installed into host system. The install may require `root` permission. 

```
$ sudo python setup.py install
```

Then we can run `hackasm` as a system command. 

```
$ hackasm -h 
``` 

## Test 

The projects contains nearly all the test cases. The testing requires `pytest`. 

```
$ sudo python setup.py clean --all 
$ python setup.py test

running test
running egg_info
writing requirements to hackasm.egg-info/requires.txt
writing hackasm.egg-info/PKG-INFO
writing top-level names to hackasm.egg-info/top_level.txt
writing dependency_links to hackasm.egg-info/dependency_links.txt
writing entry points to hackasm.egg-info/entry_points.txt
reading manifest file 'hackasm.egg-info/SOURCES.txt'
writing manifest file 'hackasm.egg-info/SOURCES.txt'
running build_ext
=========================== test session starts =============================
platform darwin -- Python 2.7.6 -- py-1.4.20 -- pytest-2.5.2
collected 2 items 

test/test_parser.py ..

=========================== 2 passed in 0.77 seconds ========================
```

