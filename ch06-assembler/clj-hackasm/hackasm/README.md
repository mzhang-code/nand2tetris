
clj-hackasm
===========

A Clojure implementation of **Hack** assembler. 

This *README* is written in _Markdown_, for better reading experience, please redirect to github page https://github.com/my-zhang/nand2tetris/tree/master/ch06-assembler/clj-hackasm

## Requirement 

The project contains a pre-compiled jar file, thus there should be no need to run test and compile. For directly run, all you need is a `jre`. *Optionally*, for test and compile, `jdk`, `lein` and network accessibility are required. 

## Usage

```
$ cd clj-hackasm/hackasm 
$ bash bin/hackasm.sh <asm_file> 
``` 

By default, the assembler print the machine code to the standard output, however we can simply redirect the output to target file. For example, 

```
$ bash bin/hackasm.sh test/hackasm/asm/Rect.asm > Rect.hack 
$ diff -u test/hackasm/asm/Rect.hack Rect.hack 
``` 

## Test and Compile 

As mentioned in **Requiredment**, optionally, we can test and compile the project with `jdk` and `lein`. There're links for the setup of [JDK] and [Lein]. 

The testcases inlcude all of the test files in ch06. 

```
$ lein test

lein test hackasm.core-test

lein test hackasm.inst-test

lein test hackasm.symbol-table-test

Ran 7 tests containing 18 assertions.
0 failures, 0 errors.
``` 

And for compile source files into standalone jar file: 

```
$ lein uberjar
``` 

[JDK]:http://www.oracle.com/technetwork/articles/javase/index-jsp-138363.html
[Lein]:http://leiningen.org/


