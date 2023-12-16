# Decorator

Certainly! A Python decorator is a design pattern that allows you to extend or modify the behavior of functions or methods without changing their actual code. Decorators are a powerful and flexible tool in Python, commonly used for tasks such as logging, memoization, access control, and more.

Let's break down the concept of decorators step by step:

## 1. Basics of Functions

In Python, functions are first-class objects, which means they can be passed around and used as arguments, just like any other object (e.g., integers, strings, etc.).

```python
def my_function():
    print("Hello, I am a function!")

# Assign function to a variable
func_variable = my_function

# Call the function through the variable
func_variable()  # Output: Hello, I am a function!
```

## 2. Functions as Arguments

You can pass functions as arguments to other functions.

```python
def greet(func):
    func()

greet(my_function)  # Output: Hello, I am a function!
```

## 3. Inner Functions

In Python, you can define functions within other functions.

```python
def outer_function():
    print("This is outer function.")

    def inner_function():
        print("This is inner function.")

    inner_function()

outer_function()
# Output:
# This is outer function.
# This is inner function.
```

## 4. Decorators

Now, let's create a basic decorator. A decorator is a function that takes another function as input, adds some functionality, and returns a new function.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
```

In the above example:

- `my_decorator` is a decorator function that takes `func` as an argument.
- It defines an inner function `wrapper`, which contains the code to be executed before and after calling the original function.
- The original function (`say_hello`) is decorated with `@my_decorator`, which is equivalent to calling `say_hello = my_decorator(say_hello)`.

## 5. Decorators with Arguments

Decorators can also take arguments. Here's an example:

```python
def decorator_with_arguments(prefix):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix}: Something is happening before the function is called.")
            result = func(*args, **kwargs)
            print(f"{prefix}: Something is happening after the function is called.")
            return result
        return wrapper
    return actual_decorator

@decorator_with_arguments("LOG")
def say_hello():
    print("Hello!")

say_hello()
# Output:
# LOG: Something is happening before the function is called.
# Hello!
# LOG: Something is happening after the function is called.
```

In this example, `decorator_with_arguments` is a decorator factory that returns an actual decorator. The actual decorator (`actual_decorator`) takes the original function and defines the `wrapper` function as usual.

## Conclusion

Decorators provide a clean and concise way to modify or extend the behavior of functions in Python. They are widely used in various programming scenarios and are an essential part of the Python language's flexibility and expressiveness.
