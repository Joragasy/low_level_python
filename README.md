# Low-Level-Python  Package

## Overview

This package provides a seamless way for developers to integrate and use C functions directly within Python. By leveraging this package, you can combine the performance advantages of C with the ease and flexibility of Python, enabling more efficient and powerful applications.

## Features

- **Direct Integration**: Automate C code Compilation during script execution and Easily call C functions within Python code.
- **High Performance**: Leverage C's speed for computationally intensive tasks.
- **Flexibility**: Use the best of both worlds by combining Python's simplicity with C's power.

## Installation

To install this package, you can use pip:

```bash
pip install low-level-python
```

## Example of Usage 

To use this package, follow the steps below:

0. **Write your C program***: the C program was writen in a file named 'clibrary.c'
   
    ```C
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    
    char* sayHello();
    
    char* sayHello() {
        char buffer[10];
        size_t bufferSize;
        bufferSize = sizeof(buffer);
        char* result = malloc(14); // 13 characters + null terminator
        if (result) {
            strcpy(result, "Hello, World!");
        }
        return result;
    }

    ```
2. **Import the Module**: Start by importing the necessary module from the package.

    ```python
    from low_level_python.llp_wrapper import includec 
    from low_level_python.llp_types import types
    ```

3. **Call a C Function**: You can now call the C functions within your Python code. Here’s an example:
   
    ```python
    @includec("clibrary")
    def c_func(**kwargs): 
        sayHello = clibrary.sayHello
        sayHello.restype = types["char*"]
        return sayHello()
    ```
    ```python
    c_func()
    ```
   
4. **Use the Result**: The result from the C function can be used just like any other Python variable. You can process, print, or return it as needed.

