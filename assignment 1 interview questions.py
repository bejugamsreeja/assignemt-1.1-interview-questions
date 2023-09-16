#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1
get_ipython().run_line_magic('psearch', '**kwargs')
Answer:
*args is used when the programmer is not sure about how many arguments are going to be passed
to a function, or if the programmer is expecting a list or a tuple as argument to the function.
**kwargs is used when a dictionary (keyword arguments) is expected as an argument to the function.


# In[ ]:


#2
get_ipython().run_line_magic('pinfo', 'Python')
Answer:
There are two types of functions in Python: built-in functions and user-defined functions.
Built-in functions are functions that are already defined in the Python language, such as the print() function.
User-defined functions are functions that are created by the user, and they can be created to do anything that 
the user wants them to do.


# In[ ]:


#3
get_ipython().run_line_magic('pinfo', 'closures')
Answer:
A closure is a function that remembers the values from the enclosing scope even when the program flow is no 
longer in that scope. Closures are implemented by creating a function that takes in one or more values from 
the enclosing scope and then returning a new function that uses those values.


# In[ ]:


#4
get_ipython().run_line_magic('pinfo', 'function')
Answer:
Assertions are often used in debugging to check for conditions that should never occur in normal execution.
For example, if you are working with a list, you might want to assert that the list is never empty,
or that every element in the list is greater than 0.


# In[ ]:


#5
get_ipython().run_line_magic('pinfo', 'Python')
Answer:
When more than one arithmetic operator appears in an expression the operations will execute in a specific order.
In Python, the operation precedence follows as per the acronym PEMDAS.
Parenthesis
Exponent
Multiplication
Division
Addition
Subtraction
(2+2)/2-2*2/(2/2)*2
= 4/2 -4/1*2
= 2-8
= -6
>>> (2+2)/2-2*2/(2/2)*2
-6.0


# In[ ]:


#6
What is the difference between a = 10 and a= = 10?
Answer:
The expression a = 10 assigns the value 10 to variable a, whereas a == 10 checks if the value of a is equal to 10 or not
. If yes then it returns ‘Ti^te’ else it will return ‘False’.


# In[ ]:


#7
Arrange the following operators from high to low precedence:

Assignment
Exponent
Addition and Subtraction
Relational operators
Equality operators
Logical operators
Multiplication, division, floor division, and modulus
Answer:
    
The precedence of operators from high to low is as follows:

Exponent
Multiplication, division, floor division, and modulus
Addition and subtraction operators
Relational operators
Equality operators
Assignment operators
Logical Operators


# In[ ]:


#8
get_ipython().run_line_magic('pinfo', 'operators')
Answer:
Associativity defines the order in which an expression will be evaluated if it has more than one operator 
having the same precedence. In such a case generally left to right associativity is followed.
Operators like assignment or comparison operators have no associativity and are known as Nonassociative operators.


# In[ ]:


#9
get_ipython().run_line_magic('pinfo', 'code')

numbers = [1,2,3,4] 
for i in numbers:
numbers.append(i + 1) 
print(numbers)
Answer:
This piece of code will not generate any output as the ‘for’ loop will never stop executing. In every iteration,
one element is added to the end of the list and the list keeps growing in size.



# In[ ]:


#10
Write a code to print the following pattern:
*
**
***
****
Answer:

for i in range(1,5):
print("*"*i)


# In[ ]:


#11
Write code to spell a word entered by the user.
Answer:
The code will be as follows:

word = input ("Please enter a word : ") 
for i in word: 
print (i)
Output
Please enter a word: Aeroplane
A
e
r
0
P
l
a
n
e


# In[ ]:


#12
get_ipython().run_line_magic('pinfo', 'branching')
Answer:
Deciding whether certain sets of instructions must be executed or not based
on the value of an expression is called conditional branching.


# In[ ]:


#13
get_ipython().run_line_magic('pinfo', 'Python')
Answer:
if, elif, and else


# In[ ]:


#14
get_ipython().run_line_magic('pinfo', 'Python')
Answer:
< Less than, > Greater than, <= Less than or equal to, >= Greater than or equal to,
= Equal to, != not equal, o alternative not equal. Note a single = is NOT a Python comparison operator, 
it is an assignment operator only.


# In[ ]:


#15
get_ipython().run_line_magic('pinfo', 'defined')
Answer:
All blocks in Python are defined by indenting. All lines of a particular code block must have the same level of indenting.


# In[ ]:


#16
Illustrate a switch-case equivalent using if-elif-else.
Answer:
if item=valueA:
. . .
elif item == valueB:
. . .
elif item = =  valueC:
. . .
elifitem = valueN:
. . .
else:
… #default code


# In[ ]:


#17
get_ipython().run_line_magic('pinfo', 'Python')

Answer: 
    The common built in data types in python are-

Numbers– They include integers, floating point numbers, and complex numbers. eg. 1, 7.9,3+4i

List– An ordered sequence of items is called a list. The elements of a list may belong to different data types.
Eg. [5,’market’,2.4]

Tuple– It is also an ordered sequence of elements. Unlike lists , tuples are immutable, which means they can’t be changed. 
Eg. (3,’tool’,1)

String– A sequence of characters is called a string. They are declared within single or double quotes.
Eg. “Sana”, ‘She is going to the market’, etc.

Set– Sets are a collection of unique items that are not in order.
Eg. {7,6,8}

Dictionary– A dictionary stores values in key and value pairs where each value can be accessed through its key. 
The order of items is not important. Eg. {1:’apple’,2:’mango}

Boolean– There are 2 boolean values- True and False.


# In[ ]:


#18
get_ipython().run_line_magic('pinfo', 'Python')
Answer:
Global Variables:

Variables declared outside a function or in global space are called global variables.
These variables can be accessed by any function in the program.

Local Variables:

Any variable declared inside a function is known as a local variable. 
This variable is present in the local space and not in the global space.


# In[ ]:


#19
get_ipython().run_line_magic('pinfo', 'type')
Answer:
The mutable Python data types can be modified, and they can change at runtime, for example,
a List, Dictionary, and Set. 

The immutable Python data types can not be changed or modified, and they remain unchanged 
during runtime, for example, a Numeric, String, and Tuple.


# In[ ]:


#20
What would be the output for 2*4**2? Explain.
Answer:
The precedence of** is higher than the precedence of*. Thus, 4**2 will be computed first.
The output value is 32 because 4**2 = 16 and 2*16 = 32.

