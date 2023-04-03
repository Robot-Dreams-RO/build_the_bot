#########################
1. Introduction to Python
#########################

======================================
0. Does it make sense to learn Python?
======================================

YES

More about on:
   
    - `StackOverflow Survey <https://insights.stackoverflow.com/survey>`_ 
    - `IEEE Spectrum <https://spectrum.ieee.org/top-programming-languages-2022>`_ 

+++++++++++++++++++++++++++++++
1. Is Python the best language?
+++++++++++++++++++++++++++++++

**No**. There are no best languages.

Every language has pros and cons.

   - **Pro**: 
      - easy to learn
      - easy to code
      - has support from the community

   - **Con**: 
      - not fast or too performant
      - needs libraries on locally to run
      - management of libraries versions is weird

-------------------------------------------------
Why do **I** use Python and not another language?
-------------------------------------------------

Python is an **efficient language**: my applications will do more in fewer lines of code than many other languages would require. I can build cli applications, machine learning algorithms, and cloud microservices. And the community - I believe in **opensource** and its ability to deliver good alternatives.

++++++++++++++++++
2. Python features
++++++++++++++++++

* **Simple** - has a minimalist feel, the code feels like pseudo-code, allowing developers to concentrate on solving the problem not on writing the code. 
* **Easy to use** - most of the components are easy to pick up
* it's **FLOSS** - Free/Libre and Open Source Software
* **High-level** Language
* **Portable**
* **Interpreted**
* **Object-oriented** - everything in Python is an object
* **Extensive libraries** - from the web apps to ml - it does all

.. note::
   **Naming convention** - the Python programming language was named after the BBC program "Monty Python's Flying Circus" by Guido van Rossum.

++++++++++++++++++
3. Python versions
++++++++++++++++++

`Release notes <https://docs.python.org/3.11/whatsnew/index.html>`_  - what is new in every version? 

When to update?

1. when new features are needed

   - bugs are solved
   - performance is improved
   - newly added APIs that you may or may not need

2. when bored and you don't have work to do

++++++++++++++
4. How to code
++++++++++++++

**The Style Guide**
   A Python Enhancement Proposal is written when someone wants to alter the Python programming language (PEP).

   PEP 8, which teaches Python programmers how to style their code, is one of the first PEPs.

   Read more about the Python conventions at https://peps.python.org/pep-0008/


**Indentation**
   Per level of indentation, PEP 8 advises using four spaces.
   Four spaces allow for many levels of indentation on each line while also improving readability.
   People frequently indent text in word-processing documents using tabs rather than spaces.
   While this is effective for word-processing documents, the Python interpreter becomes confused when tabs and spaces are used together. 

**Line Length**
   The rule of thumb among Python programmers is that lines should be no more than 80 characters.
   Because most computers could only fit 79 characters on a single line in a terminal window, this rule originated in the past.
   Even if people can currently fit considerably longer lines on their devices, there are still good reasons to stick with the 79-character limit.
   Professional programmers frequently have multiple files open on the same screen, and by using the standard line length, they can see the whole line in two or three open files onscreen.
   Because some of the tools that automatically generate documentation for larger projects add formatting characters at the beginning of each comment line, PEP 8 also advises that you keep all of your comments to a maximum of 72 characters per line. 

**Blank Lines**
   Use blank lines to visually group the various components of your application.
   To arrange your files, utilize blank lines, but don't use them frequently. 

+++++++++++++++++
The Zen of Python
+++++++++++++++++

Experienced Python programmers will encourage you to avoid complexity and aim for simplicity whenever possible. The Python community's philosophy is contained in “The Zen of Python” by Tim Peters. You can access this brief set of principles for writing good Python code by entering import this into your interpreter.

.. code-block:: python

   python3.11

   # then run
   import this

===============
1. Installation
===============

+++++++++++++++++++++++++++
Install on WSL(Ubuntu22.04)
+++++++++++++++++++++++++++

Python is already installed on your machine (the Linux Kernel is using it) - with version 3.10.
Because Python3.11 has a major performance improvement - we want it.

.. code-block:: bash

    # Add deadsnakes(from old versions of Python) repository
    # More information about deadsnakes https://github.com/deadsnakes/
    sudo add-apt-repository ppa:deadsnakes/ppa

    # Refresh the cache using the below command.
    sudo apt update 

    # And install Python 3.11 using the below command.
    sudo apt install python3.11 python3.11-venv -y

In order not to affect the Kernel, we use virtual environments.

Applications written in Python frequently use packages and modules that are not included in the standard library.
Applications will sometimes require a particular version of a library because they may need a specific issue to be solved or they may have been created using an outdated version of the library's interface.

Making a virtual environment—a self-contained directory tree including a Python installation for a certain version of Python and several additional packages—is the answer to this issue.

In Python we normally don't use as much docker when deploying/running applications - we use Virtual Environment

More about virtual environments: https://docs.python.org/3/tutorial/venv.html

.. code-block:: bash

   python3.11 -m venv venv
   source venv/bin/activate

   # Once in venv run
   python3.11
   
   # Write your hello world
   print("Hello World")

   # To exit
   # Control+D or write exit()

   # Care about the different versions of Python
   # If you run
   python
   # or
   python3
   # or
   python3.10
   # or
   python3.11

   # That means our shebang will be different
   #!/usr/bin/env python3.11

+++++++++++++++++++++++++++
Set Default Python Versions
+++++++++++++++++++++++++++

.. note::

    You can install multiple versions of Python in Linux distros, but the default can only be one version.

.. warning::

    Make sure you know which applications depend on Python 3.10, because you can break some application

You can easily find it out using apt-cache rdepends command as below.

.. code-block:: bash

    apt-cache rdepends python3.10

Create symbolic links for the executable and set it up as the default

.. code-block:: bash
    
    # Use update-alternatives to create symbolic links to python3
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1

    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2

    # And choose which one to use as Python3 via the command:
    sudo update-alternatives --config python3

+++++++++++++
Where to code
+++++++++++++

--------------------------
1. Python's embedded shell
--------------------------

   Why???

-----------------
2. Microsoft code
-----------------

A powerful, lightweight free code editor with integrated tools to easily deploy your code to Azure. - https://code.visualstudio.com/

PRO:
    - lots of extensions
    - available Linux and Windows
    - can run code on WSL
    - support for Azure, docker, and Kubernetes
CON:
    - some extensions are behind a paywall
    - you need to tune it before it's amazing

-------------------
3. Jupyter Notebook
-------------------

JupyterLab is the latest web-based interactive development environment for notebooks, code, and data. Its flexible interface allows users to configure and arrange workflows in data science, scientific computing, computational journalism, and machine learning. A modular design invites extensions to expand and enrich functionality. - https://jupyter.org/

It's Python-based so you need to install it using pip

.. code-block:: bash

    # If you have not created and activated venv
    python3.11 -m venv venv
    source venv/bin/activate
    
    # Install 
    pip install jupyter

    # Run
    jupyter notebook

    # Copy the link into a browser

PRO:
    - it allows you to start and play with code
    - is amazing for data science/ml or if you're trying to visualize data
    - can be run on a server and multiple people can access it
    - is embedded into Microsoft Code
CON:
    - it's not for OOP programming
    - hard to work if the feed will grow too much

================================
2. Variables and Data structures
================================

+++++++++
Variables 
+++++++++

Variables Are Labels - Variables are often described as boxes you can store values in - a variable reference a certain value.

When declaring a variable we use the syntax: `name = value`

.. code-block:: python

   x = 1

We can also do multiple assignments

.. code-block:: python

   x, y, z = "A", "B", "C"

   print(x, y, z)

------
Naming
------

When you are using variables in Python, you need to adhere to a few rules and guidelines. Breaking some of these rules will cause errors; other guidelines just help you write code that is easier to read and understand. Be sure to keep the following variable rules in mind:

   - Variable names can contain only **letters**, **numbers**, and **underscores**.
   - Variable names are **case-sensitive** (``name``, ``Name`` and ``NAME`` are three different variables)
   - They can start with a **letter or an underscore**, but not with a number. For instance, you can call a variable ``name_1`` but not ``1_name``.
   - **Spaces are not allowed** in variable names but underscores can be used to separate words in variable names. For example, ``first_name`` works, but ``first name`` will cause errors.
   - **Avoid using Python keywords** and function names as variable names; that is, do not use words that Python has reserved for a particular programmatic purpose, such as the word print. Read more:  https://docs.python.org/3/reference/lexical_analysis.html#keywords
   - Variable names should be **short but descriptive**. For example, ``name`` is better than ``n``, ``first_name`` is better than ``f_n``, and ``name_length`` is better than ``length_of_persons_name``.
   - Be careful when using the lowercase letter ``l`` and the uppercase letter ``O`` because they could be confused with the numbers ``1 and 0``.

------------------
Naming conventions 
------------------

In **Python** naming conventions will not affect your code, but will affect your way for working in the team (in other languages naming convention matters)

We have 4 different ways of declaring:

1. **Snake case** (ex: some_variable) 
2. **Screaming Snake case** (ex: SOME_VARIABLE)
3. **Pascal case** (ex: SomeVariable)
4. **Camel case** (ex: someVariable)

Read more about the Python conventions at https://peps.python.org/pep-0008/

**I** use them like this:

- **Snake case** - for functions, methods, attributes, and variables (this is the preferred way in Python)

Function names should be lowercase, with words separated by underscores as necessary to improve readability.

Is preferred ``def function_name():`` not ``def functionName():``.

.. code-block:: python
   
   first_name = input("Enter your name: ")

- **Screaming Snake case** - Constants  

.. code-block:: python
   
   PI = 3.14

- **Pascal case** - defining class name.

.. code-block:: python
   
   class Student:
      def __init__(self, name, age): 
         self.name = name
         self.age = age

      def displayInfo(self): # class method
         print('Student Name: ', self.name,', Age: ', self.age)

- **Camel case**- to name some methods (ex: toJson, fromFile, updateFile) - because when you are using them they look like this ``Student.displayInfo``

++++++++++
Data types
++++++++++

In Python 3.6, PEP 498 introduces a new kind of string literals: f-strings, or formatted string literals.

Read more about f-strings https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498

----------
1. Strings
----------

In Python, strings are enclosed in either single or double quotation marks. Single quotes will not let variables pass, so be careful.

.. code-block:: python
   
   single_name = 'skillab'
   doubleName = "skillab"

   print("Course name is " + single_name)
   # or
   print(f"Course name is {single_name}")

~~~~~~~~~~~~~~~~~~~
String Manipulation
~~~~~~~~~~~~~~~~~~~

.. code-block:: python
   
   print("skillab".title())

   name = "skillab"

   print(name.title())
   print(name.lower())
   print(name.upper())
   print(name.replace('a','A'))

   # How to find out all the available alternatives
   dir(name)

~~~~~~~~~~~~~
Magic methods
~~~~~~~~~~~~~ 

``__len__()``

One of the many magic methods in the Python programming language, ``__len__`` is primarily used to implement the ``len()`` function because every time the ``len()`` function is called, the magic method ``__len__`` is also called internally.

After all, is said and done, it returns an integer value larger than or equal to zero, which is the length of the object for which it was called. 

.. code-block:: python
   
   print("skillab".__len__())
   print(len("skillab"))

----------
2. Numbers
----------

Python supports two types of numbers:

 - integers(whole numbers)
 - floating point numbers(decimals).

.. code-block:: python
    
   # When declaring a variable we use the syntax
   # name = value
   x = 1
   xint = int(x)
   xfloat = float(x)
   universe_age = 14_000_000_000

   print(x)
   print(xint)
   print(xfloat)
   print(universe_age)

   print(type(x))
   print(type(xint))
   print(type(xfloat))

   print(dir(x))
   print(dir(xint))
   print(dir(xfloat))

~~~~~~~~~~~~~~~~~
Number operations
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # add 
   print(1+2)
   # subtract
   print(1-2)
   # multiply
   print(1*2)
   # divide
   print(1/2)
   # modulo
   print(1%2)

--------
3. Lists
--------

A list is a collection of objects in a specific sequence.
A list can contain anything you want, and there is no requirement that the items on it link to one another in any specific way.
It's a good idea to name your list in the plural, such as letters, numerals, or names, because lists typically contain many elements.

.. code-block:: python

   animals = ["cat", "dog", "python"]

   print(animals)

   # Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired. To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.
   print(animals[2])

   # You can also format the result
   print(animals[2].title())

~~~~~~~~~~~~~~~~~
List Manipulation
~~~~~~~~~~~~~~~~~

The majority of lists you create will be dynamic, meaning that when your program executes, you'll add, update and remove items from the list you've created. 

.. code-block:: python

   # Add elements
   animals.append("monkey")
   print(animals)

   # Insert an element at any position
   animals.insert(0, "rabbit")
   print(animals)

   # Remove elements by position
   del animals[3]
   print(animals)

   # Removing an Item Using the pop() Method
   # Example want to remove a user from a list of active members and then add that user to a list of inactive members.
   # pop() with no argument last element
   # pop(1) 2nd element
   popped_animal = animals.pop()

   # Remove elements by value
   animals.remove("python")

.. warning:: 

   Only the first instance of the value you specify is removed by the ``remove()`` method.
   You'll need to use a loop if there's a chance that the value could appear more than once in the list to ensure that all instances are eliminated.

.. code-block:: python

   digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
   min(digits)
   max(digits)
   sum(digits)

~~~~~~~~~~~~~~~~~
List Organization
~~~~~~~~~~~~~~~~~

Because you can't always control the order in which your users submit their data, your lists will frequently be generated in an unpredictable order.

.. code-block:: python

   animals = ['rabbit', 'cat', 'dog', 'python', 'monkey']
   # how long is the list
   len(animals)
   
   print(animals)

   animals.sort()
   animals.sort(reverse=True)

   # sort() is an irreversible procedure
   # if you need something temporary without affecting the original list use sorted(list_name)
   print("Here is the original list:")
   print(animals)

   print("\nHere is the sorted list:")
   print(sorted(animals))

   print("\nHere is the original list again:")
   print(animals)

.. warning::

   When all the values are not lowercase, sorting a list alphabetically becomes a little more challenging.
   When determining a sort order, capital letters can be interpreted in a variety of ways, and specifying the precise order can be more difficult than we want to handle right now.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Avoiding Index Errors When Working with Lists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you are working with lists for the first time, one type of error is frequent to see is Index error.

.. code-block:: python

   animals = ['rabbit', 'cat', 'dog', 'python', 'monkey']

   print(animals[5])

   # Instead of using last element by explicitly using position value we can use
   print(animals[-1])

---------------
4. Dictionaries
---------------

In Python, a dictionary is a collection of key-value pairs.
Each key has a value associated with it, and you may use a key to get that value.
The value of a key could be an integer, string, list, dictionary, or even another dictionary.
In actuality, you may use any Python-created object as a value in a dictionary.

.. code-block:: python

   animals = { 'reptile': 'python', 'primates': 'monkey', 'mammal': 'dog'}
   
   # Accessing elements using key
   animals['primates']

   # Accessing keys
   animals.keys()

   # Accessing values
   animals.values() 

   # Loop through dictionary values
   for animal in animals.values():
      print(animal.title())

   muscle_cars = {
   "brand": "Dodge",
   "model": "Challenger",
   "year": 1970
   }

   # Add new elements in dictionary
   muscle_cars["color"] = "black"

   # Update dictionary
   muscle_cars.update({"color": "red"})

   # Remove items
   # `pop()` method removes the item with the specified key name
   muscle_cars.pop("color")

   # `popitem()` method removes the last inserted item
   muscle_cars.pop("year")

   # `del` keyword removes the item with the specified key name
   del muscle_cars["model"]

   # clear() method empties the dictionary
   muscle_cars.clear()

=========================
3. Loops and conditionals
=========================

++++++++++++++
If Conditional
++++++++++++++

.. code-block:: python

    animals = ['rabbit', 'cat', 'dog', 'python', 'monkey']

    if 'python' in animals:
        animals.remove('python')
        print(animals)
        
    if "whale" not in animals:
        animals.append("whale")
        print(animals)

    # Checking that a list is not empty
    animals = []
    print(animals)
    if not animals:
        animals.append("python")
        print(animals)
    else:
        print(animals)

++++++++
For loop
++++++++

.. code-block:: python
    
    animals = ['rabbit', 'cat', 'dog', 'python', 'monkey']

    # Looping string lists
    for animal in animals:
        print(animal)

    # Loop numeral lists
    for value in range(1, 5):
        print(value)
    
    # Creating a new list
    squares1 = []
    for value in range(1, 11):
        square = value ** 2
        squares1.append(square)
    
    print(squares1)

    # List Comprehensions
    squares2 = [value**2 for value in range(1, 11)]

    print(squares2)

.. note::
    
    Four lines of code were used in the older method for creating the list squares.
    With just one line of code, you can create the same list using list comprehension.
    A list comprehension automatically appends each new element and condenses the for loop and production of new elements into a single line.

++++++++++
While loop
++++++++++

You can use a while loop to count up through a series of numbers. For example, the following while loop counts from 1 to 5:

.. code-block:: python
    
    current_number = 1
    while current_number <= 5:
        print(current_number)
        current_number += 1

    # Running while true until break
    user_input = "\nPlease enter the name of a country you have visited:"
    user_input += "\n(Enter 'exit' when you are finished.) "

    while True:
        country = input(user_input)

        if country == 'exit':
            break
        elif country == 'romania':
            continue
        else:    
            print(f"I'd love to go to {country.title()}!")

========================
4. Libraries and modules
========================

A Python library is a collection of related modules, that contains code that can be reused in different programs.

---------------
Using libraries 
---------------

.. code-block:: python
    
    import datetime

    today = datetime.datetime.today()
    print(f"{today:%B %d, %Y}")

How can I make sure that a library is secure, performant, and up-to-date?

This is a challenge, but the easiest is to go to the library github's project and review the code.

Also, you can use tools like https://debricked.com/select/ that will give you a summary of that project.

We consider a library to be used if it's updated in the last couple of months if has many and varied committers if has lots of active PRs.

============
5. Functions
============

Functions - blocks of code that are designed to do one specific job.

---------------
Using functions 
---------------

.. code-block:: python
    
    def hello_world():
        """Display a simple greeting.
        
        Args:
            None

        Returns:
            None
        """
        print("Hello World!")

    hello_world()

Passing arguments to the function

.. code-block:: python
    
    def hello_name(username):
        """Display a simple greeting with one parameter.
        
        Args:
            username (str): The username of your user

        Returns:
            None
        """
        print(f"Hello World {username.upper()}!")

    hello_name('skillab')

~~~~~~~~~~~~~~~~~~
Multiple arguments
~~~~~~~~~~~~~~~~~~

A function call would require multiple arguments since a function specification could contain many parameters.
There are many different ways to give arguments to your functions: 
- keyword arguments, where each argument consists of a variable name and a value, lists and dictionaries of values
- positional arguments, which must be in the same order as the parameters were written.

.. code-block:: python
    
    # Positional arguments
    def hello_name(username, email):
        """Display a simple greeting with 2 parameters.
        
        Args:
            username (str): The username of your user
            email (str): The email of your user

        Returns:
            None
        """
        print(f"Hello World {username.upper()} with {email.upper()}!")

    hello_name('skillab', 'admin@skillab.com')

    # Keyword arguments
    def hello_name(username, email):
        """Display a simple greeting with 2 parameters.
        
        Args:
            username (str): The username of your user
            email (str): The email of your user

        Returns:
            None
        """
        print(f"Hello World {username.upper()} with {email.upper()}!")

    hello_name(username='skillab', email='admin@skillab.com')
    hello_name(email='admin@robotdreams.com', username='robotdreams')

    # Best practice is to specify default values and also document them
    def hello_name(username='skillab', email='admin@skillab.com'):
        """Display a simple greeting with 2 parameters.
        
        Args:
            username (str): The username of your user
            email (str): The email of your user

        Returns:
            None
        """
        print(f"Hello World {username.upper()} with {email.upper()}!")

    hello_name(email='admin@robotdreams.com', username='robotdreams')
    hello_name(username='robotdreams')
    hello_name()

~~~~~~~~~~~~~
Return Values
~~~~~~~~~~~~~

A function's result should not always be displayed on the screen.
A value or combination of values may be returned after processing some data, as an alternative.
A return value is a value that the function returns.
A value is taken from a function's return statement and sent back to the line that is called the function.
Return values let you relocate a lot of your program's manual tasks into functions, which can reduce the code itself.

.. code-block:: python

    def hello_name(username='skillab', email='admin@skillab.com'):
        """Display a simple greeting with 2 parameters.
        
        Args:
            username (str): The username of your user
            email (str): The email of your user

        Returns:
            string: a string with information about the user and mail
        """
        return f"Hello World {username.upper()} with {email.upper()}!"

    hello_world = hello_name()

==========
6. Classes
==========

Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data and code. The data is in the form of fields (often known as attributes or properties), and the code is in the form of procedures (often known as methods).

Generating an object from a class is called instantiation.
You work with instances of a class, which are created by the process of instantiating an object from a class. 

.. code-block:: python
    
    class Student:
        """
        A class is used to represent a student.

        ...

        Attributes
        ----------
        name: str
            the name of the students
        age: int
            the age of the students

        Methods
        -------
        learn()
            Simulate a student's learning.
        take_exam()
            Simulate taking over good results.
        """

        def __init__(self, name, age):
            """Initialize name and age attributes.
            
            Attributes
            ----------
            name: str
                the name of the students
            age: int
                the age of the students
            
            Returns:
                None
            """
            self.name = name
            self.age = age

        def learn(self):
            """Simulate a student's learning.

            Prints status

            Attributes
            ----------
            name: str
                the name of the students
            age: int
                the age of the students
            
            Returns:
                None
            """
            print(f"{self.name} is now learning.")

        def take_exam(self):
            """Simulate taking over good results.
            
            Prints encouragement 

            Attributes
            ----------
            name: str
                the name of the students
            age: int
                the age of the students
            
            Returns:
                None
            """
            print(f"{self.name} did great!")

    print(f"Student1 is {student1.name} and is {student1.age}")
    print(f"Student2 is {student2.name} and is {student2.age}")

    student1 = Student("John Wick", 47)
    student2 = Student("Macaulay Culkin", 12)

A method is a function that is part of a class.
Everything you learned about functions also applies to methods; the only difference in practice is that we'll refer to methods as methods.

========================
7. Documenting your code
========================

-----------------------------------------
Why Documenting Your Code Is So Important
-----------------------------------------

.. tip::

    “Code is more often read than written.”

    — Guido van Rossum


Every piece of code you write code has three primary audiences:

    1. your users
    2. your developers 
    3. you

**Everyone is equally important!**

.. warning::

    "Well, Miss Barrett, when that passage was written only God and Robert Browning understood it. Now, only God understands it."

    — Robert Browning

.. attention::

    “It doesn’t matter how good your software is, because if the documentation is not good enough, people will not use it.“

    — Daniele Procida

-----------------------------------
Commenting vs Documenting your code
-----------------------------------

`Comments` - to explain a decision in code

`Documentation` - information about how to install, use, update, debug.

~~~~~~~~~~
Docstrings
~~~~~~~~~~

The use of Python documentation strings, sometimes known as "docstrings," makes it simple to link documentation to specific Python modules, functions, classes, and methods.

It is stated in the source code that it is used to document a particular section of code, much like a comment.
The docstring should explain what the function does, not how it accomplishes it, unlike traditional source code comments. 

More about Docstring Conventions at https://peps.python.org/pep-0257/.

~~~~~~~~~~~~~~~~~
Google Docstrings
~~~~~~~~~~~~~~~~~

More about https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings

.. code-block:: python

    def hello_name(username='skillab', email='admin@skillab.com'):
        """Display a simple greeting with 2 parameters.
        
        Args:
            username (str): The username of your user (default is skillab)
            email (str): The email of your user (default is admin@skillab.com)

        Returns:
            string: a string with information about the user and mail
        """
        return f"Hello World {username.upper()} with {email.upper()}!"

~~~~~~~~~~~~~~~~~~~~~~~~~~~
reStructuredText Docstrings
~~~~~~~~~~~~~~~~~~~~~~~~~~~

More about http://docutils.sourceforge.net/rst.html

.. code-block:: python

    def hello_name(username='skillab', email='admin@skillab.com'):
        """Display a simple greeting with 2 parameters.
        
        :param username: The username of your user (default is skillab)
        :type username: str
        :param email: The email of your user (default is admin@skillab.com)
        :type email: str
        :returns: a string with information about user and mail
        :rtype: string
        """
        return f"Hello World {username.upper()} with {email.upper()}!"

========================
8. Python Language Rules
========================

-------
Linting
-------

Lint, often known as a `linter`, is a tool that analyzes source code in order to detect programming errors, bugs, stylistic errors, and suspicious structures.

A `linter`, in its simplest form, is a program that examines your code in order to identify problems that could result in errors or inconsistencies with code health and style. Some even assist you in fixing them!

.. code-block:: bash
    
    pylint *py

-------------------
Static type checker
-------------------

``Mypy`` is a Python static type checker that is optional and attempts to combine the advantages of static and dynamic (or "duck") typing.
``Mypy`` combines a robust type system and compile-time type verification with Python's expressive power and simplicity.
``Mypy`` type verifies common Python programs, which can be executed on any Python virtual machine with almost no runtime overhead.

.. code-block:: bash
    
    mypy *py

-------------
Autoformatter
-------------

Black is the uncompromising Python code formatter. By using it, you agree to cede control over the minutiae of hand-formatting. In return, Black gives you speed, determinism, and freedom from pycodestyle nagging about formatting. You will save time and mental energy for more important matters.

Blackened code looks the same regardless of the project you're reading. Formatting becomes transparent after a while and you can focus on the content instead.

.. code-block:: bash
    
    black *py