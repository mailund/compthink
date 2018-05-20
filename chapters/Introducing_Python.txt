
# Introducing Python programming

Many textbooks on algorithms will present the algorithms in so-called *pseudo code*, something that looks like it is written in a real programming language while it is in fact written in an approximation to such a language but with the abstractions and programming constructs chosen to make the algorithm look as simple as necessary. Since the goal of this is to present the essentials of an algorithm and not distract the reader with unnecessary language artifacts, this is a sensible approach. It does, however, occasionally hide too many details from the reader, and since the pseudo code cannot actually be run by a computer, it is not possible to experiment with it to test different approaches to how an algorithm could be implemented in practice. In this book, we will not use pseudo code but present all algorithms in the Python programming language. Python is a very high-level language, and in many ways Python implementations of common algorithms look very similar to pseudo code versions of them, but with Python you get a working implementation.

Python is a complete general purpose programming language with many advanced features and it scales well to constructing very large software systems. At the same time, it has a very gentle learning curve and lets you implement small programs with very little programming overhead. It is perfect for our purpose in this book. By knowing just a small subset of the language you will be able to implement the algorithms we cover in the book and you will be able to experiment with them, and should you decide to make more of a career out of programming, then you can easily pick up the more advanced features of Python and use this language for larger projects as well.

Writing complete programs, especially larger applications, require different skills than the computational thinking this book is about. It takes a different skill set to be able to engineer software so it is scalable and maintainable than the skills that are needed to build efficient algorithms. Those software engineering skills are beyond the topic of this book, but if you find it interesting there are many excellent textbooks on the marked.

Even simpler programming tasks such as reading data from input files and formatting data for output files will be considered outside the scope of this book. If you ever need to write a program that can be used from a command line terminal, you will need to write code for input and output, but any introduction to Python programming textbook will teach you how to do this, and in many cases there will be existing software modules to assist you in this. This book, however, is not an introduction to Python programming book. We simply use Python to describe and experiment with algorithms we explore.

## Obtaining Python and Jupyter

When you write programs in Python, you will usually do this in one or more plain text files using a simple text editor. We will take a slightly different approach and use so-called *Jupyter notebooks*. Jupyter, [http://jupyter.org](http://jupyter.org), is a web interface to a text and code editor. Jupyter is not the ideal choice for large software projects---there you are better off with plain text Python files and perhaps an integrated development environment---but the Jupyter interface is frequently used when people do data analysis using Python. In the Jupyter interface, you can combine text, math, images, and tables with code that analyze your data and display the results of the analysis.

Jupyter isn't part of a standard Python installation---at least not yet---but the easiest way to install this interface is through a Python distribution that installs it and all the software it depends on. One such distribution is *Anaconda*. To download and install Anaconda, go to [https://www.anaconda.com/download](https://www.anaconda.com/download). There, you can download installation packages for Windows, OSX, and Linux. Download the distribution for your platform. The dialect of Python we will use in this book is Python 3.x (version numbers that start with 3). The differences between Python 2.x and 3.x for the purpose of the algorithms we will explore here are very minor, but you should download the installer for a Python 3.x version to get the version of Python we use here. Once you have downloaded the installer, double-click on it and follow the instructions guiding you through the installation for your platform.

The Anaconda installer will install Python, Jupyter, and various Python modules and frameworks for scientific computing, data analysis and visualization. We only use a tiny fraction of the software that is installed via Anaconda, but everything we do use will be available to you once you have installed Anaconda. If you continue programming in Python after you have read this book, chances are that you will find good use for many of the other modules installed by Anaconda.

## Starting Jupyter and creating a notebook

Once you have installed Jupyter, you can start the web-server you will interact with when working in Jupyter notebooks. In a terminal, write:

```sh
jupyter notebook
```

and hit Enter. The result will be similar to that seen in [@fig:running-jupyter].

![Running Jupyter.](figures/running-jupyter){#fig:running-jupyter}

Starting up Jupyter should also open your web-browser with a window showing the directory in which you started Jupyter. I started the server in an empty directory, and my browser opened up looking like in [@fig:empty-jupyter].

![Jupyter opened in an empty directory.](figures/empty-jupyter){#fig:empty-jupyter}

If you click the *New* button in the upper right corner, you can create a new file in this directory. You have several choices here, but we will always go with a Python 3 Notebook, see [@fig:new-jupyter-notebook].

![Creating a new notebook.](figures/new-jupyter-notebook){#fig:new-jupyter-notebook}

The new notebook you create this way will open up. At the top of the page, you will see that it is named "Untitled", see [@fig:untitled-jupyter-notebook]. You can click on the title and rename the notebook, see [@fig:renaming-jupyter-notebook].

![Untitled new notebook.](figures/untitled-jupyter-notebook){#fig:untitled-jupyter-notebook}

![Renaming the new notebook.](figures/renaming-jupyter-notebook){#fig:renaming-jupyter-notebook}

Below the menu and tool bar in the notebook you have the notebook proper. A notebook consists of one or more "cells". In the new notebook we just created there is a single cell. That is the box with "In [ ]: " in front of a field where you can type. Cells come in different types; you can go to the "Cell" menu and then select "Cell Type" to see the options. In the exercises associated with this book we will only use two types: Markdown and Code. Markdown cells are text cells; we use these to write prose. Markdown is a language for marking up text (the name is a pun on "mark up"), so we can make text italic or bold and we can format text into lists and such. The code cells contain Python code. Markdown cells are just text until you double click on them; when you do, you can edit the text. Code cells have "In [ ]: " in front of them and you can edit code in the gray area inside them. The "In [ ]: " is a prompt and a leftover from the IPython program that Jupyter is a descendant of.

Tradition has it, that the first program you write in any new Programming language is one that prints "hello, world!". Type the following into the code cell in your notebook:

```python
print("hello, world!")
```

You can then evaluate it. You can do this by hitting the "play" button in the tool bar, by selecting "Run Cells" in the "Cell" menu, or by pressing Shift-Enter. When you evaluate the cell, the result of the evaluation will be shown below the input part of the cell and a new cell will be created below, see [@fig:hello-world-jupyter-notebook].

!["Hello, world" in a notebook.](figures/hello-world-jupyter-notebook){#fig:hello-world-jupyter-notebook}

When you evaluate the cell, you will notice that "In [ ]: " changes to "In [1]: ". The number here, one, indicates that it is the first cell you evaluated. The cells in a notebook are evaluated when you explicitly choose to evaluate them, and each time a cell is evaluated the number is increased. You can see, from the numbers to the left of the code input, the order in which cells have been evaluated.

This isn't really ideal. You would expect code to be evaluated in the order you read it, so from top and down. This isn't how Jupyter does it, though; you have to explicitly evaluate cells you want evaluated (which is probably a good thing since you don't have to evaluate cells that are not modified and might take a while to run) and you can do this in any order you want (which is probably a bit risky since it doesn't take into account possible dependencies between the cells).

If the dependencies and order in which you evaluate cells start to confuse you, you can restart the notebook and reevaluate all the cells in order. Just go to the "Kernel" menu and select "Restart & Run All".

When you evaluate a cell, any output you print will be shown below the input code. In addition, unless the last expression in a cell evaluate to `None`, a special value in Python that indicate nothingness, the result of the final expression will also be printed. In the "hello, world!", example above, the last (and only) expression was the `print` command, and this command returns `None`, so no value was printed. The "hello, world!" that was printed in the cell was the side effect of printing; it wasn't the *result* of the print expression. To see the difference, try putting just the string `"hello, world!"` in the next cell and evaluate it (see [@fig:hello-world-jupyter-notebook-2]).

!["Hello, world", printing and evaluating.](figures/hello-world-jupyter-notebook-2){#fig:hello-world-jupyter-notebook-2}

The result appear similar to the print cell, but you have "Out[2]: " to the left of the `"hello, world!"` output, and that output is in quotes. The "Out[2]: " tells us that this is the result we get from evaluating the cell (the number is the same as the "In[2]: " number the cell got when we evaluated it). The string `"hello, world!"` is an expression that evaluates to the string itself, and because this string is not `None`, Jupyter displays it.

We will not make much of a distinction between printing values or displaying them by default when they are the result of the last expression in a cell we evaluate, but when you are working with code in a notebook, you might find it helpful to simply evaluate expressions in cells and see what Python thinks the look like.

## Simple calculations in Python

The simplest way you can use Python is as a calculator. You can write arithmetic expressions in a code cell and evaluate it to get the result.


```python
2 + 2
```




    4




```python
3 * 5
```




    15

## Working with strings

## Printing and formatting output


```python

```

## Statements and variables

## Conditional statements

## Loops