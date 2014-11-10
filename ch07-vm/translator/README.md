# VM Translator Part I 

The basic VM Translator that parses vm code into assembler. 

This *README* is written in _Markdown_, for better reading experience, please redirect to github page https://github.com/my-zhang/nand2tetris/tree/master/ch07-vm/translator

## Requirement 

The project contains a pre-compiled jar file, thus there should be no need to run test and compile. For directly run, all you need is a `jre`. *Optionally*, for test and compile, `jdk`, `lein` and network accessibility are required. 


## Usage

Along with the source code, there's a compiled jar with all the dependencies, thus, just run the script on any *nix machine with jre installed. 

```
$ cd translator
$ bash bin/translator.sh <vm_file> 
``` 

By default, the translator print the assembly code to the standard output, however we can simply redirect the output to target file. For example, 

```
$ bash bin/translator.sh test/translator/vm/PointerTest.vm > PointerTest.asm
``` 

## Test 

The test of this project cannot be done directly, which the `CPUEmulator` involves. Under the directory `test/translator/vm` there're generated asm files, which have successfully passed the test by `CPUEmulator`. 

## License

Copyright © 2014 FIXME

Distributed under the Eclipse Public License either version 1.0 or (at
your option) any later version.

[JDK]:http://www.oracle.com/technetwork/articles/javase/index-jsp-138363.html
[Lein]:http://leiningen.org/


