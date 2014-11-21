
Jack Compiler, the Frontend
===========================

The frontend of the Jack program compiler converts programs into *abstract syntax tree*, which is also named *parse tree*. 


Usage
-----

unzip the submitted file, and `cd` to the project directory, you'll see, 

```
$ ls 
README.md jcompiler setup.py  test
```

Then run following command to parse a jack file and generate corresponding xml file. 

```
$ python jcompiler/cli.py [INPUT_JACK_FILE]
``` 

The xml content will display on `stdout` by default. To obtain an xml file, you can simply add an redirection, 

````
$ python jcompiler/cli.py [INPUT_JACK_FILE] > [OUTPUT_XML_FILE] 
``` 

Requirement
-----------

python 2.7 

