# VM Translator Part II

The full-scale VM Translator that parses vm code into assembler. 

This *README* is written in _Markdown_, for better reading experience, please redirect to github page https://github.com/my-zhang/nand2tetris/tree/master/ch08-vm/translator

## Requirement 

The project contains a pre-compiled jar file, thus there should be no need to run test and compile. For directly run, all you need is a `jre`. *Optionally*, for test and compile, `jdk`, `lein` and network accessibility are required. 


## Usage

Along with the source code, there's a compiled jar with all the dependencies, thus, just run the script on any *nix machine with jre installed.

```
$ cd translator
$ bash bin/translator.sh <directory>
``` 

By default, the translator print the assembly code to the standard output, however we can simply redirect the output to target file. For example, 

```
$ bash bin/translator.sh test/translator/vm/FibonacciElement > FibonacciElement.asm
``` 

## Structure 

Project structure shows as follow, 

```
.
└── translator
    ├── LICENSE
    ├── README.md
    ├── bin
    │   └── translator.sh
    ├── doc
    │   └── intro.md
    ├── project.clj
    ├── resources
    ├── src
    │   └── translator
    │       ├── code_snippet.clj
    │       ├── core.clj
    │       ├── env.clj
    │       └── main.clj
    └── test
        └── translator
            ├── code_snippet_test.clj
            ├── core_test.clj
            ├── main_test.clj
            └── vm
                ├── FibonacciElement
                │   ├── FibonacciElement.asm
                │   ├── Main.vm
                │   └── Sys.vm
                └── StaticsTest
                    ├── Class1.vm
                    ├── Class2.vm
                    ├── StaticsTest.asm
                    ├── StaticsTest.cmp
                    ├── StaticsTest.out
                    ├── StaticsTest.tst
                    ├── StaticsTestVME.tst
                    └── Sys.vm

```

where `src/translator/main.clj` is the entry point of the translator, `core.clj` is contains marjor logic of parsing expressions and `code_snippet.clj` contains code segments for code generation. `test` directory contains several testcases, where there're also generated `*.asm` files. 

## License

Copyright © 2014 FIXME

Distributed under the Eclipse Public License either version 1.0 or (at
your option) any later version.

[JDK]:http://www.oracle.com/technetwork/articles/javase/index-jsp-138363.html
[Lein]:http://leiningen.org/


