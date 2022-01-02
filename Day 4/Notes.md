# Random Module

```python
#import the random module - a module made by python to assist with generating random numbers
import random
import my_module

# return number between 1 and 10(inclusive)
random_int = random.randint(1 , 10)
print(random_int)

# return random number between 0 and 1 (not inclusive)
random_float = random.random() * 5
print(random_float)

#return random number between 0 and 5
random_test = random.uniform(0, 5)
print(random_test)

# What is a module?
# a way to split large and complicated tasks into smaller bits of code.

#Creating a module is easy check my_module.py
print(my_module.pi)
```

# Lists

- A data structure used to store many pieces of related data.
- Also has an order.


```python
fruits = [item1, item2]
fruits = ["lemon", "apple", "pear"]

print(fruits[0])
> lemon

#Can have negative indices (starts at end of list)
print(fruits[-1])
> pear

#You can change the items in the list
fruits[1] = "orange"
>fruits = ["lemon", "orange", "pear"]

```
