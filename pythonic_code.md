# *Pythonic Way of writing code*

1. What is pythonic ?
Conventional guidelines that are accepted by the Python community to promote unified, maintainable, and concise applications that are written the way the language intended them to be written.

2. Use of it
# 2.1. 
Pythonic code is concise and easily understandable

example: 
a = 10
b = 1000
total_sum = 0
while b >= a:
    total_sum += a
    a += 1

Can be written as
total_sum = sum(range(10, 1001))

# 2.2.
List comprehension. This technique allows you to embed a loop inside a list to create a new list.

example:

arr = [1, 2, 3, 4, 5, 6]
length = len(arr)
for i in range(0, length):
    if arr[i] % 2 == 0:
        arr[i] *= 2

In Pythonic way:
arr = [1, 2, 3, 4, 5, 6]
arr = [x * 2 if x % 2 == 0 else x for x in arr]

# 2.3.
Tuple Unpacking

Normally, we do like this
my_tuple=('Pythonic','Code')
word_1=my_tuple[0]
word_1=my_tuple[1]

In pythonic code
word_1,word_2=my_tuple



This solution certainly works, and it would be correct in a language like C. Python, however, has a feature called multiple assignment. Instead of indexing, you can just assign all the variables in one line, and Python will unpack the tuple for you:



# Python Enhancement Proposal #8 (PEP 8) 
They are proposals written by the community designed to improve some aspect of Python, ranging from performance, to new features, and documentation.

1. Naming conventions

~Packages/Modules: Must use all-lowercase. Underscores can be used if necessary, but are discouraged. Ex: package or module.py.
~Classes: Must use CapWords. Recommended to not use the word Class in the name. Ex: class BasketballTeam:.
~Constants: Must use screaming snake case. Ex: API_URL = '...'.
~Functions/Variables: Must use standard snake case. Ex: home_team_points = ... or def final_boxscore(...).
~Function/Method Arguments: Must use standard snake case. Ex: home_team_name.

2. Proper usage of comments (PEP 257)
Usage of documentation strings (or “docstrings”) are recommended to record the purpose of functions as well describe the types, names, and descriptions of inputs and outputs, if applicable.

3. PEP 8 calls for every line of code to be less than or equal to 79 characters

example:
some_function(first_var, second_var, third_var, ... twelfth_var)

In Pyhtonic way
some_function(first_var,
              second_var,
              third_var,
              ...
              twelfth_var)

# The Zen of Python (PEP 20)
PEP20 ,written by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren’t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one — and preferably only one — obvious way to do it.
Although that way may not be obvious at first unless you’re Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it’s a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea — let’s do more of those!

Code should be written in a way that any Python developer, regardless of his or her experience, should be able to read and understand the code.

# Pythonic Style Tools

1. Linting
Linting refers to the process of automatically checking your code for errors and stylistic mistakes. 
A linting tool will flag the parts of your code that look wrong or inconsistent with PEP 8. 
You can then make fixes manually. 
There are different linters for Python, like pylint or Flake8, that you can integrate into your editor. 
IDE like Pycharm(comes with a preinstalled linter)

2. Auto-formatters
Auto-formatters like Black are more aggressive than linters, in that they do not flag your errors or inconsistencies, but they actually go in and modify your code to comply with PEP 8. 
