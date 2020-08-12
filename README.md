# IOVerify

This is a code testing program that tests against test cases in a `.zip` file.

# How to use

The zip archive with the test case input and output files must be structured in the following manner:
```
[archive.zip]
|
+- 1.in
|
+- 1.out
|
+- 2.in
|
+- 2.out
|
+- 3.in
|
+- 3.out
```

In this example, there are 3 test cases.

The program to test should read input from a file that has the same file name as the source code of that program, but ending with the
file extension `.in` for input and `.out` for output.

For example, for a program named `test`, the input it should read is `test.in` and `test.out`.