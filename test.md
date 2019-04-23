Introduction
============

Using computers as more than glorified typewriters or calculators is an
increasingly important aspect of any scientific or technological field,
and knowing how to program a computer to solve new problems has become
as essential a skill as mathematics. Learning how to program can be a
frustrating experience at times since computers require a level of
precision and rigour in how we express our ideas, that we rarely
encounter elsewhere in life. While occasionally infuriating, programming
can also be very rewarding. Programs are created out of pure thought,
and it is a special feeling when you make a computer transform your
ideas into actions and see it solve your problems for you.

Solving any kind of problem, on a computer or otherwise, requires a
certain level of precision. To address the right question, we must first
understand what the problem *is*. We also need to have a precise idea
about what an adequate *solution* to the problem would be---or at the
very least some way of distinguishing between two solutions to judge if
one is better than another. These are concerns we will need to address
in any problem-solving task, but where everyday life might forgive some
fuzzy thinking in problem-solving, computers are far less forgiving. To
solve a problem on a computer, you must first specify with mathematical
clarity what the problem is and what a solution is, and after that, how
you will go about deriving a solution. And only then, can you write a
program and put the computer to work.

For the novice programmer, the last step---implementing a solution in a
computer language---is often the most frustrating. Computer programs do
not allow any ambiguities, and that means that if you do not abide by
the computer language's rules---if you get the grammar wrong in the
slightest---the computer will refuse even to consider your program.
Learning how to write programs the computer will even attempt to run is
the first hurdle to overcome.

Many good books can teach you different programming languages, and it is
worth your while getting a few of these about the programming languages
you plan to use in your future work. This book is not so much about
programming, however, but about how computation is done and how you can
make computation efficient.

We will do some programming in the book, and we will use the Python
programming language. The Python language is generally considered an
excellent first language to learn because of its high-level yet
intuitive features, and at the same time, Python is one of the most
popular programming languages for scientific programs. It is one of the
most frequently used languages for data science. It is number one on the
Kaggle machine learning platform (https://www.kaggle.com ). It has
powerful libraries for machine learning, data analysis, and scientific
computing through various software modules. It is also one of the most
popular languages for scripting workflows of data analysis and for
administrating computer systems. We will only use a little bit of the
language, however, so this book is not sufficient if you want to become
an effective Python programmer. We use the language to illustrate ideas,
and for exercising topics we cover, but the focus of the book is not on
programming. The focus is how to think about problem-solving in a
disciplined way; to consider problems as computational tasks and how to
plan solutions in ways that are computationally efficient. This is what
we mean by *computational thinking*.

Models of the world and formalising problems
--------------------------------------------

Our goal is to learn how to *formalise objectives* in such a way that we
can specify *mathematically and objectively* what solutions to our goals
are. This also means formalising what data we have and how we should
interpret it. Formalising a problem might reveal that we do not have
sufficient data for the issue at hand. It might also show that we do not
truly understand our problem. If we cannot clearly define what we want,
we won't be able to formalise how to get it. We might, with some luck,
be able to fudge it a bit and get *something*, and then use subjective
opinion to judge if what we get is what we wanted. This is far from
optimal, though. If you and I disagree on whether one solution is better
than another or not, we have no way of resolving the issue.

Formalising problems and formalising what data we have to work with is
what you do in all natural sciences. You might not have thought about it
this way before---depending on which science you have a background
in---but when we derive theories (or laws) about the natural world, we
are making formal statements about how the world works. For some
theories there are exceptions---the world is breaking a natural
law---which tells us we do not have a comprehensive theory. But any
theory worth its salt can be falsified, which is another way of saying
that we can judge if a data point matches the formalisation of the
theory or not.

In the hard sciences, like physics and chemistry, these theories are
described in the language of mathematics; often in somewhat complex
equations. In sciences describing very complex systems, such as biology
that tries to explain life in general, we often have much simpler
mathematics, and the rules almost always have exceptions. Biology is
more complicated than particle physics, so it is harder to formalise,
and thus we stick with simpler equations. There is no point in using
very complex mathematics to describe something we do not
understand---simple mathematics suffices for that. Any quantitative
evaluation of the natural world requires some mathematics and some
formalisation of scientific theories. Even if the mathematics is as
simple counting to see if some quantity is more abundant in some
situations than others. All quantitative data analysis involves
formalising our thoughts about reality and reducing data to the relevant
aspects for those formal descriptions.

Abstracting the complex natural world to something more manageable is
called *modelling*. We build models of the real world---usually
mathematical models. We aim at making the models simple enough to
understand, yet sophisticated enough to describe the aspects of the
world we are interested in. In principle, we could model molecular
evolution as a physical system at the level of particles. We don't,
because this would be much too complex for us to work with, and probably
wouldn't help us answer most of the questions about evolution we are
interested in. Instead, we model molecular evolution as random mutations
in strings of DNA, abstracting the three-dimensional DNA molecules into
one-dimensional strings over the four letters A, C, G, and T. We
abstract away aspects of the world that are not relevant for the models,
and we abstract away features about the data that is not modelled.

Building models of the natural world are the goals of all the sciences
and much too broad a topic for this book. The models are relevant for
computational thinking, however. When we formalise how to solve
problems, we do so within a model of the world. This model will affect
how we can formalise problems and which level of detail we consider our
data. Sometimes, changing the model of reality can change what can be
efficiently computed---or make an easy problem intractable. Of course,
we should not pick scientific theories based on what we can efficiently
calculate, but sometimes, abstracting away aspects of the world that are
not essential for the problem at hand, will not qualitatively change
solutions but might make an otherwise impossible problem easy.

This book is not about modelling the world. We will generally assume
that we have some formal models to work within whatever scientific field
we find ourselves. You are rarely in the situation where you can pick
your theories at random to satisfy your computational needs, but keep in
mind that formalising the *problem* you want to solve might give you
some wiggle room within those formal scientific theories. When, for
example, we study genome evolution or population genetics we abstract
complex DNA molecules to the level of strings or reduce populations to
gene frequencies. These abstractions are there to simplify the subject
matter to something that can be attacked computationally.

What is computational thinking?
-------------------------------

Computational thinking is what you do when you take a problem and
formalise it. When you distil it into something where you can
objectively determine if something is a solution to it or not. For
example, given a sequence of numbers, are all positive? Easy to check,
and either all the numbers are positive, or they are not. Or, perhaps
the problem is not a yes-no question but an optimisation issue. Find the
shortest route to get from point A to B is an optimisation problem. It
might be easy for us to determine if one path is shorter than another,
which would be a yes-no problem, but actually coming up with short
routes might be a harder problem. It is still a computational problem,
as long as we can formalise what a path is and how we measure distance.

Computational thinking is also what happens after you have formalised
the problem. When you figure out how to solve it. A formal description
for how to solve a problem is called an *algorithm* after the 9th
Century mathematician Muhammad ibn Musa al'Khwarizmi who is also
responsible for the term algebra. To qualify as an algorithm, a
description of how to solve a problem must be in sufficient detail that
we can follow it without having to involve any guesswork. If you
implement it on a computer, I guarantee you that you do not want to
leave any room for guessing. The description must always get to a
solution in a finite number of steps---we don't want to keep computing
forever, and the description must always lead to a valid solution---we
don't want to follow all the steps and end up with something we cannot
use anyway.[^1]

Designing algorithms are part science and part art. There are general
guidelines we can use to approach a computational problem to develop
algorithms and general approaches to organising data such that we can
manipulate it efficiently, but you will almost always have to adapt the
general ideas to your specific problem. Here, sparks of insight cannot
be underestimated---sometimes, just looking at a problem in different
ways will open entirely new ways of approaching it. The general
approaches can be taught and learned and are the main topic of this
book. The art of designing algorithms come with practice, and as with
all skills, the more you practice, the better you get.

Most of the algorithms we will see in this book are used in almost all
software that runs on your computer (with the exceptions of some toy
examples found in the exercises that are never used in the wild).
Sorting and searching in data and arranging data for fast retrieval or
fast update is part of almost all computations. The models behind such
algorithms are often exceedingly abstract; much more so than any model,
we would use to describe real-world phenomena. A sorting algorithm might
work in a world where the only thing you can do with objects is to
determine which of two objects is smaller than the other. Or maybe the
algorithm works in a model that allows more structure to data and this
structure can be exploited to make the algorithm more efficient. In any
case, what we can do with data depends on our models, and for
computation, these models are often remarkably abstract. Such abstract
models can feel far from the world your problem originates in, but it is
because the models are so very theoretical that we can apply the
algorithmic solutions to so many varied problems.

Some people spend their entire lives developing new algorithms for
general problems. Those people would be professional computer science
academics. Most people that solve problems on computers are not doing
this, even if they develop algorithms on a daily basis. When we deal
with concrete issues, we can usually do so by combining existing
algorithms in the right ways. Having a toolbox of algorithms to pick
from, and knowing their strengths and weaknesses is more important in
day to day computational work than being able to design algorithms
entirely from scratch. Although that can be important as well, of
course, on the rare occasions when your toolbox does not suffice.

Whether you can get where you want to go by combining existing
algorithms or you have to design new ones, the general approach is the
same. You have to break apart big tasks, that you do not know how to
solve (yet), into smaller tasks that, when all done, will have completed
the larger tasks. Steps to a job, such as "find the largest number in a
sequence" can be broken into smaller steps such as "compare the first
two numbers and remember the largest", "compare the largest of the first
two to the third and remember the largest", and so on. You start out
with one big task---the problem you want to solve---and you keep
breaking down the problem until smaller tasks until they all are tasks
you know how to handle---either because they are trivial or because you
have an algorithm in your toolbox that can solve them. The practice of
breaking down tasks until you can resolve them all is at the heart of
computational thinking.

Developing and combining algorithms is a vital part of computational
thinking, but algorithms alone do not solve any problems. Algorithms
need to be executed to solve concrete problems; we need to follow the
instructions they provide on actual data to get actual solutions. Since
we rarely want to do this by hand or with pen and paper, we wish to
instruct computers how to run algorithms, which means that we have to
translate a high-level description of an algorithm to a lower level
description that can be put into a computer program that the machine
will then slavishly execute. This task is called *implementing* the
algorithm.

Designing an algorithm and implementing it as a computer program are two
separate tasks, although tightly linked. The first task involves
understanding the problem you want to solve in sufficient detail that
you can break it down into pieces that you know how to address. The
second task consists in breaking those pieces into even smaller ones
that the computer can solve; this is where the algorithm design task
meets the programming task.

The abstraction level at which you can implement an algorithm depends
intimately on the programming language and the libraries of
functionality you have access to. At the most basic level---the hardware
of your computer---the instructions available do little more than move
bits around and do basic arithmetic.[^2] A modern CPU is a very
sophisticated machine for doing this, with many optimisations
implemented in hardware, but the basic operations you have at this level
are still pretty primitive. This is the level of abstraction where you
can get the highest performance out of your CPU, but we practically
never program at this level, because it is also the level of abstraction
where you get the lowest performance out of a programmer. Basic
arithmetic is just too low a level of abstraction for us to think about
algorithms constructively.

Programming languages provide higher levels of abstraction to the
programmer. They can do this because someone has written a program that
can translate the high-level operations in the programming language into
the right sequence of lower-level operations that the computer can
actually execute.[^3] Which abstractions are available varies
tremendously between programming languages, but they all need to
describe programs that are eventually run at the low level of the
computer's CPU. The programming language abstractions are just an
interface between the programmer and the machine, and the language's
implementors have handled how these abstractions are executed at the
lower layers of the computer.

We sometimes talk about high-level and low-level programming languages,
but there isn't a real dichotomy. There are merely differences in the
higher level abstractions provided by all programming languages. Some
programming languages provide an environment for programming very close
to the hardware, where you can manipulate bits at the lowest level while
still having some abstractions to control the steps taken by your
program and some abstractions for representing data beyond merely bit
patterns. These, we would call low-level languages because they aim to
be close to the lowest level of abstraction on the computer. Other
languages, high-level languages, provide a programming environment that
tries to hide the lower levels to protect the programmer from them. How
data is actually represented at lower levels is hidden by abstractions
in the language, and the programming environment guarantees that the
mapping between language concepts and bits is handled correctly.

Computational thinking in a broader context
-------------------------------------------

To summarise, what we call computational thinking in this book refers to
a broad range of activities vital for solving problems using a computer.
For some of those activities, computational thinking is merely a tiny
aspect. Making models of the real world in order to understand it is the
entire goal of science; considering scientific theories in the light of
how we can make computations using the equations that come out of the
theories is a minute aspect of the scientific process, but an essential
one if you want to use your computer to do science. Creating new
algorithms to solve a particular problem is also almost entirely
computational thinking in action; implementing these algorithms, on the
other hand, can be an almost mechanical process once you have fleshed
out the algorithm in sufficient detail,

One thing that sometimes complicates learning how to think about
computations is that there is rarely a single right answer to any
problem you consider. It shares this with natural sciences. While we
usually believe that there is a unique natural world out there to
explore, we generally do not attempt to model it in full detail; an
accurate model of reality would be too complicated to be useful.
Instead, we build models that simplify reality, and there is no "right"
model to be found---only more or less valuable models. When we seek to
solve a problem on a computer, we are in the same situation. We need to
abstract a model of reality that is useful, and there may be many
different choices we can reasonably make in doing this, all with
different pros and cons.

For any of these models, we have a seemingly endless list of appropriate
algorithms we can choose from to solve our problem. Some will be
horrible choices for various reasons. They might not solve the problem
at hand in all cases, or at all, or they might solve the problem but
take so long to do this, that in practical terms they never finish
computing. Many of the choices, however, will solve the problem and in a
reasonable time, but use different computational resources in doing so.
Some run faster than others; some can exploit many CPUs in parallel,
solving the problem faster but using more resources to do so; some might
be fast but require much more memory to solve the problem, and therefore
might not be feasible solutions given the resources you have. It
requires computational thinking to derive these algorithms, but it is
also computational thinking to reason about the resources they need and
to judge which algorithms can be used in practice and which cannot.

Once you have chosen an appropriate algorithm to solve your problem, you
need to implement it to execute it. On itself, the algorithm is useless;
only when it is executed does it have any value, and executing it on a
computer means you have to implement it as a computer program first. At
this step, you need to decide on a computer programming language and
then how to flesh out the details the algorithm does not specify. For
choosing the programming language, you once again have numerous choices,
all with different strengths and weaknesses. Typically, the first choice
is between the speed and speed---how fast can you implement the
algorithm in a given language versus how fast it will run once you have
implemented it. Typically, high-level languages let you implement your
ideas more swiftly, but often at the cost of slightly (or less slightly)
slower programs. Low-level languages let you control your computer in
greater detail, which allows you to implement faster programs, but at
the cost of also having to specify details that high-level languages
will shield you from. You shouldn't always go for making your programs
as fast as possible; instead, you should go for solving your actual
problem as speedy as possible. You can make your program very fast to
run by spending a vast amount of time implementing it, or you can
implement it quickly and let it run a little longer. You want to take
the path that gets you to your solution the fastest. Here, of course,
you should also take into account how often you expect to use your
program. A program that is run often gains more from being faster than
one that runs only for a specific project and only a few times there.

In reality, the choice of programming language is not between all
possible languages, but between the languages, you know how to write
programs in. Learning a new programming language to implement an
algorithm is rarely, if ever, worth the time. If you only know one
language, the choice is made for you, but it is worthwhile to know a
few, at least, and to know both a high-level and a low-level language
with sufficient fluency that you can implement algorithms in them with
comfortable fluency. This gives you some choice in what to choose when
you have a program to write.

The choices aren't all made once you have decided on the programming
language, though. There will always be details that are not addressed by
your algorithm, but that must be addressed by your program. The
algorithm might use different abstract data structures, such as "sets"
or "queues" or "tables", and it might also specify how fast operations
on these has to be, but when you have to make concrete implementations
of these structures or choose existing implementations from software
libraries, there are more options to consider. In high-level programming
languages, there are fewer details you have to flesh out than in
low-level languages, which is one of the reasons it is usually much
faster to implement an algorithm in a high-level language than in a
low-level language---but there will always be some choices to be made at
this point in the process as well.

You might hope you are done when you have implemented your algorithm,
but this is usually not the case. You need to feed data into the program
and get the answer out, and here you have choices to make about data
formats. Your program will not live in isolation from other programs,
either, but communicate with the world, usually in the form of files and
data formatted in different file formats. Again, there are choices to be
made for how you wrap your algorithm in a program. If your algorithm is
useful for more than a single project you might also put it in a
software library, and then there are choices to be made about how you
provide an interface to it. If you build a whole library of different
algorithms and data structures, constructing interfaces to the library
is full of critical design decisions, and these decisions affect how
other programs can use the algorithms, and how efficiently, so this is
also aspects of computation thinking---but here only a part of the
broader topic of software engineering.

What is to come
---------------

The purpose of this book is to introduce computational thinking as basic
problem-solving approaches for designing algorithms and implementing
them in a computer language, the Python language. We will focus on the
design of algorithms more than the implementation of them, and only use
a subset of the Python programming language for exercises. This will
make it easier to transfer what you learn to other programming
languages, but keep in mind that it also means that the solutions we
consider are not the solutions an experienced Python programmer would
come up with. There are ways of expressing things in Python that can
implement our algorithms more effectively, but those are Python specific
and might not be found in other languages.

In many of the following chapters, I will explain how computation is
done on an actual computer; not just in Python but on computers in
general. General computers do not understand Python programs but do
understand more primitive instructions that you can give a CPU, and I
will try to put our Python programs in a context of these. I will also
explain how computers store data, which they can only do using simple
memory words consisting of ones and zeros. These explanations are far
from comprehensive and are only intended to give you a feeling for how
instructions in a high-level programming language such as Python will
have to be translated into much lower-level concepts on actual hardware.
When I do explain these concepts, I will not always be completely honest
about how Python *actually* handles these issues. Since Python is a very
high-level programming language, it supports features that are not found
in lower-level languages, and this means that to run a Python program
you need a more complex model of both data and code than you will need
in many other languages. I will explain general concepts, but I will
give a simplified explanation of them. If you want to know the details
of how your computer really deals with these concepts, and how Python
handles these and more complex features of the language, you will need
to find this information elsewhere.

We use an actual programming language to explain the algorithms in the
book to make it easier for you to experiment with them. Many algorithmic
textbooks will not, preferring to describe algorithms in pseudo-code
where the abstractions can be fitted to the problem. This might make the
description of algorithms slightly more accessible, but can also easily
hide away the issues that you will have to resolve actually to implement
them. We prefer to use an actual language. It is a very high-level
language, so some details that you will have to deal with in lower level
languages are still hidden from you, but what you can implement in
Python, you can actually run on your computer. And it is vital that you
do take the code in this book and experiment with it.

To get the full benefit out of this book, or any book like it, you must
practice. And practice a lot. Programming can look deceptively easy---at
least for the complexity level we consider in this book---but it is
substantially harder to write your own code than it is to read and
understand code already written.[^4] Without exercising the skills
involved in computational thinking and algorithmic programming, at best
you will get a superficial understanding. Watching the Olympics doesn't
prepare you for athletics. Each chapter has an exercise set associated
with it, and you should expect to use at least as much time doing
exercises as you spend reading the chapters if you want the full benefit
out of the book.

Introducing Python programming
==============================

Many textbooks on algorithms will present the algorithms in so-called
*pseudo code*, something that looks like it is written in a real
programming language while it is in fact written in an approximation to
such a language but with the abstractions and programming constructs
chosen to make the algorithm look as simple as necessary. Since the goal
of this is to present the essentials of an algorithm and not distract
the reader with unnecessary language artefacts, this is a sensible
approach. It does, however, occasionally hide too many details from the
reader, and since the pseudo code cannot actually be run by a computer,
it is not possible to experiment with it to test different approaches to
how an algorithm could be implemented in practice. In this book, we will
not use pseudo code but present all algorithms in the Python programming
language. Python is a very high-level language, and in many ways Python
implementations of common algorithms look very similar to pseudo code
versions of them, but with Python you get a working implementation.

Python is a complete general purpose programming language with many
advanced features and it scales well to constructing very large software
systems. At the same time, it has a very gentle learning curve and lets
you implement small programs with very little programming overhead. It
is perfect for our purpose in this book. By knowing just a small subset
of the language you will be able to implement the algorithms we cover in
the book and you will be able to experiment with them, and should you
decide to make more of a career out of programming, then you can easily
pick up the more advanced features of Python and use this language for
larger projects as well.

Writing complete programs, especially larger applications, require
different skills than the computational thinking this book is about. It
takes a different skill set to be able to engineer software so it is
scalable and maintainable than the skills that are needed to build
efficient algorithms. Those software engineering skills are beyond the
topic of this book, but if you find it interesting there are many
excellent textbooks on the marked.

Even simpler programming tasks such as reading data from input files and
formatting data for output files will be considered outside the scope of
this book. If you ever need to write a program that can be used from a
command line terminal, you will need to write code for input and output,
but any introduction to Python programming textbook will teach you how
to do this, and in many cases there will be existing software modules to
assist you in this. This book, however, is not an introduction to Python
programming book. We simply use Python to describe and experiment with
algorithms we explore.

Obtaining Python
----------------

When you write programs in Python, you will usually do this in one or
more plain-text files using a text editor.

**FIXME**

One such distribution is *Anaconda*. To download and install Anaconda,
go to https://www.anaconda.com/download. There, you can download
installation packages for Windows, OSX, and Linux. Download the
distribution for your platform. The dialect of Python we will use in
this book is Python 3.x (version numbers that start with 3). The
differences between Python 2.x and 3.x, for the purpose of the
algorithms we will explore here are very minor, and all the algorithms
in this book work equally well in either version. There are differences
in the built in functions, though, so you should download the installer
for a Python 3.x to get exactly the behaviour as described here.

Once you have downloaded the installer, double-click on it and follow
the instructions guiding you through the installation for your platform.

The Anaconda installer will install Python and various Python modules
and frameworks for scientific computing, data analysis and
visualisation. We only use a tiny fraction of the software that is
installed via Anaconda, but everything we do use will be available to
you once you have installed Anaconda. If you continue programming in
Python after you have read this book, chances are that you will find
good use for many of the other modules installed by Anaconda.

Running Python
--------------

**FIXME**

The simplest way you can use Python is as a calculator.

    `python

2 + 2

    `

4

    `python

3 \* 5

    `

15

Programming in Python
---------------------

**FIXME: Editor**

### Expressions in Python

We have already seen how we can evaluate simple arithmetic expressions
in Python. The arithmetic binary operators `+`, `-`, `*` and `/`, works
as you would expect them to, as does the unary `-`. That is,

``` {.python}
-4
```

is minus four,

``` {.python}
2 * 2 + 3
```

is seven. Notice that we interpret `2 * 2 + 3` as you are familiar with
in mathematical notation. First we multiply two by two and then you add
three. This is not because we evaluate the expression left-to-right, in
which case

``` {.python}
3 + 2*2
```

would mean $(3 + 2) * 2$ and would be 10. It is because multiplication
"binds tighter" or "has larger precedence" than addition. This is also
what you are familiar with. In mathematical notation, you would expect
$3 + 2cdot 2$ to be seven and not ten. Multiplication and division binds
tighter than addition and subtraction.

When precedence is taken into account, the evaluation does proceed from
left to right. For example,

``` {.python}
1 / 2 / 2
```

is interpret as $(1/2)/2=1/4$ and not $1/(2/2)=1$. To get the latter
interpretation you will need to add parentheses:

``` {.python}
1 / (2 / 2)
```

You can always use parentheses to change the default evaluation order.
Or just to make explicit what you intend, even if it is already the
default. Writing `(2 * 2) + 3`, while it is the default for `2 * 2 + 3`,
doesn't make the expression any harder to read, after all.

There are more operations that addition, subtraction, multiplication,
and divisions. For example, raising a number to a power. If you want to
compute two to the power of four, $2^4=16$, you can use the `**`
operator: `2**4`. This operator has higher precedence than
multiplication and division, so `2 * 2**4` is $2\cdot 2^4=32$ and not
$(2\cdot 2)^4=256$. This operator is not evaluated left-to-right but
right-to-left, also in accordance with typical mathematical notation.
This means that `2**3**4` is interpreted as
$2^{3^4}\approx 2.4\times 10^{24}$ and not $(2^3)^4=4086$. If you want
to compute the latter, you must write `(2**3)**4`. The notation is the
same as it would be in mathematics, but if you find it hard to remember,
you can always use parentheses even when not strictly necessary to avoid
any surprises.

Python actually has two different division operators. When you use `/`
you get the division you are used to in mathematics. However, it is
often useful to guarantee that if you divide two numbers you get the
integer result of the division. Remember that for division, $n/m$, you
get an integer if $m$ divides $n$. You can write $n=a\cdot m + b$ where
$a$ is the integer number of times that $m$ divides $n$ and $b<m$ is the
remainder. To get the integer part of the division, $a$ in this example,
you will use the `//` operator. So while `5 / 2` will give you 2.5,
`5 // 2` will give you 2. To get the remainder, you use the modulus
operator, `%`. Since $5=2\cdot 2 + 1$, we would expect `5 % 2` to be
one, and indeed it is. If you evaluate

``` {.python}
(5 // 2) * 2 + (5 % 2)
```

the $a\cdot m + b$ form of this division, you get five, as expected.
Another way to put this is that `5 // 2` is five divided by two, rounded
down, or $\lfloor 5/2 \rfloor$.

**Exercises:** Evaluate the following expressions in Python. Check that
they give you the expected result. If not, check if you can change that
by inserting parentheses.

1.  $2\cdot 4 + 2$
2.  $2^4 - 4^2$
3.  $2\cdot(1+2+3)$
4.  $5/2$
5.  $\lfloor 5/2\rfloor$
6.  $\frac{2}{1+2+3}$
7.  $(1 + 2 + 3)^{1 + 2 + 3}$
8.  $\frac{1+2+3}{2}$

chapter FIXME: appendix
-----------------------

Introduction to algorithms
==========================

We briefly discussed what we mean by *algorithms* in the introduction,
but perhaps it bears repeating; algorithms are recipes for solving a
specific computational problem. They describe the steps you (or rather
your computer) must take to get from input to output and should
guarantee you that if you follow the instructions exactly, you will 1)
finish after a finite number of steps and 2) your output will be a
solution to the problem they should solve, given the input you had.

If you think I'm being pedantic with 1), consider this program:

``` {.python}
x = 0
while True:
    x += 1
```

It computes the largest possible integer---or rather, it would if it
ever finished computing. It runs forever, increasing `x` by one in each
iteration of the loop, but, of course, it will never finish.
Theoretically, at least, eventually the computer executing the program
will break down and stop running, but if the computer never breaks, it
will keep running this program forever. This is not an algorithm because
it takes an infinite number of steps to finish.

When we design an algorithm, the first goal is to make sure that we
actually develop a proper *algorithm*. That means that steps we describe
in solving a problem must be finite and actually solve the problem. We
say that an algorithm *terminates* if it finishes computing in a finite
number of steps (and it isn't a proper algorithm if it doesn't). If it
also computes the right answer, we say that it is *correct*. When we
design an algorithm, we must ensure both properties, which usually means
proving them mathematically. With experience, you can get a little lax
in formally proving this for simple algorithms, but as soon as your
algorithm gets sufficiently complicated, you will revert to formal
proofs, and as a beginner, it pays to do this for simple algorithms as
well.

We could describe this as the algorithm for checking an algorithm:

1.  Check if it terminates.
2.  If so, check if it is correct.

This, funny enough, is not an algorithm, even if I have seen it
described as such a few places. Of course, there aren't sufficient
details to see how we would execute either step, but the first step
cannot be solved by any algorithms at all. It is beyond this book to
show you why, but there are problems that cannot be solved on any
computer ever constructed, in the past or in the future, and checking if
a given algorithm, however you choose to encode it as input to the
computer, will terminate on any specific input is one such problem. It
is known as the *halting problem*, since we also use the term *halt* for
*terminates* when we consider more fundamental aspects of computation.

It is impossible to write a computer program---or generally design an
algorithm---that can check these two properties of a suggested
algorithm, but nevertheless, it is what you must do to show that your
proposed solution to a problem is actually an algorithm. We cannot put
up a formula for doing this, for very fundamental reasons, but some
general techniques might help you with proving the properties. These
techniques are useful when you already have proposed an algorithm, but
they can often also guide you in coming up with this proposal in the
first place. The first part of this chapter focuses on these techniques
and how they can guide you in designing an algorithm, prove that it
terminates, and prove that it is correct.

Once we have an actual algorithm, we know how to solve the computational
problem at hand. You can compute a solution to your problem in a finite
number of steps. That number, however, can be enormous. In practice,
there is little difference between a program that never finishes and one
that will finish in a billion years. Knowing we can solve a problem in a
finite number of steps is good, but we usually need more than that. We
want to solve the problem in a reasonable time, where "reasonable" can
depend on the problem at hand.

We have ways of reasoning about the computational complexity of both
problems and algorithms that abstract away details about the actual
software and hardware the algorithm will be implemented in and run on.
Those techniques are the topic for [Chapter
@sec:algorithmic-efficiency]. These techniques let us compare different
algorithms and decide which is best independently on how different
low-level operations will be carried out on any particular computer and
also give us some rough ideas about whether an algorithm will run in
reasonable time on any computer system you have available.

When we compare algorithms this way, we will say we compare their
*efficiency*, and we generally go for efficient algorithms over
inefficient algorithms, naturally, at least as long as we can implement
either with roughly the same effort. We use algorithmic efficiency to
determine how fast a given problem can be solved by a given algorithm.

We can also compare problems this way, and when we do, we say that we
compare the problems' *complexity*. Some problems are intrinsically
harder to solve than others. The halting problem, determining if a given
algorithm will ever terminate on given input, is *undecidable*, meaning
that no algorithm can solve it in general. That is a tough problem
indeed. Other problems are known to be solvable but, as far as we know,
any solution will take an unacceptably long time to do it. We call such
problems *intractable*, and unfortunately, many of the problems we are
interested in, in various disciplines, are in this category. Very many
optimisation problems fall into this category. I did say "as far as we
know" because for many of these problems we do not *know* if it is
impossible to derive efficient solutions, and this is one of the most
significant open questions in theoretical computer science, known as the
\*P vs. NP problem.

Figuring out how difficult different problems is a discipline of
theoretical computer science known as *complexity theory*, and the topic
is beyond this book. For this book, it is sufficient to know that it is
possible to show that some problems need a certain number of steps to be
solved. Where it is relevant, I will mention those bounds.

For designing algorithms, we do not necessarily care so much about a
problem's complexity except for two reasons: we do not want to spend
time attempting to find an efficient solution to a problem that does not
have any efficient solutions. If we have a problem that is known to be
intractable, we cannot solve it efficiently---or if we can, we have just
solved the N vs. NP problem and should bask in the glory and fame rather
than worry about the problem that led us there in the first place. If
the problem is intractable as specified, we should try to rethink the
problem instead. Figure out if a different problem would be equally
interesting to solve. Surprisingly often, rephrasing a computational
problem solves the underlying scientific problem equally well as the
original phrasing, but changes the problem from being intractable to
tractable. If we cannot do this, we can try to come up with algorithms
that approximate a solution---they might not be the optimal solutions
but can perhaps guarantee that they are within a certain fraction of
optimal.

The other case where we care about complexity is when we have a problem
that is tractable, i.e., we know a lower bound of how fast it is
possible to solve the problem, and it is not too terrible, and we want
to design an algorithm that solves the problem within that bound. When
we reason about algorithmic efficiency, we usually derive upper bounds
for how fast (or slow) they will run, while when we reason about problem
complexity, we derive lower bounds for how long all algorithms must run,
at the very least, to solve the problem. If we can make these two ends
meet, we have an optimal algorithm. We cannot make an even faster
algorithm than what we already have. Not measured the way we measure
efficiency and complexity, at least. In practice, theoretical running
times can be misleading for actual running times, and often, a
theoretically faster algorithm, but a more complex one can be slower on
typical input than a more straightforward but theoretically slower one.
At the end of the day, the efficiency of programs are measured by how
long they run on actual data, so some experimentation is needed when you
start implementing algorithms.

Before we worry about algorithmic complexity and efficiency, however, we
need to learn how to construct algorithms.

Designing algorithms
--------------------

We will explore the tricks for developing algorithms through an example.
Consider this problem: You are in city $A$ and want to know if it is
possible to get to city $B$ and to answer this question, you have a map
available. The problem is a toy example of a real problem. No matter
which pair of cities you can think of, you can get from one to the
other. There are no city or set of cities that are entirely cut off from
the rest of the world. But we could ask the question if it is possible
to *drive* from city $A$\~ to city $B$---which isn't possible for all
pairs of cities in the world---and then we would have the same problem.
Or we could ask if it is possible to get from the city $A$ to the city
$B$ in less than three hours---in which case we have a slightly harder
problem, but still a similar one. Or, we could even ask, what is the
shortest route from $A$ to $B$---if we could solve that problem we could
use it to solve all the others. Later, in [Chapter
@sec:trees-and-graphs], we will see an efficient algorithm for solving
the shortest route problem, but for now, we will only consider the first
question: is it possible to get from $A$ to $B$?

Consider the map in [@fig:simplified-map]. This is a simplification of a
real map of roads between cities. We do not care about the actual
landscape the roads pass through, only how cities are connected. So, in
this map, we abstract cities to be nodes in a network, and we connect
two cities with an edge if there is a road between them. It is a
simplification of a real map, but a simplification that might be
familiar to you from subway maps, where the actual geography is usually
not visualised, but the connection between stations is.

![Simplified map we can use to determine if we can get from $A$ to
$B$.](simplified-map.pdf){#fig:simplified-map}

We simplify the setup a little further by representing all cities as
numbers instead of naming them. The cities with names $A$ and $B$
happens to be 0 and 13. The problem of is then "is it possible to get
from the city with index 0 to the city with index 13?"

From the figure, you can probably immediately tell that city number 0
and city number 13 are connected (and by several routes), but this
partly because the map is straightforward, containing few cities and
partly because it is laid out in a way that makes it easy for your brain
to detect the connections. With thousands or millions of connected towns
and cities, it would not be so easy to see if two particular cities are
connected. It would not be trivial for you to answer the question either
if you got the information in the form that a computer would most likely
get it. Our brains are very good at handling visual input, and you can
intuitively answer the question on this small map. You probably cannot
tell *how* you solve the problem; you just know the answer. You can
train computers to "see" in some ways, but it is not the most
straightforward approach to telling them about the connectedness of
cities. Most likely, if we took that approach, they would run into the
same limitations as our brains---they could answer the question for
small and well laid out graphs but could not handle large graphs.

The input we will give the computer is a list of the direct connections:

``` {.python}
roads = [
    (0, 1), (0, 2), (0, 3),
    (1, 4), (1, 5),
    (2, 5), (2, 6),
    (3, 6), (3, 7),
    (4, 8),
    (5, 9),
    (6, 9),
    (7, 10),
    (8, 11),
    (8, 12),
    (9, 13),
    (10, 13)
]
```

The roads are represented as pairs of cities. In this example, the first
city in a pair has an index that is smaller than the second city in the
pair, but we do not mean to imply any order to the pair; if there is a
road from $i$ to $j$, there is also a road from $j$ to $i$.

From this list of pairs of cities, we want to design an algorithm that
determines if the city at index 13 can be reached from the city at index
0.

### A reductionist approach to designing algorithms

The first and perhaps the most important lesson about designing
algorithms is this: if you cannot see an immediate solution to your
problem, try to break the problem into subproblems and see if you can
solve these. This is generally a good recipe for solving any problems in
life---and, incidentally, what recipes do. It might seem like an
insurmountable task to cook a large dinner, but a dinner can be split
into different dishes, and each dish is prepared in a number of smaller
steps, and each of the smaller steps are manageable. When I write a
book, I can't attack the writing as a single task. I break the book into
chapters, then chapters into sections, and sections into paragraphs and
paragraphs into sentences.

There must be some system to the madness of breaking down a problem into
smaller steps. We should ensure that the smaller steps are easier to
solve than it is to solve the full problem, and we should ensure that if
we complete all the steps of the larger problem, we will have
successfully solved the full problem. These two requirements are, not
coincidentally, similar to the conditions we had for a recipe being an
algorithm. When we break a problem into smaller steps, such that the
smaller steps are more manageable, we are making a kind of progress, and
this progress should lead us to termination; when we know that the
steps, when all are taken, solves the original problem, we have a
correct algorithm.

In our original problem, we have the question of whether city 0 is
connected to city 13, which we cannot immediately answer. What we can
answer is whether two cities are neighbours---we merely run through the
list of roads and check if there is one between the two cities. If we
could reduce the first problem to the second, we would have a solution
to our original problem.

We won't do precisely that, but instead do something that at first
glance might look more complicated, but turns out to be easier to derive
an algorithm for. We will work on a collection of sets; the sets contain
cities we know are connected. The "collection", here, is a set, so we
have a set of sets of cities. Before we analyse the roads, we only know
that each city is connected to itself, so we start with a singleton set,
one per city containing just that city. We then iterate through all the
roads. Each road tells us about one connection between two cities. If
the cities are already known to be connected, this doesn't tell us
anything new, but if the two cities are in different sets, what we have
is a new connection between all the cities in one set to all the cities
in the other. All the cities in both sets must, therefore, be connected,
so we merge the two sets. When we have seen all the roads, the sets we
are left with are the sets of connected cities; if there is a connection
from one city to another (and vice versa), then they two cities are in
the same set, if there is not, they will be in separate sets. To solve
our original problem, to determine whether city $A$ (number 0) is
connected to city $B$ (number 13), we can now directly determine if 0 is
in the same set as 13.

We will iterate through all the roads, and then we will separate cities
into disjoint sets such that two cities are in the same set if and only
if they are connected through any of the roads we have seen so far. If,
when we have seen all the roads, index 0 and index 13 are in the same
set, then we know there is a route from $A$ to $B$.

An outline of the algorithm could look like this:

1.  Start with a set of singleton sets $S = \{ \{i\} \}$ for all cities
    $i$.
2.  for each road $(p,q)$ let $s_p$ and $s_q$ be the sets that $p$ and
    $q$ belong to, respectively. Update $S$ to be
    $S - s_p - s_q + s_p \cup s_q$ where $- s_p - s_q$ means removing
    the sets that $p$ and $q$ belongs to and $+ s_p \cup s_q$ means
    adding the union of these two sets.
3.  Once all roads have been processed, check if $s_0 = s_{13}$.

### Assertions and invariants

Once we have an algorithm sketched out at the overall level, it is time
to flesh out exactly what each step can expect from the preceding steps
and what it must guarantee for those steps that come after it. Such
requirements and promises are usually called *assertions*; the claims we
make for what should be true *before* a step are called
*pre-conditions*, and the claims that should be true *after* a step are
called *post-conditions*. Pre- and post-conditions should match up so
that the post-conditions of one step implies the pre-conditions of the
following step; they need not be the same conditions, but the
post-conditions of one step cannot be weaker than the pre-conditions of
the next.

To ensure that the algorithm works according to plan, we need each step
to guarantee its post-conditions, which then allows each step to then
assume that its pre-conditions are met. If the final post-condition says
that the problem is solved, and the pre-condition is true for all input
would need to apply the algorithm on, then we know that we have a
correct algorithm.

The essential property we want satisfied while we run our example
algorithm is this: if the city $i$ and the city $j$ are connected
through any of the roads we have seen so far, then $s_i=s_j$. There are
other properties that we will leave implicit, such as $S$ being a set of
disjoint sets of cities where all cities are represented. That is
important as well, but we won't make it an explicit condition in this
example. We will instead focus on properties for how we represent sets
and ensure that this representation guarantees that two cities are in
the same set if they can be reached through the roads seen so far.

There are many different ways to implement sets and many ways to
implement their union. We will use a list. We represent our set $S$ as a
list that holds a value for each city, $i$. This value is our
representation of a set. If you can pick one element in a set as a
representative of the set, and do so consistently, so the same set is
always represented by the same value, then you can use that element to
represent the set. For our sets, we will pick the city with the highest
index. We will require the following: `S[i]` contains the largest index
of a city, reachable from $i$, via the roads seen so far. Call this
property $I(S, R)$ where $S$ is the set of sets and $R$ is the set of
the roads I have seen so far. I use $I$ because I want it as an
invariant, i.e., I want it always to be true. I won't manage that
* precisely*, but it will be true most of the time.

Now, with this property about the set $S$, I will annotate the algorithm
like this:

1.  Start with a set of singleton sets `S[i] = i` for all cities $i$.
2.  $\langle\, I(S, \emptyset) \,\rangle$
3.  For each new road $r=(p,q)$, let $R$ denote the roads we have seen
    so far.
    1.  $\langle\, I(S, R) \,\rangle$
        2.  Set $S$ to $S - s_p - s_q + s_p \cup s_q$
        3.  $\langle\, I(S, R\cup\{(p,q)\}) \,\rangle$
4.  $\langle\, I(S, R) \,\rangle$ where $R$ is the set of all our roads.
5.  Once all roads have been processed, check if `S[0] == S[13]`.

For the initialisation in line 1 you can iterate through the cities and
append their indices to a list, or you can create the right list
succinctly like this:

``` {.python}
N = 14 # number of cities
S = list(range(N))
```

The statements wrapped in angle-brackets ($\langle - \rangle$) are the
assertions we make about the state of the algorithm. They are not part
of the algorithm as such. We never consider them something the algorithm
has to do, although we sometimes write code that checks if they are
satisfied when debugging an algorithm. They help us guide the design of
the algorithm and later they will help us prove correctness.

Actually, we can prove correctness right now if we just assume that the
steps between the assertions will satisfy them. The condition in line
2---a post-condition for the initialisation in line 1 but a
pre-condition for the loop---ensures that we have the right set when we
haven't seen any nodes. The conditions in line 3.1 and 3.3 guarantees us
that we update the set correctly for each new road we see, so we always
know if two cities are connected via the roads seen so far. Finally, we
know from line 4 that when we exit the loop, our set $S$ is a partition
of cities that exactly matches which are reachable from each other, and
thus, using the set we can answer the question of whether we can get
from city 0 to city 13 in line 5.

The conditions in lines 3.1 and 3.3 are the same except for 3.3 having
processed one more road than 3.1. Often, we will lump such two
conditions together and call it a *loop invariant*. We want loop
invariants always to be true just before we execute a loop body and
still to be true, in an updated form, when we finish running the loop
body. If we focus on the loop, where the real work will be done, we have
a pre-condition (for the loop) at line 2 and a post-condition at line 4.
In between, we have the loop-invariant, lines 3.1 and 3.3. To get the
algorithm to work correctly, we need to guarantee the following:

-   Before we enter the loop the pre-condition must be true and it must
    also imply that the loop-invariant is satisfied.
-   As long as the loop invariant is satisfied before we execute the
    body of the loop, it must also be satisfied after we have completed
    the body.
-   If the loop invariant is true when we exit the loop, then this must
    imply the post-condition for the loop.

That the pre-condition guarantees the loop invariant before we process
the first road, and that the loop invariant after we have processed the
last road guarantees the post-condition, are almost trivial to see in
this particular algorithm. Before the first road is processed, we have
$R=\emptyset$ making conditions in lines 2 and 3.1 the same. After the
last road, $(p,q)$, is processed, $R\cup\{(p,q)\}$ will be the set of
all roads, making the condition on line 3.3 the same as the
post-condition for the loop on line 4. If the step in line 3.2 updates
$S$ correctly, by merging the sets on either side of the road $(p,q)$,
then the loop invariant is satisfied after we have processed each road.
Some details are missing in step 3.2, though, so we need to get those
sorted out.

To get the final piece of the problem into place, we consider the
property $I(S,R)$ in more detail. It states that $S[i]$ should contain
the highest index for cities that are connected to $i$. This means that,
if $s_i$ is the set that contains $i$, then for all $j\in s_i$,
$S[j]=S[i]$, because *all* cities in set $s_i$ points to the largest
index in the set. This means that we can use the list `S` both to check
if two sets are equal, but also to get all elements in a set. The set
$s_i$ is represented by some index $k$ where `S[i] == k`. All other
elements in the set are those $j$ with `S[j] == k`.

When we want to merge the sets $s_p$ and $s_q$ when processing road
$(p,q)$ we can first check if the sets are different in the first place.
If `S[p] == S[q]`, the sets are already the same, and we do not need to
do anything. If not, we need to first find the representative element
for the union of the two. That will be `max(S[p],S[q])`. We then need to
update all elements in $s_p$ and $s_q$ to point to this element.

We can implement the loop like this:

``` {.python}
for p, q in roads:
    rep_p = S[p]
    rep_q = S[q]

    if rep_p == rep_q:
        continue # p and q are already connected

    new_rep = max(rep_p, rep_q)
    for i in range(N):
        if S[i] == rep_p or S[i] == rep_q:
            S[i] = new_rep
```

If we run this algorithm and print the content of `S` at each step, we
will get the following:

``` {.python}
# Initial state
S = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Entering loop...
S = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
S = [2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
S = [3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
S = [4, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
S = [5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13]
S = [5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13]
S = [6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13]
S = [6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13]
S = [7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 10, 11, 12, 13]
S = [8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 10, 11, 12, 13]
S = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 11, 12, 13]
S = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 11, 12, 13]
S = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 12, 13]
S = [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 13]
S = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13]
S = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
S = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
# After loop
S = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
```

You can check yourself that the states during the algorithm satisfy the
invariants. Just because the algorithm does the right thing on this
example, however, doesn't guarantee that it will work on all input. We
need to prove that if the loop invariant is satisfied before executing
the loop body, which is this code

``` {.python}
    rep_p = S[p]
    rep_q = S[q]

    if rep_p == rep_q:
        continue # p and q are already connected

    new_rep = max(rep_p, rep_q)
    for i in range(N):
        if S[i] == rep_p or S[i] == rep_q:
            S[i] = new_rep
```

the loop invariant will also be satisfied after the body is executed,
but with one more road processed. For this algorithm, proving that the
loop invariant is satisfied is relatively simple. We know that the
invariant is satisfied if the set of sets, $S$, is updated correctly,
which means that all elements in $s_p$ and all elements in $s_q$ should
now be in $s_p\cup s_q$, i.e., for all $i\in s_p$ and all $i\in s_q$,
`S[i] = k` where $k$ is the representative for the set $s_p\cup s_q$.
The loop (inside the outer-loop body) identifies all the cities we need
to update and does the update. So we are good.

Breaking down the steps we need to take to solve a problem, and then
asserting what should hold true before and after any step, is a potent
approach both for designing algorithms and proving their correctness. It
is not necessarily easy, however. It might look simple when following
the steps taken when I have written them down, but I had to work at
getting just the right invariants in this example, and I already knew
how the algorithm would work. When you don't know what the final
algorithm will look like, it gets more difficult. As with everything
else in life, though, it gets easier with practice, so do not skip the
exercises later in this chapter. In many of the algorithms, you need to
come up with invariants to prove correctness, and in a few of the
exercises, you also need to derive an algorithm from scratch.

### Measuring progress

When we loop, we do not necessarily know in advance how many steps we
need for any given problem. When you use a `for`-loop, you iterate over
a number of elements in a sequence, and the length of that sequence
often depends on the input.

Whenever we need an unknown number of steps to solve a problem, we have
the issue of termination. To have a proper algorithm, we need to ensure
that we only need a finite number of steps on any valid input. To ensure
this, we want each step to take us closer to the final solution. If we
can, somehow, associate a measure of progress towards the ultimate
solution to each step, in such a way that we will always reach the
solution and not merely move asymptotically towards it, then we can
prove that our algorithm will eventually terminate.

We usually do not worry about capturing the progress we make towards our
goal outside of a loop. Computations we make outside of a loop are only
ever done once, so there is no concern about them preventing
termination. We usually do not worry about `for`-loops either, since in
most cases they iterate over each element in a finite sequence. It is
possible to create infinite sequences in Python, but we will not
consider such constructions in this book, so all `for`-loops we see are
guaranteed to terminate. We might not know exactly how many times a loop
body will be executed, but we know that it is finite as long as the
sequence we iterate over is finite.

The real issue is when we have `while`-loops. With those, we keep
iterating until the loop condition evaluates to `False`, so we need to
ensure that this will eventually happen.

Consider this problem: given two numbers, `n` and `m`, we want to
compute how many times `m` divides `n` and what the remainder is. We can
readily do this in Python using the (integer) division and modulus
operator

``` {.python}
n = 42
m = 11
print(n // m, n % m)
```

but assume, for the sake of the example, that we did not have those
operators. A simple approach to solving the problem would then be to
repeatedly remove `m` from `n` until we are left with a number less than
`m`. In Python, this could look like this:

``` {.python}
a = n ; p = 0
while a >= m:
    a -= m
    p += 1
print(p, a)
```

After running this algorithm, `p` will be `n // m` and `a` will be
`n % m`. I will leave it to the reader to come up with a loop invariant
that can be used to prove the correctness of this and focus on how we
demonstrate that the computation terminates.

To ensure that the loop terminates, we must prove that eventually
`a >= m` will be false, i.e., that eventually `a` will be less than `m`.
It should be obvious that this happens with this simple algorithm, since
we decrease `a` in each iteration and we never increase it, but to
formalise this reasoning we can say that we associate with the loop a
*termination* function, $t$, that measures how close we are to the point
where the loop condition is false. Thinking in terms of such a function
will help us when the loops are more complicated than this one.

Such a termination function should have the following properties:

1.  The termination function maps the algorithm's state to a number.
2.  In each iteration, it is decreasing.
3.  The loop condition is `False` when the termination function is at or
    below zero.

For the first point, we need to know what we mean when we say " the
algorithm's state". This is just the value of all the variables we use
in the algorithm. We want the termination function to be a map the
current value of the variable to a number that measures how far we are
from completion. We don't need to use all the variables, but if it
depends on none of them, then the value it gives us will never change,
and we cannot ensure the other two points. In our simple algorithm, we
have a loop condition that depends only on `a` and `m`; our termination
function will also only depend on these. We define it to be

$$t(a,m) = a - m$$

Here, the termination function only depends on the variables used in the
loop condition, but this need not always be the case. The condition
variables might not capture all the information in the algorithm that is
needed to measure progress. Then we have to make it depend on more
variables.

The second and third conditions to the termination function should be
more straightforward to interpret. If we can show that $t(a,m)$
decreases in each iteration and that $t(a,m)\le 0$ implies that the loop
condition is `False`, then we are guaranteed termination. Well, we are
also implicitly assuming that the function doesn't converge
asymptotically towards zero. That is, it is not sufficient to require
that $t$ always decreases if it can get arbitrarily close to zero but
never reach zero. There are cases where we use algorithms to approximate
a value to within a given acceptable error. In such cases, we need to
require that it converge to a negative number. For example, if we have
an algorithm that approximates a number, $x$, by a computed value
$\hat{x}$, to within an error $\epsilon$, i.e., it computes a value
$\hat{x}$ such that $|x-\hat{x}|<\epsilon$, then we can use a
termination function that is $t(\hat{x})=|x-\hat{x}|-\epsilon$. If
$\hat{x}$ moves asymptotically towards $x$, then $|x-\hat{x}|$ converges
to zero but might not necessarily reach zero. It will, however, if we
set up the algorithm correctly, get within a distance less than
$\epsilon$ at some point, and at that point, the termination function
will be negative.

For our example algorithm, conditions two and three are easy to prove.
In each iteration, we decrease `a` while `m` never changes, so the
termination function must decrease by the same amount that `a` is
decreased by. This guarantees the second condition. For the third
condition, we simply observe that when $t(a,m)=m-a \le 0$, the condition
`a >= m` must be `False`.

Let us consider another, equally simple, example. Say we want to print
out the bits that the binary representation of a number is. We can
attack this problem in two different ways. We can use arithmetic where
we can get the least significant bit by taking modulus two and then
shift the remaining bits down by dividing by two.

``` {.python}
reverse_bits = []
while n > 0:
    reverse_bits.append(n % 2)
    n //= 2
print(reverse_bits[::-1])
```

The loop-condition is `n > 0`, so a natural choice for the termination
function is $t(n) = n$. Let us check if that works. Obviously, the
function maps the algorithmic state to a number, the value of the
variable `n`. This variable is decreased in each iteration when we set
`n` to half its current value. When `n` is eventually at zero, the
loop-condition is false. So this would be a termination function that
proves that this algorithm terminates.

As a final example, where the termination function doesn't only depend
on the variables in the loop condition, we can consider finding the
roots of a function, i.e., values where it is zero. We consider a simple
polynomial

$$p(x) = x^3 - 3 x^2 + 1$$

This polynomial is positive at $x=0$, where $p(0)=1$, and negative at
$x=1$, where $p(1) = -1$, so from basic calculus we know that somewhere
between zero there is an $x$ such that $p(x)=0$. To find that point we
will keep reducing the interval we search in until the midpoint of the
interval is within $\epsilon$ of $0$, i.e. we look for an $x$ where
$|p(x)|<\epsilon$. (The polynomial has three real roots, but only one
between zero and one, so the one we are looking for is
$x\approx 0.65720$.)

The algorithm looks like this:

``` {.python}
a = 0 ; b = 1
x = (a + b) / 2
epsilon = 0.01

val = x ** 3 - 3 * x ** 2 + 1
while abs(val) > epsilon:
    if val > 0:
        a = x
    else:
        b = x
    x = (a + b) / 2
    val = x ** 3 - 3 * x ** 2 + 1
```

In the algorithm, we set `x` to the midpoint between `a` and `b`, two
variables that define our interval and that starts out as 0 and 1
respectively. We then get the value of the polynomial in that midpoint
and check if it is positive or negative. We know it should be positive
to the left of the root and negative to the right of the root, so if our
value is not sufficiently close to zero, we move one of the interval
endpoints to the right or left depending on the value the function takes
at the midpoint.

To construct a termination function for this algorithm, we need a little
bit of calculus. We need to know that as $x$ tends toward the root we
are looking for, $r$, the polynomial will tend towards zero (from
negative or positive numbers, depending on whether we approach from the
left or right), i.e. $p(x)\to 0$ as $x\to r$. This tells us that if we
keep decreasing the size of the interval $[a,b]$, $x$ will tend to $r$
and $p(x)$ will tend to zero. We don't know how close $x$ needs to be to
$r$ before $p(x)<\epsilon$, but we do know that such a number exist, and
we can call it $\delta$.

That gives us the termination function we are after:
$t(a,b)=b-a-\delta$. Clearly, this is a mapping from algorithmic states
to a number, even if it is not a mapping of the variables that appear in
the loop-condition. It decreases in each iteration because we cut the
size of the interval in half when we replace an endpoint with a
midpoint. Once $|x-r|<\delta$ the termination function will be negative,
but at the same time $|p(x)|<\epsilon$ by definition of $\delta$, and
the loop-condition will be `False`.

The last example is a bit more complicated than the previous two, but
usually, coming up with a termination function is not that complicated,
and the situation is more like the first two examples than the last.
There is even less reason to despair because in most cases, you don't
*need* to come up with a termination function. Anytime you use a
`for`-loop over a finite sequence, you can simply use the number of
remaining elements for your termination function, and that works for all
`for`-loops over finite sequences.

Exercises for sequential algorithms
-----------------------------------

The following exercises test that have understood algorithms and
algorithmic design in sufficient detail to reason about termination and
correctness and that you have enough experience with Python programming
to implement simple sequential (also known as iterative) algorithms.
Here, by sequential, I only mean that the algorithms iterate through one
or more loops to achieve their goal.

### Below or above

Here's a game you can play with a friend: one of you think of a number
between 1 and 20, both 1 and 20 included. The other has to figure out
what that number is. He or she can guess at the number, and after
guessing will be told if the guess is correct, too high, or is too low.
Unless the guess is correct, the guesser must try again until the guess
*is* correct.

The following program implements this game for the case where the
computer picks the number, and you have to guess it. Play with the
computer as long as you like.

``` {.python}
# This is code for picking a number. You don't need
# to understand it but can just go to the loop below.
from numpy.random import randint
def input_integer(prompt):
    while True:
        try:
            inp = input(prompt)
            i = int(inp)
            return i
        except:
            print(inp, "is not a valid integer.")

# When picking a random number, we specify the interval
# [low,high). Since high is not included in the interval, 
# we need to use 1 to 21 to get a random number in the
# interval [1,20].
n = randint(1, 21, size = 1)
guess = input_integer("Make a guess> ")
while guess != n:
    if guess > n:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")
    guess = input_integer("Make a guess> ")
print("You got it!")
```

The `input_integer()` can be implemented like this:

``` {.python}

from numpy.random import randint

def input_integer(prompt):
    while True:
        try:
            inp = input(prompt)
            i = int(inp)
            return i
        except:
            print(inp, "is not a valid integer.")
```

Here are three different strategies you could use to guess the number:

1.  Start with one. If it isn't the right number, it has to be too
    low--there are no smaller numbers the right one could be. So if it
    isn't one, you guess it is two. If it isn't, you have once again
    guessed too low, so now you try three. You continue by incrementing
    your guess by one until you get the right answer.
2.  Alternatively, you start at 20. If the correct number is 20, great,
    you got it in one guess, but if it is not, your guess must be too
    high---it cannot possibly be too small. So you try 19 instead, and
    this time you work your way down until you get the right answer.
3.  Tired of trying all numbers from one end to the other, you can pick
    this strategy: you start by guessing 10. If this is correct, you are
    done, if it is too high, you know the real number must be in the
    interval $[1,9]$, and if the guess is too low, you know the right
    answer must be in the interval $[11,20]$---so for your next guess,
    you pick the middle of the interval it must be. With each new guess,
    you update the range where the real number can hide and choose the
    middle of the previous range.

**Exercise:** Prove that all three strategies terminate and with the
correct answer, i.e. they are algorithms for solving this problem.

**Exercise:** Would you judge all three approaches to be equally
efficient in finding the right number? If not, how would you order the
three strategies such that the method most likely to get the correct
number first is ranked highest, and the algorithm most likely to get the
right number last is rated lowest. Justify your answer.

If you do not lie to the computer when it asks you about its guess
compared to the number you are thinking of, this program implements the
first strategy:

``` {.python}
# This is code for picking a choice. You don't need
# to understand it but can just go to the loop below.
def input_selection(prompt, options):
    """Get user input, restrict it to fixed options."""
    modified_prompt = "{} [{}]: ".format(
        prompt.strip(), ", ".join(options)
    )
    while True:
        inp = input(modified_prompt)
        if inp in options:
            return inp
        # nope, not a valid answer...
        print("Invalid choice! Must be in [{}]".format(
            ", ".join(options)
        ))

for guess in range(1,21):
    result = input_selection(
        "How is my guess {}?".format(guess),
        ["low", "hit", "high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break
    else:
        print("I must have been too low, right?", result)
```

**Exercise:** Implement the other two strategies and test them.

When iterating from 20 and down, for the second strategy, you should
always get the result `"high"` when you ask about your guess, so you can
use a `for` loop and not worry about the actual result form
`input_selection`. When you implement strategy number three, however,
you need to keep track of a candidate interval with a lower bound,
initially 1, and an upper bound, initially 20. When you guess too high,
you should lower your upper bound to the value you just guessed minus
one (no need to include the guess we know is too high). When you guess
too low, you must increase your lower bound to the number you just
guessed plus one. In both cases, after updating the interval, you should
guess for the middle point in the new range. When you compute the middle
value in your interval, you can use

``` {.python}
guess = (upper_bound + lower_bound) // 2
```

### Finding square roots

Given a positive number $S > 0$, we want to compute its positive square
root, $\sqrt{S}$. We don't need our answer to be perfectly accurate.
Using floating point numbers with a finite number of bits to represent
the uncountable set of real numbers prevents this anyway. However, we
want to be able to put an upper bound on the error we get, $\epsilon$,
such that we are guaranteed that for our result, $\hat{S}$, we have
$|S-\hat{S}|<\epsilon$.

One algorithm that solves this problem is known as the *Babylonian
method* and is based on two observations. The first is this: for any
$x>0$, if $x>\sqrt{S}$ then $S/x<\sqrt{S}$ and if $S/x>\sqrt{S}$ then
$x<\sqrt{S}$, i.e., if we guess at a value for the square root of $S$
and the guess is too high, we have a lower bound on what it *could* be,
and if the guess is too low, we have an upper bound on what it could be,
see [@fig:babylonian-method-range].

![Bounds for where to find the square root of $S$ depending on where $S$
lands.](Babylonian-method-range.pdf){#fig:babylonian-method-range}

To see that this is so, consider the case where $x>\sqrt{S}$ and
therefore $x^2>S$. This inequality naturally also implies that
$S/x^2 < x^2/x^2$, and from this we derive
$S=S\frac{x^2}{x^2}>S\frac{S}{x^2}=\left(\frac{S}{x}\right)^2$, i.e.,
$S/x<\sqrt{S}$. The other case is proven similarly.

Because of this, if we start out knowing nothing about $\sqrt{S}$, it
could be anywhere between $0$ and $S$, so we can make an initial guess
of some $x_0$, $0<x_0<S$. If $|S-x|<\epsilon$, then $x_0$ is an
acceptable output and we are done. If not, we know that $\sqrt{S}$ lies
in the interval $(x/S,x)$ (if $x^2>S$) or in the interval $(x,x/s)$ (if
$x^2<S$), and we can make a new guess inside that interval.

The Babylonian method for finding square roots follows this idea and
work as follows:

1.  First, make a guess for $x_0$,\~ e.g. \~$x_0=S/2$. Any number in
    $(0,S)$ will do.

2.  Now, repeat the following, where we denote the guess we have at
    iteration $i$ by $x_i$.

    1.  If $|S/x_i-x_i|<\epsilon$ report $x_i$.
    2.  Otherwise, update $x_{i+1}=\frac{1}{2}\left(x_i+S/x_i\right)$.

The test $|S/x_i-x_i|<\epsilon$ is different than the requirement we
made about the error we would accept, which was
$|\sqrt{S}-x_i|<\epsilon$, but since we don't know $\sqrt{S}$ we cannot
test that directly. We know, however, that $\sqrt{S}$ lies in the
interval $(S/x,x)$ or the interval $(x,S/x)$, so if we make this
interval smaller than $\epsilon$, we have reached at least the accuracy
we want.

The update $x_{i+1}=\frac{1}{2}\left(x_i+S/x_i\right)$ picks the next
guess to be the average of $x_i$ and $S/x_i$, which is also the midpoint
in the interval $(S/x,x)$ (for $x>S/x$) or the interval $(x,S/x)$ (for
$x<S/x$), so inside the interval we know must contain $\sqrt{S}$.

**Exercise:** From this description alone you can argue that *if* the
method terminates, it will report a correct answer. Prove that the
algorithm is correct.

In each iteration, we update the interval in which we know $\sqrt{S}$
resides by cutting the previous interval in half.

**Exercise:** Use this to prove that the algorithm terminates.

**Exercise:** Implement and test this algorithm.

Exercises on lists
------------------

Lists are representations of ordered sequences of elements. These
exercises involve algorithms where we have to examine or manipulate
lists to solve a problem.

### Changing numerical base

When we write a number such as 123 we usually mean this to be in base
10, that is, we implicitly understand this to be the number
$3 \times 10^0 + 2 \times 10^1 + 1 \times 10^2$. Starting from the right
and moving towards the left, each digit represents an increasing power
of tens. The number *could* also be in octal, although then we would
usually write it like $123_8$. If the number were in octal, each digit
would represent a power of eight, and the number should be understood as
$3\times 8^0 + 2 \times 8^1 + 3 \times 8^2$.

Binary, octal and hexadecimal numbers---notation where the bases are 2,
8, and 16, respectively---are frequently used in computer science as
they capture the numbers you can put in one, three and four bits. The
computer works with bits, so it naturally speaks binary. For us humans,
binary is a pain because it requires long sequences of ones and zeros
for even relatively small numbers, and it is hard for us to readily see
if we have five or six or so zeroes or ones in a row.

Using octal and hexadecimal is more comfortable for humans than binary,
and you can map the digits in octal and hexadecimal to three and
four-bit numbers, respectively. Modern computers are based on bytes (and
multiples of bytes) where a byte is eight bits. Since a hexadecimal
number is four bits, you can write any number that fits into a byte
using two hexadecimal digits rather than eight binary digits. Octal
numbers are less useful on modern computers, since two octal digits, six
bits, are too small for a byte while three octal digits, nine bits, are
too larger. Some older systems, however, were based on 12-bits numbers,
and there you had four octal numbers. Now, octal numbers are merely used
for historical reasons; on modern computers, hexadecimal numbers are
better.

Leaving computer science, base 12, called duodecimal, has been proposed
as a better choice than base 10 for doing arithmetic because 12 has more
factors than 10 and this system would be simpler to do multiplication
and division in. It is probably unlikely that this idea gets traction,
but if it did, we would have to get used to converting old decimal
numbers into duodecimal.

In this exercise, we do not want to do arithmetic in different bases but
want to write a function that prints an integer in different bases.

When the base is higher than 10, we need a way to represent the digits
from 10 and up. There are proposed special symbols for these, and these
can be found in Unicode, but we will use letters, as is typically done
for hexadecimal. We won't go above base 16 so we can use this table to
map a number to a digit up to that base:

``` {.python}
digits = {}

for i in range(0,10):
    digits[i] = str(i)

digits[10] = 'A'
digits[11] = 'B'
digits[12] = 'C'
digits[13] = 'D'
digits[14] = 'E'
digits[15] = 'F'
```

To get the last digit in a number, in base $b$, we can take the division
rest, the modulus, and map that using the `digits` table:

``` {.python}
digits[i % b]
```

Try it out.

You can extract the base $b$ representation of a number by building a
list of digits starting with the smallest. You can use `digits[i % b]`
to get the last digit and remember that in a list. Then we need to move
on to the next digit. Now, if the number we are processing is
$n = b^0 \times a_0 + b^1\times a_1 + b^2 \times a_2 + \cdots + b^m a_m$,
then $a_0$ is the remainder in a division by $b$ and the digit we just
extracted. Additionally, if $//$ denotes integer division,
$n//b=b^0\times a_1 + b^1 \times a_2 + \cdots b^{m-1}a_m$. So, we can
get the next digit by first dividing $n$ by $b$ and then extract the
smallest digit.

If you iteratively extract the lowest digit and put it in a list and
then reduce the number by dividing it by $b$, you should eventually have
a list with all the digits, although in reverse order. If your list is
named `lst`, you can reverse it using this expression `lst[::-1]`. The
expression says that we want `lst` from the beginning to the end---the
default values of a range when we do not provide anything---in steps of
minus one.

**Exercise:** Flesh out an algorithm, based on the observations above,
that can print any integer in any base $b\le 16$. Show that your method
terminates and outputs the correct string of digits.

### The Sieve of Eratosthenes

> *Sift the Two's and Sift the Three's,*
>
> *The Sieve of Eratosthenes.*
>
> *When the multiples sublime,*
>
> *The numbers that remain are Prime.*

The Sieve of Eratosthenes is an early algorithm for computing all prime
numbers less than some upper bound $n$. It works as follows: we start
with a set of candidates for numbers that could be primes, and since we
do not a priori know which numbers will be primes we start with all the
natural numbers from two and up to $n$.

``` {.python}
candidates = list(range(2, n + 1))
```

We are going to figure out which are primes by elimination and put the
primes in another list that is initially empty.

``` {.python}
primes = []
```

The trick now is to remove from the candidates the numbers we know are
not primes. We will require the following loop invariants:

1.  All numbers in `primes` are prime.
2.  No number in `candidates` can be divided by a number in `primes`.
3.  The smallest number in `candidates` is a prime.

**Exercise:** Prove that the invariants are true with the initial lists
defined as above.

We will now loop as long as there are candidates left. In the loop, we
take the smallest number in the `candidates` list, which the invariant
states must be a prime. Call it $p$. We then remove all candidates that
are divisible by $p$ and then add $p$ to `primes`.

**Exercise:** Prove that the invariants are satisfied after these steps
whenever they are satisfied before the steps.

**Exercise:** Prove that this algorithm terminates and is correct, i.e.,
that `primes` once the algorithm terminates contain all primes less than
or equal to $n$. Correctness does not follow directly from the
invariants so you might have to extend them.

**Exercise:** Implement and test this algorithm.

### Longest increasing substring

Assume you have a list of numbers, for example

``` {.python}
x = [12, 45, 32, 65, 78, 23, 35, 45, 57]
```

**Exercise:** Design an algorithm that finds the longest sub-sequence
`x[i:j]` such that consecutive numbers are increasing,
i.e. `x[k] < x[k+1]` for all `k` in `range(i,j)` (or one of the longest,
if there are more than one with the same length).

### Compute the powerset of a set

The *powerset* $P(S)$ of a set $S$ is the set that contains all possible
subsets of $S$. For example, if $S=\{a,b,c\}$, then

$$P(S) = \{\emptyset,\{a\}, \{b\}, \{c\}, \{a,b\}, \{a,c\}, \{b,c\}, \{a,b,c\}\}$$

**Exercise:** Assume that $S$ is represented as a list. Design an
algorithm that prints out all possible subsets of $S$. Prove that it
terminates and is correct.

*Hint:* You can solve this problem by combining the numerical base
algorithm with an observation about the binary representation of a
number and a subset of $S$. We can represent any subset of $S$ by the
indices into the list representation of $S$. Given the indices, just
pick out the elements at those indices. One way to represent a list of
indices is as a binary sequence. The indices of the bits that are 1
should be included, the indices where the bits are 0 should not. If you
can generate all the binary vectors of length `k=len(S)`, then you have
implicitly generated all subsets of $S$. You can get all these bit
vectors by getting all the numbers from zero to $2^k$ and extracting the
binary representation.

### Longest increasing subsequence

Notice that this problem has a different name than "longest increasing
*substring*"; it is a slightly different problem. Assume, again, that
you have a list of numbers. We want to find the longest sub-sequence of
increasing numbers, but this time we are not looking for consecutive
indices `i:j`, but a sequence of indices $i_0,i_1,\ldots,i_m$ such that
$i_k<i_{k+1}$ and $x[i_k] < x[i_{k+1}]$.

**Exercise** Design an algorithm for computing the longest (or a
longest) such sequence of indices $i_0,i_1,\ldots,i_m$.

*Hint:* This problem is harder than the previous one, but you can brute
force it by generating *all* subsequences and checking if the invariant
is satisfied. This is a *very* inefficient approach, but we need to
learn a little more about algorithms before we will see a more efficient
solution.

### Merging

Assume you have two sorted lists, `x` and `y`, and you want to combine
them into a new sequence, `z`, that contains all the elements from `x`
and all the elements from `y`, in sorted order. You can create `z` by
*merging* `x` and `y` as follows: have an index, `i`, into `x` and
another index, `j`, into `y`---both initially zero---and compare `x[i]`
to `y[j]`. If `x[i] < y[j]`, then append `x[i]` to `z` and increment `i`
by one. Otherwise, append `y[j]` to `z` and increment `j`. If either `i`
reaches the length of `x` or `j` reaches the end of `y`, simply copy the
remainder of the other list to `z`.

**Exercise:** Argue why this approach creates the correct `z` list and
why it terminates.

Algorithmic efficiency {#sec:algorithmic-efficiency}
======================

As a general rule, we want our algorithms to work as efficiently as
possible, which usually means that we want them to quickly solve the
problem they are designed for using as few resources, such as memory or
disk space, as possible. This is just a rule of thumb, of course,
because we also need to factor in programmer time. If you need a problem
solved a month from now, and you have the choice between an algorithm
that can solve the problem in two weeks and takes one week to implement,
that is preferable over an algorithm that can solve the problem in an
hour but takes a month to implement.

It is notoriously hard to estimate how long it will take to implement a
new algorithm, however, as this depends on the skills of the programmer,
the chosen programming language, and which libraries are available; we
will not attempt to do that here. With experience, you will get a feel
for how hard it will be to implement any given algorithm, and while you
are unlikely ever to be able to estimate precisely how much work goes
into implementing one, you will be able to determine which of two
choices is the more complex algorithm. Unless there are good reasons for
wanting a more complicated but potentially more efficient algorithm, you
should go for the most straightforward algorithm that can get the job
done. Sometimes, the simplest algorithm *will* be too slow for your
problem, and you have to replace it with a more complex one. Or
sometimes you expect to run your algorithm many times on many data sets,
and spending a little more programming time for faster execution down
the line might pay off. But as a general rule, you do not want to spend
more time programming than what is warranted for your problem.
Programmer-time is much more valuable than computer-time, so simple
algorithms that can be implemented quickly are generally preferable to
more sophisticated algorithms that are hard to implement.

This chapter is not about the complexity of algorithms in the sense of
how complicated they are to implement. Instead, it is about how
efficiently algorithms solve a problem once implemented. That is, the
chapter is about how fast you can expect an algorithm to complete its
job on any given data. Whenever you have the choice between two
algorithms that look roughly equally complicated to implement, you want
to go with the one that is likely to be the most efficient of the two.

The best way to measure which of two algorithms is superior for solving
a given problem is, of course, to program the best implementations of
the two that you can manage and then measure how fast they are on your
data. Whichever you stopwatch tells you is the best, unquestionably is.
That, of course, is not an option if your focus is on actually solving a
problem rather than comparing two algorithms. To answer your question
that way, you have to do twice the work. You need to implement both
algorithms and then run both of them on your actual data. What we need
is a way of reasoning about how likely it is that one algorithm is
better than another without using a stop-watch.

The way we reason about algorithmic efficiency is similar to how we
reason about the physical world when we do science: we use a model of a
computer that is much simpler than the real thing, but one we can reason
about without too many complications. We then work out how many
primitive operations an algorithm needs to make on the input we give it.
This is not an entirely accurate measurement of how long the actual
algorithm will run on a real computer, but it is a reasonable estimate.

To make it even simpler to reason about efficiency than this, we often
don't care about counting the number of primitive operations accurately
either. We will only care about how the number of calculations depends
on the input in an asymptotic sense that should be clear by the end of
this chapter. This might sound a bit sloppy, but there is a mathematical
underpinning that justifies this, and by using this approach we can very
quickly determine which of two algorithms is likely to be faster than
the other.

The RAM model of a computer and its primitive operations
--------------------------------------------------------

Any actual computer you will ever use is a very complex machine. At its
core is a gazillion transistors, wired together to implement different
logical operations in hardware. The hardware in your computer handles
both simple computations, such as comparing numbers or doing arithmetic,
and manages how data is moved around. Information is stored different
places in such a computer; you have persistent storage on disk, that
lives outside of running programs, and while programs run, you have data
moving between different layers of memory hierarchies. At the core of
the computer is one or more central processing units, or CPUs, that do
actual computations.[^5] Data needs to be moved to these CPUs for them
to compute on it. They can hold some data themselves, in what is called
*registers*, and they can do computations on such data very quickly.
There is only a finite number of registers, though, so data needs to be
moved to and from these registers. Below registers are several layers of
memory called *caches*, and the closer caches are to the registers, the
faster data can be moved between them. Below caches, you have
*random-access memory*, or RAM, and below that, disks, which can be
solid state or actual rotating disks, or some combination thereof.

The levels of the memory hierarchy are vital to the actual performance
of an algorithm. Every time you move data from one level to the next,
the time it takes to access it grows by orders of magnitude. Your CPUs
can compute on data much faster than it can fetch it from memory and put
it back. Moving data up and down the memory hierarchy, however, is
handled automatically by the computer, so we don't have to deal with it
explicitly. We can construct algorithms that ignore the memory hierarchy
entirely and still get well-working programs. Considering the memory
hierarchy can help us improve the running time of a program immensely,
but doing this also hugely complicates our algorithms, and in many
cases, solutions will depend on the actual hardware our software runs
on.

I am mentioning all this to make it clear that considering any actual
computer dramatically complicates how we can reason about the actual
performance of an algorithm. If we have to consider any real computer,
reasoning about running time becomes practically impossible. When we
reason about algorithmic complexity, we use much simpler models of
computers, and a traditional model is the so-called *RAM model*.

The critical property of the RAM model is that we assume that any data
we need and know where to find, we can access in constant time. We
understand that there is such a thing as a *computer word*, which you
should think of as a number, a character, or a primitive piece of data
like that. We cannot store arbitrarily large chunks of data in single
computer words, but we assume that if the size of the input data for
your algorithm is $n$, then our computer words can hold at least the
number $n$. In other words, if your input data is of size $n$, then you
can represent $\lceil \log_2 n \rceil$ bits in a single computer word.
Any computer word in our input data, or any computer word we create in
our algorithm, can be accessed on constant time. We ignore that some
computer words can be located much faster than others; they are all just
accessible in constant time. We also assume that we can compare computer
words in constant time and that any arithmetic operation we do on
numbers that can be stored in a single computer word can be done in
constant time.

The reason we have to be a little careful about what a computer word is
that we want to make the assumption about how fast we can perform
calculations on them. We want our abstract computer words to roughly
match what the actual computer can work within its registers. In the
hardware of a real computer, the different operations you can do on
numbers and bit-patterns are wired together, so the CPUs consider
operating on words in registers as primitive operations. The time it
takes actual hardware to do a primitive operation depends on what that
operation is. The hardware for multiplication is more complicated than
the hardware for simple comparison, but a lot of the computation
involves parallel calculations, and at a rough approximation, all
primitive operations take the same time. To actually compare two numbers
that can be up to $n$ large, we need to compare $\lceil \log_2 n \rceil$
bits, so it *isn't* constant time, but if a computer word has at least
that many bits, we can; then it is a single CPU operation.

As long as you do not work with numbers that are larger than the size of
the input, the RAM model says that:

1.  You can compare numbers in constant time.
2.  You can access any computer word in constant time.
3.  You can do any arithmetic or bit-wise operation on computer words in
    constant time.

This is a considerable simplification of actual hardware. If we make
these simple assumptions about how fast our model of a computer can do
calculations, and we assume that all such operations take the same
amount of time, then we can just count how many of these primitive
operations an algorithm will need on any given input to get an estimate
of how fast it will run.

Let us try counting primitive operations in a small example. Let us
assume that we have a list of numbers,

``` {.python}
numbers = [1, 2, 3, 4, 5]
```

In this case, we have $n=5$ numbers. We usually do not count the
operations it takes to get our input. Sometimes, we need to read it in
from disk, or in this example, we need to tell Python what the numbers
are, and this will take around $n$ operations to create this list. If
the data is part of our input, however, we do not count those
instructions. The reason for this is that there are many algorithms
where we use less than $n$ operations to answer questions about our
data, and we do not want to have our analysis of the efficiency of these
dominated by how long it takes to get the input. Such algorithms are
used as building blocks for other algorithms that will be responsible
for getting the input in the right form for what we need, and we
consider that a cost of the other algorithm. If you need to create a
list as part of your algorithm, the number of operations this takes have
to be included in the accounting, but here we just assume that the input
is present before we start counting.

Let us now consider the task of adding all these numbers up. We can do
this using this algorithm:

``` {.python}
accumulator = 0
for n in numbers:
    accumulator += n
```

First, we create a variable to store intermediate values, `accumulator`.
Then we have a `for`-loop that runs over our input and for each
input-number add that number to `accumulator`. Initialising a variable
with a number amounts to setting a computer word to a value, so it takes
one operation in our RAM model. Adding two numbers is also a single
operation, and on all modern computers you can add a number to an
existing computer word as a single operation, so we consider
`accumulator += n` as a single operation---if you want to think about it
as `accumulator = accumulator + n` you can count it as two operations.
If, however, we consider updating `accumulator` a single operation, we
have $1 + n$ operations for initialising and updating `accumulator`. It
is less straightforward to know how many operations we spend on the
`for`-loop, however. That depends on how Python handles `for`-loop
statements. The `for`-loop construction is not as primitive as the RAM
model. We can implement the same loop using a `while`-loop, however,
using only primitive operations:

``` {.python}
accumulator = 0
length = len(numbers)
i = 0
while i < length:
    n = numbers[i]
    accumulator += n
    i += 1
```

Here, we have a more transparent view of the primitive operations a
`for`-loop likely implements. To iterate over a list, we need to know
how long it is.[^6] The statement

``` {.python}
length = len(numbers)
```

isn't actually primitive either. It uses Python's `len` function to get
the length of a sequence, and we don't know how many primitive
operations *that* takes. If we assume, however, that lists store their
lengths in a single computer word, which they really do, and that `len`
simply gets that computer word, which is not far from the truth, we can
consider this statement a single operation as well.[^7]

``` {.python}
accumulator = 0.        # one operation
length = len(numbers)   # one operation
```

We then initialise the variable `i` that we use to keep track of how
many elements we have processed. That is also a single primitive
operation.

The `while`-loop construction does two things. It evaluates its
condition and if it is `True` it executes the code in the loop body; if
it is `False`, it sends the program to the point right after the loop to
start executing the statements there, if any, if any are left. We call
such an operation a *branching operation* because it sends the point of
execution to one of two places, and such an operation is implemented as
a single instruction in hardware. So we will count the decision of where
to continue execution as a single operation. We need to evaluate the
loop condition first, however, which is a single numeric comparison, so
that takes another primitive operation. We evaluate the loop-condition
once for each element in `numbers`, i.e., $n$ times, so now we have:

``` {.python}
accumulator = 0         # one operation
length = len(numbers)   # one operation
i = 0                   # one operation
while i < length:       # 2n operations 
  ...
```

Each of the statements inside the loop-body will be evaluated $n$ times,
so we just need to figure out how many operations are required for each
of the statements there and multiply that with $n$. The last two
statements are simple, they update a number by adding another number to
them, and that is a single operation.

``` {.python}
accumulator = 0         # one operation
length = len(numbers)   # one operation
i = 0                   # one operation
while i < length:       # 2n operations 
    n = numbers[i]      # ? * n operations
    accumulator += n    # 2n operations
    i += 1              # 2n operations
```

The remaining question is how many operations it takes to handle the
statement `n = numbers[i]`. Here, we need to understand what something
like `numbers[i]` means. Once again, we use a Python construction that
we do not necessarily know how many operations take to execute. To
understand that, we need to know how Python represents lists in computer
memory, and that is beyond the scope of this chapter. You will have to
take my word on this, but it is possible to get the $i$'th element in a
list by adding two computer words and then reading one, so we count this
as two operations and end up with:

``` {.python}
accumulator = 0         # one operation
length = len(numbers)   # one operation
i = 0                   # one operation
while i < length:       # 2n operations 
    n = numbers[i]      # 2n operations
    accumulator += n    # n operations
    i += 1              # n operations
```

If we add it all up, we get that to compute the sum of $n$ numbers this
way, we need to use $3 + 6n$ primitive operations.

If we assume that all `for`-loops are implemented by first capturing the
length of the sequence, then setting a counter to zero, and then
iterating through the sequence, comparing the counter with the length as
the loop-condition and incrementing the counter at the end of the loop
body, and accessing elements in the sequence by indexing, i.e., that the
`for`-loop

``` {.python}
for element in a_list:
    # do something
```

can be translated into this `while`-loop

``` {.python}
length = length(a_list)        # 1 operation
counter = 0                    # 1 operation
while counter < length:        # 2n operations
    element = a_list[counter]  # 2n operations
    # do something
    counter += 1               # n operations
```

we can say that a `for`-loop iterating over a sequence of length $n$
takes $5n + 2$ operations. If we go back to our original `for`-loop
adding algorithm we then get

``` {.python}
accumulator = 0       # 1 operation
for n in numbers:     # 5n + 2 operations
    accumulator += n  # n operations
```

which gives us the same $6n + 3$ operations as before.

If you feel a bit overwhelmed by how difficult it is to count the number
of primitive operations in something as simple as this, I understand you
and feel for you. If it is this hard to count operations in the abstract
RAM model, where we even make some assumptions about how many operations
Python needs to implement its operations, you will understand why we do
not even attempt to accurately estimate how much time it will take to
execute code on a real computer.

The good news is that we very rarely do count the number of operations
an algorithm needs this carefully. Remember that I said, at the
beginning of the chapter, that we generally consider functions such as
$2x^2+x$ and $100x^2+1000x$ the same. We will also consider $6n + 3$ the
same as $n$ number of operations, in a way I will explain a little
later. First, however, you should try to count primitive operations in a
few examples yourself.

### Counting primitive operations exercises

**Exercise:** Consider this way of computing the mean of a sequence of
numbers:

``` {.python}
accumulator = 0
for n in numbers:
    accumulator += n
mean = accumulator / len(numbers)
```

Count how many primitive operations it takes. To do it correctly you
need to distinguish between updating a variable and assigning a value to
a new one. Updating the accumulator `accumulator += n` usually maps to a
single operation on a CPU because it involves changing the value of a
number that is most likely in a register. Assigning to a new variable,
as in

``` {.python}
mean = accumulator / len(numbers)
```

doesn't update `accumulator` with a new value, rather it needs to
compute a division, which is one operation (and it needs `len(numbers)`
before it can do this, which is another operation), and then write the
result in a new variable, which is an additional operation.

**Exercise:** Consider this alternative algorithm for computing the mean
of a sequence of numbers:

``` {.python}
accumulator = 0
length = 0
for n in numbers:
    accumulator += n
    length += 1
mean = accumulator / length
```

How many operations are needed here? Is it more or less efficient than
the previous algorithm?

Best-case, worst-case, and average-case efficiency
--------------------------------------------------

When computing the sum of a sequence of numbers, the number of
operations we need is independent of what the actual numbers are, so we
could express the number of operations as a function of the input size,
$n$. Things are not always that simple.

Consider this algorithm for determine if a number $x$ is in the sequence
of numbers `numbers`:

``` {.python}
in_list = False
for n in numbers:
    if n == x:
        in_list = True
        break
```

Here, we assume that both `numbers` and `x` are initialised beforehand.
The algorithm sets a variable, `in_list`, to `False`---one primitive
operation---and then iterates through the numbers. This would usually
cost us $5n + 2$ operations for the `for`-loop, but notice that we
`break` if we find the value in the list. We won't spend more than
$5n + 2$ operations on the `for`-loop, but we might spend considerably
less. Let us say that we iterate $m$ times, so the cost of the
`for`-loop is $5m + 2$ instead. Then we can count operations like this:

``` {.python}
in_list = False           # 1 operation
for n in numbers:         # 5m + 2 operations
    if n == x:            # 2m operations
        in_list = True    # 1 operation 
        break             # 1 operation
```

The `if`-statement is a branching operation just like the `while`-loop;
we need to compare two numbers, which is one operation, and then decide
whether we continue executing inside the `if`-body or whether we
continue after the `if`-block, which is another operation. Inside the
`if`-block, we have two primitive operations. Setting the variable
`in_list` is a primitive operation like before, and `break` is another
branching operation, that does not need a comparison first, but that
simply moves us to the point in the code after the loop. These two
operations are only executed once since they are only executed when the
`n == x` expression evaluates to `True`, and we leave the loop right
after that.

When we add up all the operations, we find that the algorithm takes
$7m + 5$ operations in total, where $m$ depends on the input. It is not
unusual that the running time of an algorithm depends on the actual
input, but taking that into account vastly complicates the analysis. The
analysis is greatly simplified if we count the running time as a
function of the size of the input, $n$, and do not have to consider the
actual data in the input.

For this simple search algorithm, we apparently cannot reduce the
running time to a function of $n$, because it depends on how soon we see
the value $x$ in the sequence, if at all. To get out of the problem, we
usually consider one of three cases: the *worst-case* complexity of an
algorithm, the *best-case* complexity, or the *average-case* complexity.

To get the worst-case estimate of the number of operations the algorithm
needs to take, we need to consider how the data can have a form where
the algorithm needs to execute the maximum number of operations it can
possibly do. In the search, if $x$ is not found in the sequence, we will
have to search the entire sequence, which is as bad as it gets, so the
worst-case time usage is $7n + 5$. If the very first element in
`numbers` is $x$, then $m=1$, which is as good as it gets, so the
best-case running time is 12 operations.

The average-case is much harder to pin down. To know how well our
algorithm will work on average we need to consider our input as randomly
sampled from some distribution---it does not make sense to think of
averages over something that doesn't have an underlying distribution the
data could come from, because then we would have nothing to average
over. Because of this, we will generally not consider average-case
complexities in this book. Average-case complexity is an important part
of so-called randomised algorithms, where randomness is explicitly used
in algorithms, and where we have some control over the data. To get a
feeling for how we would reason about average-case complexity, imagine
for a second that $x$ is in the `numbers` list but at a random location.
I realise that would make it very silly to run the algorithm in the
first place, since the result will always be `True`, but indulge me for
a second. If $x$ is a random number from `numbers`, then the probability
that it is at index $j$ for any $j$ in $1,\ldots,n$\~ is \~$1/n$. Since
we stop when we find the item we are searching for, our variable $m$ is
$j$ The mean of $m$ is therefore $\mathrm{E}[m]=\sum_{j=1}^n j/n$ which
is $\frac{n+1}{2}$. Plugging that into $7m + 5$ we get the average-case
time usage $7/2(n+1)+5$.

Of the three cases, we are usually most concerned with the worst-case
performance of an algorithm. The average-case is of interest if we have
to run the algorithm many times over data that is distributed in a way
that matches the distributions we use for the analysis, but for any
single input, it does not tell us much about how long the algorithm will
actually run. The best-case is only hit by luck, so relying on that in
our analysis is often overly optimistic. The worst-case performance,
however, gives us some guarantees about how fast the algorithm will be
on any data, however pathological, we give it.

### Exercise

Recall the guessing game from the previous chapter, where one player
thinks a number between 1 and 20 and the other has to guess it. We had
three strategies for the guesser:

1.  Start with one. If it isn't the right number, it has to be too
    low---there are no smaller numbers the right one could be. So if it
    isn't one, you guess it is two. If it isn't, you have once again
    guessed too low, so now you try three. You continue by incrementing
    your guess by one until you get the right answer.
2.  Alternatively, you start at 20. If the right number is 20, great,
    you got it in one guess, but if it is not, your guess must be too
    high---it cannot possibly be too small. So you try 19 instead, and
    this time you work your way down until you get the right answer.
3.  The third strategy is this: you start by guessing ten. If this is
    correct, you are done, if it is too high, you know the real number
    must be in the range $[1,9]$, and if the guess is too low, you know
    the right answer must be in the range $[11,20]$---so for your next
    guess, you pick the middle of the range it must be. With each new
    guess, you update the interval where the real number can be hidden
    and pick the middle of the new range.

**Exercise:** Identify the best- and worst-case scenarios for each
strategy and derive the best-case and worst-case time usage.

Asymptotic running time and big-Oh notation
-------------------------------------------

As we have seen, counting the actual number of primitive operations used
by an algorithm quickly becomes very tedious. Considering that all
operations are not actually equal, and given that memory-hierarchies
make access to different data more or less expensive, it also seems to
be a waste of time to be that precise in counting operations. If adding
ten numbers can be much faster than multiplying three, why should we
worry that the first involves nine operations and the second only two?
In fact, we very rarely do count the actual operations, and when we do,
it is for elementary but essential algorithms. What we really care about
is how the running time (or memory or disk space usage, or whatever
critical resource our algorithm uses) grows as a function of the input
size in some rough sense, that we will now consider.

When we have a function of the input size, $f(n)$, we care about the
*order* of $f$. We classify functions into classes and only care about
which class of functions $f$ belongs to, not what the actual function
$f$ is. Given a function $f$ we define its "order class" $O(f)$ as:

$$O(f) = \left\{\, g(n): \exists c\in\mathbb{R}^+, n_0\in\mathbb{N} : \forall n\in\mathbb{N} \geq n_0 : 0 \leq g(n) \leq c f(n) \,\right\}$$

Put into words, this means that the class of functions of order $f$ are
those functions $g(n)$ that, as $n$ goes to infinity, will eventually be
dominated by $f(n)$ times a positive constant $c$.

If $g$ is in $O(f)$ we write $g\in O(f)$, as per usual mathematical
notation, but you will often also see it written as $g=O(f)$. This is an
abuse of notation, but you might run into it, so I should mention it,
even if I will not use that notation myself.

Consider functions $f(n) = 10n + 100$ and $g(n) = 3n + 100,000$. We have
$g\in O(g)$ because, eventually, a line with incline 10 will grow faster
than one with incline 3, so eventually, regardless of where the lines
intersect the $y$-axis, the former will be above the latter. We also
have $f\in O(g)$ because we can simply multiply $g(n)$ by $10/3$ and it
is already above $f(n)$ because it intersects the $y$ axis at a higher
value. This "big-Oh" notation is not symmetric, however. Consider the
function $h(n)=n^2$. We have both $f\in O(h)$ and $g\in O(h)$ because,
regardless of where a line intersects the $y$-axis, $n^2$ will
eventually be larger than the line. We do *not* have $h\in O(f)$,
however, for exactly the same reason. There is no constant $n_0$ after
which a line, regardless of what its intercept is, will always be larger
than $n^2$.

When we write $f\in O(g)$ we provide an *upper bound* on $f$. We know
that as $n$ goes to infinity, $f(n)$ will be bounded by $cg(n)$ for some
constant $c$. The upper bound need not be exact, however, as we saw with
$h(n)$. We have a separate notation for that, the "big-Theta" notation:

$$\Theta(f) = \left\{\, g(n): \exists c_1,c_2\in\mathbb{R}^+, n_0\in\mathbb{N} : \forall n\in\mathbb{N} \geq n_0 : 0 \leq c_1 f(n) \leq g(n) \leq c_2 f(n)\,\right\}$$

The class of functions $\Theta(f)$ are those that, depending on which
constant you multiply them with, can be both upper- and lower-bounds of
$f(n)$ as $n$ goes to infinity. This notation *is* symmetric:
$g\in\Theta(f)$ if and only if $f\in\Theta(g)$. For our two lines,
$f(n) = 10n + 100$ and $g(n) = 3n + 100,000$, we have $f\in\Theta(g)$
and $g\in\Theta(f)$, and we can in good conscience write
$\Theta(f)=\Theta(g)$ as they are the same classes of functions. We can
also write $O(f(n))=O(g(n))=O(n)$ since these are also the same classes,
but $O(f)\neq O(h)$ because $O(h(n))=O(n^2)$ is a large class than
$O(n)$. There are functions that are bounded, up to a constant, by $n^2$
that are not bounded by $n$, regardless of which constant we multiply to
$n$.

The big-Oh notation can be thought of as saying something like "less
than or equal to". When we say that $g\in O(f)$ we are saying that $g$
doesn't grow faster than $f$, up to some constant and after a certain
$n_0$. Because the notation is concerned with what happens as $n$ goes
to infinity, it captures *asymptotic behaviour*. This is just a math
term for saying that we concern ourselves with what a function does as
it moves towards a limit, in this case, infinity. When we analyse
algorithms, we usually care more about how efficient they are on large
input data compared to how they behave on small input data, so we care
about their asymptotic efficiency more than we care about the details of
how they behave for small $n$.

Consider algorithms that use $n^2$ versus $10n + 100$ operations on
input of size $n$. For small $n$, the $n^2$ algorithm will use fewer
operations than the $10n + 100$ algorithm, but unless we expect that the
input size will always be small, the $10n + 100$ algorithm is superior.
As $n$ grows, it will eventually be *much* faster than the $n^2$
algorithm.

When we have an algorithm that uses $f(n)$ operations for input of size
$n$, and we know $f\in O(g)$, then we know that $g$ will eventually
bound the running time for the algorithm. We will say that "the
algorithm runs in time $O(g)$"---or usually qualify that we consider
worst-case complexity, say, by saying that "the algorithm runs in
worst-case time $O(g)$".

Consider the example from earlier where we added $n$ numbers together.
We counted that this involved $6n + 3$ primitive operations. If we pick
any constant $c>6$, then $cn$ will eventually be larger than $6n + 3$,
so we can say that the algorithm runs in time $O(n)$. The cost of each
individual operation will vary according to the actual hardware you will
execute the algorithm on, and it will not be the same cost for each
operation; knowing that the running time is linear, i.e., that the
algorithm runs in time $O(n)$, is much more important to know than what
the exact number of operations is. Therefore, we usually do not care
about the actual number of operations but only the big-Oh of them.

The big-Oh notation is the most used notation of the two. It is often
easier to show that an algorithm does not do more than a certain number
of operations, f(n) than to show that it doesn't do fewer. In many
cases, we can show that an algorithm's running time is in big-Theta,
$\Theta(f)$, which gives us more information about the actual running
time, but it can at times be harder to get such an exact function of its
running time. When we use big-Oh, it is not a problem to over-count how
many operations we actually use; when we use big-Theta, we have to get
it right.

### Other classes

In the vast majority of times when we use this asymptotic notation, we
use big-Oh. We often do that even when we know that an algorithm's
complexity accurately and could use big-Theta. This is just because we
usually care much more about bounding the running time of an algorithm
than we care about getting the running time precisely right. For
completeness, however, I will quickly define a few more classes, in case
you run into these outside of this book.

The big-Oh class of a function is all functions that work as upper
bounds of it. If $g\in O(f)$, then after some $n_0$ and for some
constant $c$, $g(n) \leq c f(n)$. If we can change the inequality sign
to be less, rather than less-than, we get a different class of
functions, called "little-oh":

$$o(f) = \left\{\, g(n): \exists c\in\mathbb{R}^+, n_0\in\mathbb{N} : \forall n\in\mathbb{N} \geq n_0 : 0 \leq g(n) < c f(n) \,\right\}$$

If $g\in o(f)$ then we know that $g\in O(f)$ as well but also that
$f\not\in O(g)$. Asymptotically, $f$ grows strictly faster than $g$.

We also have notation for lower bounds, similar to big-Oh and little-oh:
we have big-Omega and little-omega:

$$\Omega(f) = \left\{\, g(n): \exists c\in\mathbb{R}^+, n_0\in\mathbb{N} : \forall n\in\mathbb{N} \geq n_0 :
    0 \leq f(n) \leq c g(n) \,\right\}$$
$$\omega(f) = \left\{\, g(n): \exists c\in\mathbb{R}^+, n_0\in\mathbb{N} : \forall n\in\mathbb{N} \geq n_0 :
    0 \leq f(n) < c g(n) \,\right\}$$

These captures lower bounds, strict or otherwise. When $g\in\Theta(f)$
we have that, asymptotically, $f$ can dominate $g$ and $g$ can dominate
$f$; so saying $g\in\Theta(f)$ is equivalent to saying $g\in O(f)$ as
well as $g\in\Omega(f)$.

When we reason about the efficiency of an algorithm, we care about upper
bounds and use the oh-notation; if we instead worry about how
intrinsically complex problems are, we usually care about the lower
bounds for any algorithm that solves them will have to be, and use the
omega-notation. If we have a problem that we know requires $\Omega(f)$
to solve, but we also have an algorithm that solves it in $O(f)$, we
have a tight bound of $\Theta(f)$. We do not concern ourselves much with
the complexity of problems in this book, but it will come up from time
to time, so keep this in mind.

### Properties of complexity classes

These classes of functions have a few rules that are easy to derive that
can help us reason about them in general. As long as we do not use the
strict upper- and lower-bound classes, a function is going to be in its
own class:

$$f \in \Theta(f)$$ $$f \in O(f)$$ $$f \in \Omega(f)$$

There is a symmetry between upper- and lower bounds:

$$f\in O(g) \quad\text{ if and only if }\quad g\in\Omega(f)$$
$$f\in o(g) \quad\text{ if and only if }\quad g\in\omega(f)$$

Furthermore, there is transitivity in these senses:

$$f\in\Theta(g) \land g\in\Theta(h) \implies f\in\Theta(h)$$
$$f\in O(g) \land g\in O(h) \implies f\in O(h)$$
$$f\in\Omega(g) \land g\in\Omega(h) \implies f\in\Omega(h)$$
$$f\in o(g) \land g\in o(h) \implies f\in o(h)$$
$$f\in\omega(g) \land g\in\omega(h) \implies f\in\omega(h)$$

I have personally found very few opportunities where these rules have
been useful, but if you can see why the rules must be correct, you have
taken a significant step towards understanding this asymptotic function
notation.

One rule that can be very useful is this: if $f\in\Theta(g)$, i.e.,
there exists $c_1,c_2\in\mathbb{R}^+$ such that
$c_1g(n)\leq f(n)\leq c_2g(n)$ as $n$ goes to infinity, then we also
have

$$c_1 \leq \frac{f(n)}{g(n)} \leq c_2.$$

This means that if we believe that an algorithm runs in time
$f\in\Theta(g)$, we can experimentally measure its running time and
divided it by $g(n)$. If we are right about the running time should
eventually stay confined to the interval between these two constants. In
other words, $f(n)/g(n)$ should flatten out as $n$ goes to infinity; not
entirely, because it can fluctuate between $c_1$ and $c_2$, but it will
eventually be bounded by these two constants. In practice, the ratio
often does converge to a single constant non-zero. If we are wrong about
the complexity, this doesn't happen. If $f\in o(g)$, then the ratio will
converge to zero and not a positive constant, while if $f\in\omega(g)$,
the ratio will grow unbounded.

### Reasoning about algorithmic efficiency using the big-Oh notation

Here is how we would reason about an algorithm when using big-Oh
notation. Any sequence of primitive operations that we only do once is
$O(1)$. Regardless of what the actual cost of an operation is, say $c$,
it is still $O(1)$ because $O(1)=O(c)$ for all constants. It also
doesn't matter how many things we do, as long as we do them once,
because $O(1 + 1)=O(1)$. Whenever we loop over $n$ elements, that loop
costs us $O(n)$ operations. Any operation that happens inside the loop
body can be multiplied by $n$ to account for its cost. It doesn't matter
if we actually *do* execute that operation for each iteration; the
big-Oh notation gives us an upper bound for the running time, so if we
count an operation more often than we really should, that is okay.

In the summation algorithm, we therefore have:

``` {.python}
accumulator = 0       # O(1)
for n in numbers:     # O(n)
    accumulator += n  # n * O(1)
```

where $n \times O(1)$ should be read as $O(n)$---we are really saying
that we do something that has a constant cost, say $c$, but we do it $n$
times, so we do something that costs $cn$ which is in $O(n)$.

With the search algorithm, we can reason similarly and get:

``` {.python}
in_list = False           # O(1)
for n in numbers:         # O(n)
    if n == x:            # n * O(1)
        in_list = True    # n * O(1)
        break             # n * O(1)
```

We know that we only ever execute the body of the `if`-statement once,
but it is easier just to multiply all the operations inside the loop by
$n$, and since the big-Oh notation only guarantees us that we have an
upper bound, it works out okay.[^8]

To make the big-Oh reasoning about these algorithms even more relaxed,
we will work out how to add big-Oh expressions together.

### Doing arithmetic in big-Oh

When analysing algorithms like we just did, we often end up with
multiplying a function to a big-Oh class, as we did with $n\cdot O(1)$,
and if we want to combine a number of calculations where we know their
big-Oh class, we need to add them together, that is we want to know how
to interpret $O(f) + O(g)$.

First, we need to know how to do arithmetic on functions, but that is
probably familiar to you. If you have a function $f$ and multiply it
with a constant, $c$, you have $cf$ which is the function
$h(n)=c\cdot f(n)$. Similarly, $f+c$ is the function $h(n)=f(n) + c$. If
you have two functions, $f$ and $g$, then $f\cdot g$ is the function
$h(n)=f(n)g(n)$ and $f+g$ is the function $h(n)=f(n)+g(n)$. Do not
confuse function multiplication, $f\cdot g$, with function composition,
$f\cdot g$. The former means that $(f\cdot g)(n) = f(n)\cdot g(n)$,
while the latter means that $(f\cdot g)(n) = f(g(n))$.

For the rules for doing arithmetic with big-Oh notation let
$f$,f\_1,f\_2,g,g\_1,g\_2\$ denote functions.

The first important rule is this:

$$f_1\in O(g_1) \land f_2\in O(g_2) \implies f_1+f_2\in O(g_1+g_2)$$

We can also write this as:

$$O(f) + O(g) = O(f + g).$$

Since $g+g$ is the same as $2g$ we furthermore have that

$$f_1\in O(g) \land f_2\in O(g) \implies f_1+f_2\in O(g)$$

This means that if we can bound two separate pieces of the running time
of an algorithm by the same function, then the entire algorithm's
running time is bounded by that. Because of the transitivity rules for
big-Oh, this also means that if $f\in O(g)$ then $f+g\in O(g)$. So when
we add together different parts of a runtime analysis, whenever one
function dominates the other, we can simply discard the dominated part.
So, if we add a constant number of operations, $O(1)$, to a linear
number of operations, $O(n)$, as we have to in our examples, we end up
with something that is still linear $O(n)$.

We also have a rule for multiplying functions:

$$f_1\in O(g_1) \land f_2\in O(g_2) \implies f_1\cdot f_2\in O(g_1\cdot g_2)$$

or

$$O(f)\cdot O(g) = O(f\cdot g).$$

This rule is particularly useful when we reason about loops. The time it
takes to execute a loop over $n$ elements is $O(n)$ times the time it
takes to execute the loop body, which could be some function $f(n)$, so
the total running time for such a loop is $n\cdot f(n)\in O(n f(n))$.

We also have rules for multiplying into big-Oh classes:

$$f \cdot O(g) = O(f\cdot g)$$

We can use this in our examples where we have expressions such as
$n\times O(1)$. This simply becomes $O(n)$. From this rule, it follows
that when $c$ is a non-zero constant we have:

$$c \cdot O(f) = O(f)$$

You can see this by merely considering $c$ a constant function:
$c(n) = c$ and then apply the previous rule.

We can now apply these rules to get a final, big-Oh, running time for
our example algorithms. Consider first the summation:

``` {.python}
accumulator = 0       # O(1)
for n in numbers:     # O(n)
    accumulator += n  # n * O(1)
```

We have to work out $O(1) + O(n) + n\cdot O(1)$. This is the same as
$O(1) + O(n) + O(n)$ by the rule for how to multiply into a big-Oh
class, and then, by the addition rule, we get $O(1 + n + n)=O(n)$.

For the search we have

``` {.python}
in_list = False           # O(1)
for n in numbers:         # O(n)
    if n == x:            # n * O(1)
        in_list = True    # n * O(1)
        break             # n * O(1)
```

which breaks down to $O(1) + O(n) + 3\times n\times O(1) = O(n)$.

Consider now a different algorithm:

``` {.python}
for i in range(1,len(numbers)):
    x = numbers[i]
    j = i
    while j > 0 and numbers[j-1] > numbers[j]:
        numbers[j-1], numbers[j] = numbers[j], numbers[j-1]
        j -= 1
```

This is an algorithm called "insertion sort", and we return to it in the
next chapter where we prove that it sorts `numbers`. Here, we will just
consider its running time. The algorithm consists of two nested loops.
So we reason as follows: the outer loop iterates over `numbers`, which
gives us an $O(n)$ contribution. It doesn't include the first element in
`numbers`, but that doesn't change anything since $O(n-1)=O(n)$. Inside
the loop body, we have two constant time contributions and an inner
loop. The constant contributions give us $O(1)$ and the inner loop is
bounded by $O(n)$ ($j$ starts at a number less than $n$ and is decreased
by at least one in each iteration and leave the look if it reaches
zero). So we have the running time

$$O\left(n\right)\times\left(O\left(1\right)+O\left(n\right)\right)=O\left(n^2\right).$$

In other words, this sorting algorithm runs in quadratic time. Or
rather, we should say that its *worst-case* running time is
$O\left(n^2\right)$. In the analysis, we assumed that the inner loop
could execute $n$ iterations; if the list is already sorted, then
`numbers[j-1] > numbers[j]` is always `False`, and the inner loop will
actually take constant time. So the *best-case* running time is only
$O(n)$.

Now consider this algorithm, called *binary search*. This is another
algorithm we return to in the next chapter. It searches for a number,
$x$, in a sorted list of numbers using the third strategy from the
guessing game we have seen a few times by now. It has a range in which
to search, bracketed by `low` and `high`. If $x$ is in the list, we know
that it must be between these two indices. We pick the midpoint of the
range and check if we have found $x$, in which case we terminate the
search. If we haven't, we check if the midpoint number is smaller or
larger than $x$. If it is smaller, we move `low` up to the midpoint plus
one. If it is larger, we move `high` down to the midpoint. We do not
move it to the midpoint minus one. If we did, it is possible to miss the
index where $x$ is hiding; this can happen if the interval is of length
one and `low` is the index where $x$ resides, as we will see next
chapter.

``` {.python}
low, high = 0, len(numbers)
found = False
while low < high:
    mid = (low + high) // 2
    if numbers[mid] == x:
        found = True
        break
    elif numbers[mid] < x:
        low = mid + 1
    else:
        high = mid
```

We can analyse its complexity as follows: we have some constant time
operations at the beginning, $O(1)$, and then a loop. It is less obvious
how many iterations the loop will make in this algorithm than in the
previous ones we have looked at, but let us call that number $m$. Then
the loop takes time $O(m)$ times the time it takes to execute the loop
body. All the operations inside the loop are constant time, $O(1)$, so
we have

$$O\left(1\right)+O\left(m\right)\times O\left(1\right)=O\left(m\right).$$

Of course, this isn't entirely satisfying. We don't know what $m$ is,
and we want the running time to be a function of $n$.

The interval we are searching in decreases in each iteration, so if we
start with an interval of size $n$ we could, correctly, argue that the
loop is bounded by $n$ as well, and derive a running time of $O(n)$.
This is correct; $O(n)$ is an upper bound for the (worst-case)
complexity. In fact, however, the algorithm is much faster than that. It
actually runs in $O(\log_2 n)$, where $\log_2$ is the base-two
logarithm. To see this, consider how much we shrink the interval by in
each iteration. When we update the interval, we always shrink the
interval to half the size of the previous one. So we can ask ourselves,
how many times can you halve $n$ before you get below one? That is
$\lceil\log_2 n\rceil$, so $m$ is bounded by $O(\lceil\log_2 n\rceil)$.
We typically do not include the rounding-up notation when we write this
but consider it implicit, so we simply write $O(\log_2 n)$.

### Important complexity classes

Some complexity classes pop up again and again in algorithms, so you
should get familiar with them. From fastest to slowest, these are:

-   Constant time: $O(1)$. This is, obviously, the best you can achieve
    asymptotically, but since it does not depend on the input size, we
    very rarely see algorithms running in this time.
-   Logarithmic time: $O(\log n)$. We saw that binary search was one
    such algorithm. Generally, we see this complexity when we can reduce
    the size of the input we look at by a fixed fraction in each
    iteration of a loop. Typically, we can cut the data in half, and we
    get a base-two logarithm, but since the difference between two
    different-based logarithms is a constant,
    $\log_a(x)=1/\log_b(a)\cdot\log_b(x)$, we rarely write the base in
    big-Oh notation.
-   Linear time: $O(n)$. We saw several examples of linear time
    algorithms in this chapter. Whenever we do something where we have
    to, in the worst case, examine all our input, the complexity will be
    at least this.
-   Log-linear time: $O(n\log n)$. We haven't seen examples of this
    class yet, but it will show up several times in [Chapter
    @sec:divide-and-conquer].
-   Quadratic time: $O(n^2)$. We saw that bubble sort had this
    complexity. This complexity often shows up when we have nested
    loops.
-   Cubic time: $O(n^3)$. This is another class we haven't seen yet, but
    when we have three levels of nested loops, we see it. If you
    multiply two $n\times n$ algorithms the straightforward way,[^9]
    $C=AB$, you have to compute $n\times n$ values in $C$, and for each
    compute $c_{ij} = \sum_k a_{ik}b_{kj}$ where you add $n$ values,
    giving you a total running time of $n^3$.
-   Exponential time: $O(2^n)$. You should avoid this complexity like
    the plague. Even for tiny $n$, this running time is practically
    forever. It does, unfortunately, pop up in many important
    optimisation problems where we do not know of any faster algorithms.
    If you have a problem that can only be solved in this complexity,
    you should try to modify the problem to something you can solve more
    efficiently, or you should try to approximate the solution instead
    of getting the optimal solution. Algorithms that run in this
    complexity are rarely worth considering.

In [@fig:function-growth] I have plotted the growth of the different
classes. As you can see in the upper-left frame, logarithmic growth is
very slow compared to linear growth. On the upper-right, you can see
that log-linear growth is slower than linear, but compared to quadratic
time, it is much faster. Cubic time, lower-left, is much slower than
quadratic time, and exponential time, lower-right, just grows to
infinity before you even get started.

![Growth of different complexity
classes.](function-growth.pdf){#fig:function-growth}

### Asymptotic complexity exercises

In the following exercises, you can test your understanding of the
big-Oh notation and in how you derive upper bounds for algorithm's
running time.

#### Function growth

Consider the classes

1.  $O(\log n)$, $o(\log n)$, $\Omega(\log n)$ and $\omega(\log n)$
2.  $O(n)$, $o(n)$, $\Omega(n)$, and $\omega(n)$
3.  $O(n^2)$, $o(n^2)$, $\Omega(n^2)$, and $\omega(n^2)$
4.  $O(2^n)$, $o(2^n)$, $\Omega(2^n)$, and $\omega(2^n)$

**Exercise:** For each of the functions below, determine which of the 16
classes it belongs in. Remember that the complexity classes overlap, so
for example, if $f\in o(g)$ then $f\in O(g)$ as well, and if
$f\in\Theta(g)$ then $f\in O(g)$ as well as $\Omega(g)$ (but
$f\not\in o(g)$ and $f\not\in\omega(g)$).

1.  $f(n) = 23n$
2.  $f(n) = 42n^2 - 100n$
3.  $f(n) = n/\log n$
4.  $f(n) = \log(n)/n$
5.  $f(n) = n^2/\log n$
6.  $f(n) = \log n + \log(n)/n$
7.  $f(n) = 5^n - n^3$
8.  $f(n) = n!$
9.  $f(n) = 2^n/n$
10. $f(n) = \log\left(\log n\right)$

#### Insertion sort

Consider the insertion sort algorithm. We argued that the worst-case
running time was $O\left(n^2\right)$ but the best-case running time was
$O\left(n\right)$.

**Exercise:** Describe what the input data, `numbers`, should look like
to actually achieve the worst- and best-case running times.

### Binary search

We argued that the worst-case running time for the binary search is
$O\left(\log n\right)$.

**Exercise:** What is the best-case running time, and what would the
input data look like to achieve it?

### Sieve of Eratosthenes

Recall the Sieve of Eratosthenes from the previous chapter.

**Exercise:** Derive an upper bound for its running time.

**Exercise:** Is there a difference between its best-case and worst-case
running time?

### Longest increasing substring

Recall the exercise from the previous chapter where you should design an
algorithm that finds the longest sub-sequence `x[i:j]` such that
consecutive numbers are increasing, i.e. `x[k] < x[k+1]` for all `k` in
`range(i,j)` (or one of the longest, if there are more than one with the
same length).

**Exercise:** What is the time complexity of your solution?

**Exercise:** Can you construct a linear-time algorithm for solving this
problem?

*Hint:* One way to approach this is to consider the longest sequence
seen so far and the longest sequence up to a given index into `x`. From
this, you can formalise invariants that should get you through.

### Merging

Recall the *merging* algorithm from the previous chapter.

**Exercise:** Show that you can merge two sorted lists of size $n$ and
$m$, respectively, into one sorted list containing the elements from the
two, in time $O(n+m)$.

Reduction from one problem to another
-------------------------------------

Searching and sorting {#sec:searching-and-sorting}
=====================

In this chapter, we will explore two fundamental problems that are the
foundations of many other algorithms: sorting sequences and searching
for an element in them. These are central problems used as building
blocks for many different algorithms, and Python already has built-in
functionality for solving them. You should practically always use the
existing implementations; they are well engineered and optimised, so you
are not likely to implement faster solutions. The exception is when
there are you have some a priori knowledge about your data that Python
does not have that you can exploit it while Python must use a general
algorithm. Different algorithms have different pros and cons, and we
will briefly discuss these. You can choose the right algorithm for the
job because you know more about the data than Python does. Optimising
the algorithm you use this way is rarely worthwhile, though, so you are
usually better off just using what Python already has. Anyway, onward to
the algorithms.

Searching
---------

We first consider the simplest of the two problems: searching. Given a
sequence of numbers,[^10] `numbers`, and a value, `x`, we want to
determine if `x` is in `numbers`. We consider two solutions to this
problem. The first, *linear search*, assumes nothing about `numbers`
except that it is a sequence we can loop through. The second, *binary
search* makes a few more assumptions: 1) `numbers` is a sorted sequence
and 2) we can access any element in `numbers` by index, `numbers[i]` in
constant time.[^11]

The linear search algorithm runs in worst-case linear time, thus the
name. Binary search only takes logarithmic time. This makes the binary
search algorithm the preferred choice whenever your data is sorted. If
the data is not sorted to begin with, however, the cost of sorting the
data before you can use binary search should also be taken into account.
If you search for $m$ elements in a sequence of $n$ numbers, the linear
search will take time $O(mn)$ while binary search will take time
$O(S(n)+m\log n)$ where $S(n)$ is the cost of sorting $n$ numbers.

How fast we can sort data depends on the assumptions we can make about
our data items. If all we can do with data objects is to compare them to
learn which is smaller than the other, then it can be shown that the
sorting problem cannot be solved faster than $\Omega(n\log n)$.
Algorithms that only assume that we can compare objects are called
*comparison-based* sorting algorithms. Not that inventive, I know. We
shall see comparison-based algorithms that run in time $O(n\log n)$ in
[Chapter @sec:divide-and-conquer] and [Chapter @sec:return-to-sorting].
In this chapter, we will only see comparison-based sorting algorithms
that run in worst-case time $O(n^2)$. We will also see algorithms that
run in linear time. This doesn't conflict with the lower bound of
$\Omega(n\log n)$ for comparison-based algorithms because our linear
time algorithms will depend on more than simple comparison; with more
assumptions about what we can do with our data, we have more to exploit
when building algorithms to solve a problem.

### Linear search

Linear search is straightforward. We loop over all the elements in
`numbers` and compare each in turn to `x`. If we see `x`, we break the
search and report that we found it. If we reach the end of `numbers`
without having seen `x`, we report that it wasn't found.

``` {.python}
found = False
for n in numbers:
    if x == n:
        found = True
        break
```

The built-in solution in Python for linear search uses the `in`
keyword:[^12]

``` {.python}
x in numbers
```

That the linear search algorithm has a worst-case running time of $O(n)$
is also straightforward. The `for`-loop has to run over all the $n$
elements in `numbers` if it doesn't find $x$ and breaks early. The
best-case running time is obviously $O(1)$ because we could get lucky
and find $x$ in the very first iteration.

### Binary search

If we assume we have random-access sorted input, we can do better than a
linear search, we can do a binary search. We already saw the binary
search algorithm in the previous chapter. It looks like this:

``` {.python}
low, high = 0, len(numbers)
found = None
while low < high:
    mid = (low + high) // 2
    if numbers[mid] == x:
        found = mid
        break
    elif numbers[mid] < x:
        low = mid + 1
    else:
        high = mid
```

The algorithm works by keeping track of an interval, `[low,high)`. The
algorithm makes sure that if `x` is found in `numbers`, it is found in
this range. In each iteration of the `while`-loop we look at the
mid-point of the range (if the midpoint is not an integer, we round down
when we do integer division). If the midpoint is equal to $x$, we are
done. If it is less than $x$, we know that $x$ must be found in the
interval `[mid+1,high)`. The elements are sorted, so if the midpoint is
less than $x$, then all elements to the left of the midpoint are less
than $x$ as well. If the midpoint is greater than $x$, then we know that
all elements to the right of the midpoint are greater than $x$ as well,
so if $x$ is in the list, then it must be in the interval $[low,mid)$.
Notice the asymmetry in the updated intervals.[^13] When we increase
`low`, we use `mid+1`, but when we decrease `high`, we use `mid`. This
is a consequence of how we generally represent ranges in Python. We
include the point at `low` in the range but exclude point at `high`. So,
when we decrease `high` to `mid`, we have already eliminated the point
at `mid` from the search, just as when we increase `low` to `mid + 1`.

**Exercise:** Consider a modified solution where we set `high` to
`mid-1` instead of `mid`. Give an example where the algorithm would give
you the wrong answer.

The built-in solution in Python is implemented in the module `bisect`
and looks like this:

``` {.python}
import bisect
print(bisect.bisect(numbers, x))
```

The `bisect` algorithm does something *slightly* different from our
implementation. It returns an index where `x` is found, or if `x` is not
in `numbers`, it returns the index at which it should be inserted if we
wanted to do that. We just consider the simpler problem of determining
if `x` is in the sequence or not.

The `numbers` sequence has to be sorted for the algorithm to work. It is
this property that gives us information about where to continue the
search if the midpoint of the interval is smaller or larger than $x$. If
the list were not sorted, knowing whether the midpoint is smaller than
or larger than $x$ would give us no information about where $x$ would be
found if it were in the list.

To hone our skills at reasoning about algorithms, we will formally prove
termination and correctness. We look at termination first. For our
termination function, we take `high-low`. Clearly, if this function is
at or below zero, the `while`-loop condition is false. To see that it
decreases in each iteration, we consider the two options for updating
the interval. If we set `low` to `mid + 1`, we clearly reduce
`high-low`. To see that we also decrease the size of the interval when
we update `high`, we observe that `mid < high` when we use
integer-division for determining `mid`.

**Exercise:** If we updated `low` by setting it to `mid` instead of
`mid + 1`, our reasoning about the termination function fails. Give an
example where this would result in the loop never terminating.

To prove correctness, we specify the loop-invariant: `x` is not in the
interval `[0,low)` and not in the interval `[high,n)`. This invariant
guarantees us that if we reach the point where the `[low,high)` interval
is empty, then `x` was not in `numbers`. Since we do not set `found` to
true unless we actually see $x$, we also know that we do not report that
$x$ *is* in `numbers` unless it is.

We already discussed the algorithms running time in the previous
chapter, but recall: if we reduce the size of a problem from $n$ to
$n/2$ in each iteration and only use $O(1)$ per iteration, then the
running time amounts to the number of times we can divide $n$ by two
until we reach one (or below). That is the base-two logarithm of $n$, so
the worst-case running time of binary search is $O(n \log n)$.

Sorting
-------

The sorting problem is this: given a sequence of elements $x$ of length
$n$, create a new sequence $y$ that contain the same element as $x$ but
such that $y[i]\leq y[i+1]$ for $i=0,\ldots,n-1$. For this problem to
even make sense we must make clear what we mean by $y[i]\leq y[i+1]$.
Not all data has a natural order of elements. For some data, there is no
natural way to define an order. For other data, it is possible to have a
*partial order*, which means that for *some* elements $a$ and $b$ we can
determine if $a=b$, $a<b$ or $a>b$, but not all; some elements $a\neq b$
are *neither* $a<b$ nor $a>b$. In such a case, we might require of $y$
that $y[i]\not\geq y[i+1]$. This is known as *topological sorting*. We
return to this in [@sec:toplogical-sorting]. In this chapter, we only
consider data that has a total order.

In this chapter, we assume that our elements have a *total order*, which
means that for any two elements, $a$\~ and \~$b$, (exactly) one of these
three relations are true: $a<b$, $a=b$, or $a>b$. This is, for example,
the case for numbers, with the usual order, but also for strings with
the alphabetical order, also known as the *lexical* order, of strings.

Even if we have managed to define a total order on our data points, we
are not out of the woods yet. The total order only means that we have
well-defined comparison relations, $a=b$, $a<b$, and $b>a$, where for
any given elements $a$ and $b$ exactly one is true. But what *exactly*
can we assume about $a$ and $b$ when we write $a=b$? Using the relation
"$=$" to mean (object) equality is simple. If $a=b$, then we know that
$a$ and $b$ are the same object. This isn't the only way we use
equality, though. Sometimes it is used to define an equivalence relation
instead of actual equality. This happens when we sort elements according
to some key or keys, and the order is defined by these keys. If the keys
are only part of the data, we can have two elements that have the same
values for all keys (so we would conclude $a=b$), but they are actually
different objects with different non-key attributes.

If we sort a list of people by their last name, then we consider "John
Doe" and "Jane Doe" as equal with relation to the order---after all
"Doe" equals "Doe"---but that does not mean that "John" equals "Jane".
We can resolve this by first sorting by the last name and then according
to the first name, but this creates a new problem. If we first sort by
the last name and then according to the first name, do we risk of
messing up the first order. If we sort

-   "John Doe"
-   "John Smith"
-   "Jane Doe"

by the last name, we get the order

-   "John Doe"
-   "Jane Doe"
-   "Joe Smith"

(or maybe we get "Jane Doe", "John Doe", and "Joe Smith" since "Jane
Doe" and "John Doe" are equal concerning last names). If we then sort by
the first name, we mess up the first sort, because now we might get
"Jane Doe", "Joe Smith", and "John Doe".

When we only sort elements based some sub-set of their attributes, what
we call *keys*, an algorithm can be *stable* or *unstable*. If it is
stable, it means that elements we consider equal end up in the same
order as they appear in the input; if it is unstable, there is no such
guarantee. To correctly sort names, first by family name and then
according to Christian name, we can first sort by Christian name and
then use a stable sort on the family name. If we sort our list with the
first names as keys we get

-   "Jane Doe"
-   "Joe Smith"
-   "John Doe"

If we then sort with a stable sort, using the family names as the key,
"Jane Doe" must appear before "John Doe" because that is the order they
are in when we apply the stable sort.

We also classify sorting algorithms by whether they are
*comparison-based* or not. If all we can do, when we have two elements,
is to test which of the relations, $a<b$, $a=b$, and $a>b$ are true,
then we are doing what is called *comparison* sort. As I mentioned at
the start of this chapter, no comparison-based algorithm can sort $n$
elements faster than $\Omega(n \log n)$, and some algorithms do run in
$\Theta(n\log n)$, although we won't see them in this chapter. Sorting
algorithms do not have to be comparison-based, though. We will see two
such algorithms in this chapter that can sort in worst-case linear time,
as long as we can reduce our keys to numbers bounded by $n$.

Another property we use to classify sorting algorithms is whether they
sort the elements *in-place* or not. If we sort in-place, it means that
we swap around the items in our input sequence to turn it into a sorted
sequence without using any additional memory. In the previous chapter,
we focused on running time complexity, but how much memory an algorithm
needs can be equally important. An in-place algorithm has optimal memory
usage, $O(1)$.[^14] Just as we didn't include the input size for the
time-usage of the binary search algorithm, we do not include the input
size as part of sorting algorithm's memory usage. When algorithms are
not in-place, i.e., when they use more than constant memory, their
memory consumption is often equally important to their time usage.

For implementations of sorting algorithms, we also distinguish between
them being *destructive* or *non-destructive*. If you modify the input
sequence when you sort it, you destroy the original order you got the
data in. Sometimes, this is what you want. You only care about the
sorted version of your data, so the original order is irrelevant. Other
times, you want to keep the original order around, for some reason or
other, and just want a sorted copy around as well. This is not so much a
property of algorithms as it is for implementations. You can copy the
input data and then use a destructive algorithm to sort it, thus
preserving the original sequence. The only consequence of making a
non-destructive sort out of a destructive one is the memory usage. You
can take the memory usage of any sorting algorithm, make it at least
linear and then you can sort non-destructively in that complexity.
In-place algorithms use constant space but are by nature destructive; if
you first create a copy of the input and sort that destructively, you
now have a linear space implementation.

There are more properties used to classify sorting algorithms than
these, but they are the main ones. To summarise, the classifications we
have seen are:

-   **comparison based**: All we can do with our data items is to
    compare pairs ($a,b$) to determine whether $a<b$, $a=b$, or $a>b$.

-   **stable**: When we sort data items by some key, we do not change
    the order of the input items that have the same key.

-   **in-place**: When we only use constant extra memory to sort a
    sequence.

-   **destructive** (For implementations): Whether sorting a sequence
    modifies it or whether we create a copy of the data in sorted order.

In this chapter, we will see three algorithms that are comparison-based
algorithms and two that are not, four that are stable and one that is
not, and three that are in-place and two that are not:

  Algorithm    Comparison based      Stable        In-place
  ----------- ------------------ -------------- --------------
  Insertion      $\checkmark$     $\checkmark$   $\checkmark$
  Bubble         $\checkmark$     $\checkmark$   $\checkmark$
  Selection      $\checkmark$                    $\checkmark$
  Bucket                          $\checkmark$  
  Radix                           $\checkmark$  

You can implement all of them both as destructive and non-destructive.
For the in-place algorithms this changes the memory complexity from
constant to linear; for the bucket- and radix-sort, it does not alter
the space complexity.

### Built-in sorting in Python

Python lists have a builtin sorting method

``` {.python}
x.sort()
```

using an algorithm known as *Timsort* (named after Tim Peters who
created it). This is a comparison based stable sorting algorithm that
runs in worst-case time $O(n\log n)$ and best-case time $O(n)$ with
$O(n)$ memory usage.[^15]

Calling `x.sort()` is destructive; modifies `x` so the object is in
sorted order after the call. Python also provides a non-destructive way
to get a sorted copy:

``` {.python}
y = sorted(x)
```

This uses the same Timsort algorithm as `x.sort()`; it just doesn't
modify `x` but creates a new copy.

### Comparison sorts

We've seen enough algorithm classification terms now to satisfy even the
most pedantic programmer, so we now turn to actual algorithms. We first
consider three comparison-based, in-place sorting algorithms. Two of
them, *insertion sort* and *bubble sort* are stable and have a best-case
running time of $O(n)$. The third, *selection sort*, is not stable and
has a best-case running time of $O(n^2)$.

#### Selection sort

A straightforward comparison sort algorithm is *selection sort*. It
works similar to how you might sort items by hand. You keep a list of
sorted items and a set of yet-to-be-sorted items. One by one, you pick
the smallest of the unsorted elements and append it to the list of
sorted elements. Selection sort follows this strategy but keeps the list
of sorted and the list of unsorted elements in the same list as the
input, making it an in-place algorithm. It uses a variable, $i$, that
iterates from zero to $n-1$, where $n$ is the length of the input list.
The items below $i$ are kept sorted and are less than or equal to the
items above $i$. Formalised as a loop invariant, we can write this as

$$I_1: \forall j\in[0,i) : x[j-1] \leq x[j]$$

and

$$I_2: \forall j\in[0,i), \forall k\in[i,n) : x[j] \leq x[k]$$

where $x$ is the sequence to be sorted.

If $i$ iterates from $0$ to $n-1$, then in the last iteration, when $i$
is incremented form $n-1$ to $n$, invariant $I_1$ guarantees us that all
elements in the range $[0,n)$ are sorted, so the loop invariant
guarantees correctness. (We still have to guarantee that we satisfy the
invariant in each iteration over variable $i$, of course). The algorithm
will consist of two loops, one nested inside the other, but both will be
`for`-loops, iterating through finite length sequences, so termination
is also guaranteed.

In each iteration, we locate the index of the smallest element in the
range $[i,n)$\~, call it ~$j$~, and we swap \~$x[i]$ and $x[j]$, see
[@fig:selection-sort-swap]. From invariant $I_2$ we know that the $x[j]$
we locate is greater than or equal to all elements in the range $[0,i)$,
so when we put it at index $i$, the range $[0,i+1)$ is sorted,
satisfying $I_1$. Since $x[j]$ was the smallest element in the range
$[i,n)$\~, we also know that for all
\~$\ell \in [i,n): x[j] \leq x[\ell]$, so after we swap $x[i]$ and
$x[j]$---we can call the resulting list $x^\prime$---we have
$\ell \in [i+1,n) : x^\prime[i]=x[j]\leq x[\ell]$, satisfying $I_2$.
Thus, swapping the smallest element in $[i,n)$\~ into position \~$x[i]$
and incrementing $i$ each iteration satisfy the loop invariants, so the
algorithm is correct.

![Swapping the $j$'th and $i$'th item in selection
sort.](selection-sort-swap.pdf){#fig:selection-sort-swap}

Implemented in Python, the algorithm looks as follows:

    for i in range(len(x)):
        # find index of smallest elm in x[i:]
        min_idx, min_val = i, x[i]
        for j in range(i, len(x)):
            if x[j] < min_val:
                min_idx, min_val = j, x[j]
                
        # swap x[i] and x[j] puts
        # x[j] at the right position
        x[i], x[min_idx] = min_val, x[i]

If we start with this input sequence

``` {.python}
x = [1, 3, 2, 4, 5, 2, 3, 4, 1, 2, 3]
```

the states in the algorithm are given by these lists

``` {.python}
[1] [3, 2, 4, 5, 2, 3, 4, 1, 2, 3]
[1, 1] [2, 4, 5, 2, 3, 4, 3, 2, 3]
[1, 1, 2] [4, 5, 2, 3, 4, 3, 2, 3]
[1, 1, 2, 2] [5, 4, 3, 4, 3, 2, 3]
[1, 1, 2, 2, 2] [4, 3, 4, 3, 5, 3]
[1, 1, 2, 2, 2, 3] [4, 4, 3, 5, 3]
[1, 1, 2, 2, 2, 3, 3] [4, 4, 5, 3]
[1, 1, 2, 2, 2, 3, 3, 3] [4, 5, 4]
[1, 1, 2, 2, 2, 3, 3, 3, 4] [5, 4]
[1, 1, 2, 2, 2, 3, 3, 3, 4, 4] [5]
[1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5] []
```

as they look at the end of each outer `for`-loop body, where the first
list shows the elements in the range $[0,i+1)$ and the second list the
elements in the range $[i+1,n)$---before the loop body, we have $[0,i)$
sorted but at the end of the body we have $[0,i+1)$ sorted, which is
what I show here.

In each iteration, we locate the smallest element amongst those not yet
sorted and append it to the sorted list. If we always picked the
left-most minimal value when there were ties, it seems like the
algorithm should be stable, i.e. that the input order is preserved when
elements have the same key. This reasoning is faulty, however, since it
does not take into account exactly *how* we append a minimal value to
the sorted list. The swap we use to move the element at index $j$ into
index $i$ also moves the element at index $i$ over to index $j$. If
there is another index, $k<j$, where the key of $x[k]$ is the same as
the key of $x[i]$, then the swap of $x[i]$ and $x[j]$ has changed the
order of $x[i]$ and $x[k]$ as well, which a stable algorithm shouldn't
do.

**Exercise:** Give an example input where selection sort is not stable.

It *is* possible to make the algorithm stable, but not by swapping as we
do here. For that, we need a data structure where we can move an element
from one location to another in constant time. The linked lists we see
in [@sec:linked-lists] permits this, and there, we will revisit
selection sort.

To derive the running time of the algorithm, we see that the outer loop
execute $n-1$ operation and the inner loop executes $n-i$ iterations in
iteration $i$ of the outer loop, which gives us
$n + (n-1) + (n-2) + \cdots +1 = \sum_{i=1}^n i = \frac{1}{2}n(n+1) = \frac{1}{2}n^2 + \frac{1}{2}n \in O(n^2)$.
The running time does not depend on the actual input, only on the size,
so this running time is also the best case running time.

#### Insertion sort

The *insertion sort* algorithm is superficially similar to selection
sort. It is an in-place sorting algorithm where we keep the first part
of the input array sorted. We iterate from the beginning of the input to
the end and in each iteration we move one element from the unsorted part
to the sorted. We can implement it as follows:

``` {.python}
for i in range(1,len(x)):
    j = i
    while j > 0 and x[j-1] > x[j]:
        x[j-1], x[j] = x[j], x[j-1]
        j -= 1      
```

Just as for selection sort, in iteration $i$, we have the loop
invariant:

$$I: \forall j\in[0,i) : x[j-1] \leq x[j]$$

As we also observed for selection sort, this invariant guarantees us
that when we reach $i=n$, and the algorithm terminates, all the elements
in $x$ are sorted. Unlike selection sort, however, we do not guarantee
that the elements to the left of index $i$ are smaller than or equal to
the elements to the right of index $i$, the $I_2$ invariant for
selection sort. And we do not search for the smallest element in the
unsorted part of $x$ in each iteration, but instead, we move $x[i]$ to
the left until we find its proper location in the range $[0,i+1)$.

When we consider $x[i]$ in iteration $i$, the elements to the left of
$i$ are sorted. This means that we can split this first part of $x$ into
three contiguous regions (all three can potentially be empty). The first
region of $x$ contains elements with keys less than $x[i]$, the second
region contains elements with keys equal to $x[i]$, and the third region
contains elements with keys larger than $x[i]$, see
[@fig:insertion-sort-swap]. The inner loop in the insertion sort
algorithm moves $x[i]$ to the left until it reaches the first index with
a key that is equal to or less than $x[i]$. This move is made through
swapping, so a side effect of moving $x[i]$ to the left is that all the
elements in the sorted part of $x$ that are larger than $x[i]$ will be
moved one position to the right.

![Moving the i'th element to its correct location by swapping it towards
the left in insertion
sort.](insertion-sort-swap.pdf){#fig:insertion-sort-swap}

To see that the invariant $I_1$ is satisfied after each such move (if it
was satisfied before the inner loop), consider the three blocks in
[@fig:insertion-sort-swap]. The invariant guarantees us that the two
grey segments of $x$ are sorted, so when we extend the region where all
keys are the same as $x[i]$'s by one, we still have a sorted list.

To see that the algorithm terminates, we first observe that the outer
loop is a `for`-loop through $n-1$ elements, so this is guaranteed to
terminate if the inner loop does. For the inner loop, we condition that
$j>0$ and we decrease $j$ by one each iteration so we can use $j$ as a
termination function. The inner loop might not actually reach $j=0$
because we also condition on $x[j-1] > x[j]$, but using this termination
function, we are guaranteed that the inner loop terminates.

For the running time, we can do an analysis similar to selection sort.
We iteration $n-1$ times in the outer loop and the inner loop is bounded
by $i$ in iteration $i$, so we have the worst-case upper bound
$1+2+3+\cdots+(n-2)+(n-1) = \frac{1}{2}(n-1)n\in O(n^2)$. In the best
case, however, we only ever test the inner loop condition once, so the
best-case time usage is only $O(n)$, unlike selection sort where the
best-case is also $O(n^2)$.

**Exercise:** Describe what the input list should look like to achieve
best-case and worst-case time performance, respectively.

Now, since selection sort and insertion sort both have the same
worst-case running time, but insertion sort has a better best-case
running time---and would be expected to perform better every time we
have runs of consecutive, non-decreasing elements in the input---we
could argue that insertion sort is always the better choice. If the
elements are as simple as single computer words, so swapping items cost
no more than decreasing a counter, this would be true. The items in the
input list *could*, however, be more complex, and swapping could,
therefore, be a more expensive operation. If that is the case, we should
also take into consideration the cost that swapping incurs; instead of
merely counting operations, we should distinguish between comparison
operations and swap operations.

Selection sort, as we have implemented it, swaps $O(n)$ elements on all
input. We could avoid this by not moving the smallest item in the
unsorted sequence to a temporary variable and only swap $x[i]$ and
$x[j]$ when $x[j] < x[j]$.

``` {.python}
        if x[i] > min_val:
            x[i], x[min_idx] = min_val, x[i]
```

In that case, selection sort will have a best-case swap-count of zero,
which happens when the input list is already sorted. So selection sort
has a swap-complexity of worst-case $O(n)$ and best-case $O(1)$.

The worst-case swap count for insertion sort is obviously $O(n^2)$. If
we consider how elements are swapped more carefully, we will see that
each object is either always swapped upwards or always swapped downwards
until it finds its final position. No object will be swapped both up and
down in the algorithm. This means that an element that starts at index
$i$ and ends at index $k$ has been swapped $|i-k|$ times. If the input
list is already sorted, we swap zero elements. So the insertion sort has
a swap-complexity of worst-case $O(n^2)$ and best-case $O(1)$.

The best-case scenario is better for insertion sort than selection sort
since both algorithms would perform zero swaps but the selection sort
will do $O(n^2)$ comparisons while insertion sort will do only $O(n)$.
The worst-case performance is better for selection sort. Selection sort
will make $O(n^2)$ comparisons and $O(n)$ swaps, worst-case, while
insertion sort will do $O(n^2)$ comparisons and $O(n^2)$ swaps.

  --------------------------------------------------------------------------
  Algorithm      Comparisons    Comparisons    Swaps          Swaps
                 worst-case     best-case      worst-case     best-case
  -------------- -------------- -------------- -------------- --------------
  Selection      $O(n^2)$       $O(n^2)$       $O(n)$         $O(1)$

  Insertion      $O(n^2)$       $O(n)$         $O(n^2)$       $O(1)$
  --------------------------------------------------------------------------

Of course, if we need the sort to be stable, the selection sort we have
seen here cannot be used.

#### Bubble sort

The *bubble sort* algorithm is a stable in-place algorithm sort that
runs in the same complexity as insertion sort: worst-case $O(n^2)$ and
best-case $O(n)$, and will always do the same number of swaps for any
given input as insertion sort. It usually requires more comparisons,
though, so you should never prefer bubble sort over insertion sort. I
present the algorithm here only because it is a classical algorithm and
because it solves the sorting problem in a different way than the other
two.[^16] If the choice is between insertion sort and bubble sort,
insertion sort is always better. This doesn't mean that we cannot learn
something from considering the algorithm, to hone our computational
thinking skills; figuring out *why* bubble sort is a worse choice than
insertion sort will also teach us something.

Now, bubble sort is unlike the previous two algorithm in that it does
not keep the first part of the input list sorted. Instead, it runs
through the list repeatedly, swapping pairs that are in the wrong order,
like this:

``` {.python}
while True:
    swapped = False
    for i in range(1,len(x)):
        if x[i-1] > x[i]:
            x[i-1], x[i] = x[i], x[i-1]
            swapped = True

    if not swapped:
        break
```

When no pairs are swapped, it is because the inner loop managed to get
through the entire list without finding any keys out of order, so the
list must be sorted. We keep track of when this happens using the
variable `swapped`.

To prove that this algorithm is correct and terminates, we are going to
add an imaginary variable, $j$. It doesn't appear in the algorithm, but
we imagine that it starts at zero and gets incremented every time we
finish the outer loop, so it counts how many times we have executed this
loop. We need this variable for the termination function and the loop
invariant. If you want to make it explicit you can actually replace the
outer loop with a `for`-loop where $j$ goes from zero to $n$, but we
need to prove that the outer loop is not executed more than $n$ times
for us to be able to do this, so we stick with the `while`-loop.

So we have indices $i$ and $j$---with $j$ imaginary---and we define the
following invariants for the inner and outer loops, respectively, see
[@fig:bubble-sort-invariants]:

$$I: \forall k\in[0,i-1): x[k]\leq x[i-1]$$
$$O_1: \forall k\in[n-j,n-1): x[k]\leq x[k+1]$$
$$O_2: \forall k\in[0,n-j), x[k] \leq x[n-j]$$

Strictly speaking, predicate $O_2$ is only well-defined when $j>0$, but
we are going to consider it true for all $j$---we could introduce
another imaginary variable, $x[n]=\infty$ to factually true, but we
might as well have the special case be $j=0$. The invariants say the
following in English: when we run the inner loop, then $x[i-1]$ is
larger than all elements to the left of it in the list, and when we run
the outer loop, then the last $n-j$ elements are sorted, and they are
the largest in the list.

![Invariants for the inner and outer loops of bubble
sort.](bubble-sort-invariants.pdf){#fig:bubble-sort-invariants}

Invariant $I$ is the easiest to prove. It is vacuously true when $i=0$,
and whenever we increase $i$ we have first moved the smaller of $x[i-1]$
and $x[i]$ to $x[i-1]$ so the new $i-1$ satisfy the invariant. $O_1$ and
$O_2$ are also vacuously true when $j=0$ (or defined to be by setting
the imaginary value $x[n]$ to infinity). Now, assume that the outer-loop
invariants are true when we begin iteration $j$. We need to show that it
is true for $j+1$ after we have executed the loop body. Consider now the
inner loop. If the last $j$ elements are already larger than those
before them, and already sorted, then the inner loop will not modify
them. The interesting step in the inner loop happens when reaches
$n-j-1$ and execute the inner body for this iteration, i.e., when we
update $i$ to $n-j$. When it does, invariant $I$ tells us that all
$x[k]$ for $k\in [0,n-j)$ we have $x[k]\leq x[n-j-1]$. Combined with
$O_2$, this tells us that the last $j+1$ elements are now larger than
the first $n-j-1$ elements, giving us that $O_2$ is true at this point.
Invariant $O_1$ combined with invariant $I$ gives us that the range
$[n-j,n)$\~ is sorted and \~$x[n-j-1]$ is less than or equal to all
elements in the range $[n-j,n)$, so this means that the elements in the
range $[n-j-1,n)$ are sorted, giving us that $O_1$ is also satisfied.
Since the invariants are satisfied at the end of their respective loops,
we have that the algorithm correctly sorts the input.

For termination, we observe that the invariants give us that the last
$j$ elements in $x$ are sorted after iteration $j$, so when $j=n$, all
the elements are sorted. A natural termination function would then be
$n-j$. The pattern for how we think about termination functions isn't
entirely satisfied, however. We used to require that the loop condition
should be false when the termination function hits zero (or goes below
zero), but `True` will never be false. We can rewrite the outer loop to

``` {.python}
swapped = False
while not swapped:
    # the usual loop body
```

and observe that `swapped` is `False` when no elements are swapped,
which happens when the inner loop finds no elements out of order---which
it does in when $j=n$.

**Exercise:** Since $O_1$ and $O_2$ tells us that the last $j$ elements
are already the largest numbers and are already sorted, we do not need
to have the inner loop iterate through these last $j$ elements. How
would you exploit this to improve the running time of bubble sort? The
worst-case behaviour will not improve, but you can change the running
time to about half of the one we have above. Show that this is the case.

If we consider the swaps executed by bubble sort more carefully, we will
see, as for insertion sort, that the elements in the input sequence are
either moved up or down to their correct position in the sorted list,
but never moved both up and down. So the number of swaps are only those
necessary to move elements to their correct positions. This is the same
insight we had for Insertion sort, and consequently, Bubble sort must
have the same swap complexity: the best-case number of swaps is zero,
and the worst case is $O(n^2)$. For swapping we also get the same
complexity as Insertion sort. The best-case number of comparisons happen
when the elements are already sorted, in which case we never set
`swapped` to `True`, and we perform $O(n)$ comparisons. In the worst
case, when we have to execute the inner loop $n$ times, we perform
$O(n^2)$ comparisons.

  --------------------------------------------------------------------------
  Algorithm      Comparisons    Comparisons    Swaps          Swaps
                 worst-case     best-case      worst-case     best-case
  -------------- -------------- -------------- -------------- --------------
  Selection      $O(n^2)$       $O(n^2)$       $O(n)$         $O(1)$

  Insertion      $O(n^2)$       $O(n)$         $O(n^2)$       $O(1)$

  Bubble         $O(n^2)$\~     ~$O(n)$~       ~$O(n^2)$~     \~$O(1)$
  --------------------------------------------------------------------------

The asymptotic complexity of Insertion sort and Bubble sort is the same.
There is a difference in the actual number of comparisons hidden under
the big-Oh, however.

For both algorithms, the number of comparisons is equal to the number of
iterations we execute in the inner loop. In Insertion sort, the inner
look iterates over the range $j\in(0,i]$ for each outer-loop iteration
$i=1,\ldots,n$; bubble sort iterates over the entire range
$i=1,\ldots,n$ each time the outer loop is executed. Because Insertion
sort iterates over an interval that shrinks by one for every outer-loop
iteration, it performs $\frac{1}{2}(n-1)n$ comparisons. Bubble sort
always iterates over the full range for each of the $n$ outer-loop
iterations, so it performs $n^2$ comparisons---twice as many as
Insertion sort.

When bubble sort's inner loop encounters a key $k$, it moves that key to
the right until it encounters a larger key. The largest key in the
entire sequence is moved to the largest index in the very first
iteration. The second time the inner loop is run, the second largest
element is moved to the second largest index, and so on. In general,
large values will move quickly to the right in the list; they "bubble
up", which is where bubble sort gets its name.

Smaller values, however, are only moved one step to the left in each
iteration of the inner loop. There is a variant of bubble sort that
tries to move both large values quickly to the right but also small
values quickly to the left. It essentially consists of two bubble sorts,
one that bubbles left-to-right and one that bubble right-to-left. It
alternates between these two inner loops, and because it moves left and
right in this motion it is sometimes called the cocktail shaker
algorithm, or simply cocktail sort. We can implement it like this:

``` {.python}
while True:
    swapped = False
    for i in range(1, len(x)):
        if x[i-1] > x[i]:
            x[i-1], x[i] = x[i], x[i-1]
            swapped = True
                
    if not swapped:
        break

    for i in range(len(x)-1, 1, -1):
        if x[i-1] > x[i]:
            x[i-1], x[i] = x[i], x[i-1]
            swapped = True

    if not swapped:
        break
```

The analysis of this variant of bubble sort is not different from the
one we did for bubble sort. Although the algorithm can run a bit faster
than bubble sort in practice, the worst case complexity is the same as
bubble sort. It performs exactly as many swaps---because, again,
elements are moved up or down using swaps until they find their final
position---but it will usually make fewer comparisons when the list is
close to sorted because it is faster in getting the elements to their
right position.

**Exercise:** With cocktail sort, after running the outer loop $j$
times, both the first $j$ and the last $j$ elements are in their final
positions. Show that this is the case.

**Exercise:** Knowing that both the first and last $j$ elements are
already in their right position can be used to iterate over fewer
elements in the inner loops. Modify the algorithm to exploit this. The
worst case complexity will still be $O(n^2)$, but you will make fewer
comparisons. How much do you reduce the number of comparisons by?

In [@fig:quadratic-sort-comparison-comparisons] and
[@fig:quadratic-sort-comparison-swaps] I have plotted the performance of
selection sort, insertion sort, and the two variants of bubble sort,
counting the number of comparisons or the number of swaps, respectively.
I have generated data in four forms:

-   Data that is already sorted---where insertion sort and the two
    bubble sorts run in $O(n)$, but selection sort runs in $O(n^2)$.
-   Data where the elements are sorted in reverse order. Here, insertion
    sort and the two bubble sorts meet their worst case setup, and we
    see that the bubble sorts use twice as many comparisons as insertion
    sort.
-   Data where the elements are almost sorted. Here, I have generated a
    sorted list of the numbers 1 to $n$ and swapped 20% of the elements
    to random positions. Here we get the performance where the insertion
    sort and the two bubble sorts run in $O(n^2)$ but with fewer
    comparisons since the sorted elements are already in place and the
    inner loop in insertion sort iterates over fewer elements and the
    inner loop in bubble sort and cocktail sort is run fewer times. The
    cocktail sort performs fewer comparisons than bubble sort for the
    reasons we have already discussed.
-   Finally, I have generated data that is random permutations of the
    elements from 1 to $n$. Here, the performance is close to the worst
    case for all algorithms in numbers of comparisons, but we do need
    fewer swaps in insertion sort and the bubble sorts than when the
    elements are sorted in reverse order. This is also to be expected
    since the reverse sorted case needs to swap elements the maximum
    possible number of times.

![Number of comparisons executed by the different quadratic-time sorting
algorithms. Despite appearance, the insertion, bubble, and cocktail
sorting algorithms do not run in constant time on sorted data. The lines
are linear, but compared to quadratic growth, the linear number of
comparisons is tiny. On sorted data, they all use exactly $n-1$
comparisons.](quadratic-sort-comparison-comparisons.pdf){#fig:quadratic-sort-comparison-comparisons}

![Number of swaps executed by the different quadratic-time sorting
algorithms.](quadratic-sort-comparison-swaps.pdf){#fig:quadratic-sort-comparison-swaps}

**Exercise:** Insertion sort runs in $O(n^2)$ when the input is sorted
in the reverse order, but can process sorted sequences in $O(n)$. If we
can recognise that the input is ordered in reverse, we could first
reverse the sequence and then run the insertion sort. Show that we can
reverse a sequence, in place, in $O(n)$. Try to adapt insertion sort, so
you first recognise consecutive runs of non-increasing elements, then
reverse these before you run insertion sort on the result. Show that the
worst-case running time is still $O(n^2)$, but try to compare the
modified algorithm with the traditional insertion sort to see if it
works better in practice.

### Index-based sorting algorithms

For much data that we can assign a total order to, all we can really do
with it is determine if one object is smaller than, equal to, or greater
than another. Sometimes, however, the data is in a form that we can
exploit to build faster sorting algorithms. If our keys are small
positive integers, we can use them as indices into lists. Let's call
sorting algorithms that use this idea *index-based*. (These algorithms
are also known as *distribution sorting* algorithms, but I find it
easier to remember "index-based" than *distribution* since a critical
property of these algorithms is to index into a list).

We can then exploit that we can create a list of length $m$ in $O(m)$
and for a list `x` we can get index `k`, `x[k]`, in constant time. We
will also exploit that we can append elements to a list `y`,
`y.append(k)`, in constant time[^17]. In this section, we will look at
two algorithms that exploit this: *bucket sort* and its big brother
*radix sort*.

Bucket sort assumes that we sort positive integer keys with a max value
of $m$ and runs in worst- and best-case $O(n+m)$. Radix sort relaxes the
requirement that the keys should be less than $m$ in magnitude but
instead assume that we can split keys into $k$ sub-keys that are bounded
by $m$. It then uses bucket sort on these keys $k$ times, achieving a
best- and worst-case running time of $O(k(m+n)$.

The memory usage depends on whether we are only sorting keys---i.e. the
values we sort are identical to their keys---or whether our data items
carry more information than their keys. This matters because we need to
remember actual data values in the latter case but only a counter in the
former. If we are merely sorting keys, then the memory usage for bucket
sort is $O(m)$. If data items are more than their keys, bucket sort
needs $O(n+m)$ memory. It is for this case that it is essential that we
can add to a list in constant time; we use this to keep track of data
items efficiently. Radix sort just runs bucket sort $k$ times, without
needing extra memory between runs, so its memory complexity is the same
as bucket sort. Neither of these two algorithms is in-place.

#### Bucket sort

We first consider the case where our keys are positive integers bounded
by some number $m$. The smaller, the better, but the important part is
that they are bounded by a known value $m$. We can create a list of
length $m$ in time $O(m)$, and what we will do is, for each key $k$, we
will put the element with that key at position $k$ in this list. We call
the list the *buckets* and we just put our elements in different buckets
based on their key. The algorithm is called *bucket sort*.

The simplest version of bucket is only sorting keys. We assume that our
elements are equal to their keys, i.e. we are sorting positive integers
bounded by $m$. The algorithm then looks like this:

``` {.python}
buckets = [0] * m
for key in x:
    buckets[key] += 1
result = []
for key in range(m):
    for i in range(buckets[key]):
        result.append(key)
```

Our input is the list `x` of length $n$ and the bound on our keys, `m`.
With this implementation, the bound $m$ has to be strict. We create $m$
buckets, but they are indexed with values from zero to $m-1$. If the
largest number in your keys is $m$, you need to allocate $m+1$ buckets.

We first create a list of buckets of length $m$ and set all buckets to
zero---this takes time $O(m)$. Then we iterate over all our keys in `x`
and increment the count in `bucket[key]`. After that, we simply collect
the keys again in sorted order. We iterate through the buckets, and for
each key, we output that key as many times as the bucket's
counter---this is how many times that key was found in the input. We
create a new list for the result and append to this list. Although we
have two nested loops for collecting the results, the inner loop is only
executed $n$ times. The outer loop is executed $m$ times and the inner
loop, in total, $n$ times. Since we can append to `results` in constant
time, the running time for the entire algorithm is $O(n+m)$. The
algorithm is not in-place, and we use $O(n+m)$ extra memory, for the
bucket list and the result list. If you want to avoid spending $O(n)$
memory on the results list, you can modify the input list instead:

``` {.python}
buckets = [0] * m
for key in x:
    buckets[key] += 1
i = 0
for key in range(m):
    for j in range(buckets[key]):
        x[i] = key
        i += 1
```

This doesn't change the running time of the algorithm but reduces the
memory usage to $O(m)$.

If $m\in O(n)$, this means we have a linear time sorting algorithm.
Since we cannot sort any list of $n$ elements without at least looking
at each key, this is an optimal algorithm---you cannot possibly sort $n$
elements in time $\omega(n)$, and we sort them in $\Theta(n)$. This
doesn't contradict that sorting $n$ elements using comparisons takes
time $\Omega(n\log n)$, because we do not rely on comparisons. The
algorithm only works when our keys are positive integers bounded by
$m\in O(n)$. Comparison sorting is more general than that and therefore
a harder problem to solve.

**Exercise:** Argue why the inner loop in

``` {.python}
result_keys, result_values = [], []
for key in range(m):
    for val in buckets[key]:
        result_keys.append(key)
        result_values.append(val)
```

only executes $n$ times.

**Exercise:** Argue why the bucket sort actually sorts the input.

This variant of bucket sort is also known as counting sort because we
simply count how many times we see each key. This doesn't quite cut it
if we need to sort elements where the keys are not the full information
associated with them. If, for example, we have a list of values and
another of keys and we need to sort the values according to the keys.
Then we need to remember which values are actually put in each bucket,
not just how many there are in each bucket. We can do this by putting a
list in each bucket and append the values to their respective buckets:

``` {.python}
buckets = [[] for bucket in range(m)]
for i in range(n):
    key = keys[i]
    val = values[i]
    buckets[key].append(val)

result_keys, result_values = [], []
for key in range(m):
    for val in buckets[key]:
        result_keys.append(key)
        result_values.append(val)
```

You cannot use

``` {.python}
buckets = [] * m
```

here, since this would create a list of `m` references to the *same*
list. Appending to one bucket would modify all buckets. Instead, we use
the list comprehension expression

``` {.python}
buckets = [[] for bucket in range(m)]
```

to create a new empty list for each bucket.

Other than that, the general bucket sort is not much different from
counting sort. We append the values to the buckets instead of counting
keys, and we collect the values from the buckets after that.

Because we need to store $n$ elements in the buckets, the memory usage
is now $O(n+m)$ rather than $O(m)$. We could still reuse the input lists
when we collect the sorted elements, but it would not reduce asymptotic
the memory usage.

Because we append values to the buckets and read them out later in the
order they were added, the bucket sort is a stable algorithm. It
wouldn't be if we prepended elements to the lists, but you shouldn't do
this anyway with Python `list` objects. We can append to `list` objects
in $O(1)$ but prepending takes time $O(\ell)$ if the list has length
$\ell$.

#### Radix sort

Bucket sort can sort $n$ elements with keys bounded by $m$ in time
$O(n+m)$ which is excellent if $m$ is small. As long as $m\in O(n)$ it
is an optimal sorting algorithm. If $m$ is much larger than $n$,
however, handling $m$ buckets slows down the algorithm. If, for example,
all we knew about the keys were that they were 32-bit positive integers,
we would need $2^{32}$ buckets, which is more than four billion buckets.
Sorting 32-bit integer keys using bucket sort is apparently not a viable
approach.

If, however, our keys can be broken down into $d$ sub-keys, each bounded
by a reasonable $m$, we have an algorithm that will sort these in
$O(d\cdot(n+m))$, by sorting by each sub-key in turn, running $d$
applications of bucket sort. For 32-bit integers, for example, we can
split the keys into four bytes. Each byte can hold $2^8$ different
values, so $m=256$ is an upper bound for these. You can, therefore,
split a 32-bit integer into a tuple of four sub-keys, each bounded by
$256$. You need some bit operations to do it, but it looks like this:

``` {.python}
subkeys = (k         & 0xff
          ,(k >> 8)  & 0xff
          ,(k >> 16) & 0xff
          ,(k >> 24) & 0xff)
```

You do not need to know how this work to use the trick, but if you are
interested, I explain it at the end of the chapter, in
[@sec:bin-repres-of-numbers].

This algorithm for sorting $d$ sub-keys bounded by $m$ is called *radix
sort*, and that it runs $d$ iterations of bucket sort tells you exactly
how it works:

``` {.python}
for j in range(d):
    key_buckets = [[] for bucket in range(m)]
    value_buckets = [[] for bucket in range(m)]
    for i in range(n):
        key = keys[i]
        subkey = key[j]
        val = values[i]
        key_buckets[subkey].append(key)
        value_buckets[subkey].append(val)

    key_result, value_result = [], []
    for subkey in range(m):
        for key in key_buckets[subkey]:
            key_result.append(key)
        for val in value_buckets[subkey]:
            value_result.append(val)

    keys = key_result
    values = value_result
```

Here, $j$ ranges over the $d$ sub-keys. In each bucket sort, we use $m$
buckets. We need to keep track of both keys and values here because the
sub-keys do not contain the full information about the keys. We collect
the results of the bucket sorts in two lists, `key_result` and
`value_result`, and at the end of each outer loop we update the `keys`
and `values` lists to their sorted versions, so these are ready for the
next iteration.

Radix sort only works because bucket sort is stable, and the order in
which we sort the sub-keys is critical. To see this, let us consider a
simple case where we have two sub-keys, and we want to sort

``` {.python}
keys = [(1,0), (2,1), (1,1), (0,1), (1,1)]
```

If we want to sort this into the usual tuple order, also called lexical
order, we need first to sort the tuples by the first component and then
by the second. So the list we want to end up with is this:

``` {.python}
[(0, 1), (1, 0), (1, 1), (1, 1), (2, 1)]
```

If you set $d$ to two and run the radix sort, you will get the list
sorted first by the second component and then by the first. We will get

``` {.python}
[(1, 0), (0, 1), (1, 1), (1, 1), (2, 1)]
```

To see why consider what happens in the two iterations of the radix
sort. In the first iteration, we do sort by the first tuple component.
So we sort the list into this:

``` {.python}
[(0, 1), (1, 0), (1, 1), (1, 1), (2, 1)]
```

If we only consider the first component, this list is sorted. Of course,
we do not only consider the first component, so we execute a second
bucket sort, this time on the second component, to get the result

``` {.python}
[(1, 0), (0, 1), (1, 1), (1, 1), (2, 1)]
```

Since bucket sort is stable, we keep the order from the first sort
within the buckets of the second sort. We keep the order of the tuples

``` {.python}
[(0, 1), (1, 1), (1, 1), (2, 1)
```

that all have the same value for the second sub-key. Because the sort is
stable and preserves the ordering for the first key, when we sort on the
second key we get a list that is sorted by both keys. In the opposite
order from how we apply the bucket sort, though. The second key we sort
on becomes the major key, the first the minor key.

To sort the tuples in lexicographical order, we the second sub-key
(`key[0]`) to be the major key and the second sub-key to be the major
key (`key[1]`). To get this, we must first apply bucket sort to the
first key and then the second; we must sort with subkeys
$k = d-1,d-2,\ldots,1,0$:

``` {.python}
for j in range(d-1,-1,-1):
    # loop body same as before
```

The radix sort is a very powerful algorithm for sorting positive
integers that can fit into a constant number of computer words since
these can generally be split into $d$ bytes. For 32-bit integers, as we
saw, we can split them into 4 bytes. For 64-bit words we need 8 bytes,
and for 128-bit words we need 16 bytes, but in all cases, we can sort
the integers in linear time because $m$ is bounded by the constant
256.[^18]

If we have both positive and negative integers, we cannot use radix sort
out of the box. If we index into a list with a negative number, we just
index from the back of the list, which is not what we want. If you
actually break a negative number into 8-bit bytes and consider these as
positive integers, you will get the wrong answer. This is a consequence
of how negative numbers are represented as bits in computer words. You
do not necessarily need to know how negative numbers are represented on
your computer (but you are interested I will tell you in
[@sec:bin-repres-of-numbers]).[^19] Suffices to say that if you sort
positive and negative numbers as bit-patterns, you will not get the
numbers sorted as integers.

There is a simple trick to sorting integers with both positive and
negative numbers, though. If $a$ is the smallest number in your input,
and it is negative, then add $-a$ to all the numbers. Now they are
positive but in the same order as before. You can sort these, and then
subtract $-a$ again to get the original numbers back.

If you sort variable length keys, for example, strings, you do not
necessarily have a constant bound on how many sub-keys you need. If
$d\in O(n)$, you are back to having an $O(n^2)$ algorithms, and you can
do better with a $O(n\log n)$ comparison sort.

Generalising searching and sorting {#sec:general-search-sort}
----------------------------------

Before we leave sorting there is one additional issue I want to mention.
We have assumed that, for each item in the list we want to sort, we have
an associated key (or keys) we use to define the ordering of the
objects. We haven't discussed how we extract keys from the items we wish
to sort or how we use them to compare objects.

If you only ever have to sort numbers, this isn't a concern. If you need
to sort other types of objects and tailor your algorithm to the exact
type of the objects, then you do not need to worry about it either. If,
however, you want to implement a search or sort algorithm that works for
different types of objects, it is a concern. You need to provide the
user of your algorithm some handle by which to specify the order of
objects. Since you are most likely to be the user at some point, you
should make that handle easy to work with and yet flexible enough to
handle all cases you will need.

This is typically done using functions in one of two ways: you can
specify a function for comparing two objects. A common approach is to
require a function of two arguments, $a$ and $b$, that determines if
$a<b$ (or $a>b$, it doesn't matter which). Since we only aim for putting
the objects in order, so no $x[i]>x[i+1]$ we do not need any other
information. If we want to search for an element, we also need to know
how to test for equality, of course. To handle both, a common approach
is to require that the function returns a negative number for $a<b$,
zero for $a=b$, and a positive number for $a>b$.

An entirely different approach is to provide a function that maps your
objects to something that you already know how to sort. That is the
approach Python has taken for its `sort` and `sorted` functions. Objects
of simple types, like numbers and strings, Python already knows how to
sort. Python can also sort composite types such as lists and tuples if
they hold objects that Python can already sort. If you have more
complicated objects, or if you need to sort them according to some
specialised ordering, then you need to provide a `key` function.

We haven't seen how to define our own functions yet (we will in [Chapter
@sec:functions]), but we have used plenty, so you should be able to
understand how this works with an example.

Consider a list of fruits:

``` {.python}
fruit = [
    "apple",
    "orange",
    "bananba",
    "kiwi"
]
```

If we sort these, we get their alphabetic (lexicographic) ordering.

``` {.python}
>>> fruit = ["apple", "orange", "bananba", "kiwi"]
>>> sorted(fruit)
['apple', 'bananba', 'kiwi', 'orange']
```

If for some reason, we want to sort the fruits by word-length, we can do
this:

``` {.python}
>>> sorted(fruit, key = len)
['kiwi', 'apple', 'orange', 'bananba']
```

The `len` function, which we have used several times already, gives us
the length of a sequence. In this case, the length of a sequence of
letters, so the length of a word. When we give this function to `sorted`
it becomes the key it sorts by. So when it looks at an object it doesn't
see the object itself, but rather the result of calling `len` on the
object, so it sees word lengths rather than the actual strings.

For providing a handle into a search function, of the two approaches,
providing a comparison function or a key-function, I personally think
the second is much simpler and more elegant, but your mileage may vary.

We can easily implement sorting algorithms that use a `key_fun`
function. Selection sort will look like this:

``` {.python}
for i in range(len(x)):
      # find index of smallest elm in x[i:]
      min_idx, min_val, min_key = i, None, x[i]
    for j in range(i, len(x)):
        if key_fun(x[j]) < min_key:
            min_idx, min_val, min_key = j, x[j], key_fun(x[j])        
    x[i], x[min_idx] = min_val, x[i]
```

Insertion sort looks like this:

``` {.python}
for i in range(1,len(x)):
    j = i
    while j > 0 and key_fun(x[j-1]) > key_fun(x[j]):
        x[j-1], x[j] = x[j], x[j-1]
        j -= 1    
```

Bucket sort requires that the key-function maps to integers and we need
to find a number they are all smaller than, but other than that, it is
simply this:

``` {.python}
n = len(x)
m = max(key_fun(e) for e in x) + 1
buckets = [[] for bucket in range(m)]

y = []
for e in x:
    buckets[key_fun(e)].append(e)
for b in buckets:
    for e in b:
        y.append(e)
# Result is now in y
```

If we used a comparison function, we would only be able to write generic
comparison algorithms. With a key-function, we can also handle bucket
sort, at least as long as the key-function gives us a small integer.
There is a bit more to do with radix sort, but you could imagine the
key-function returning a tuple of sub-keys.

How computers represent numbers {#sec:bin-repres-of-numbers}
-------------------------------

For most of what we have seen in this and the earlier chapters, we do
not need to know how our computer actually represents numbers. A number
is a number, and while we do have to differentiate between numbers that
can fit into a computer word and numbers that cannot do so when we
consider complexity in the RAM model, we do not worry about their
representation beyond that. If we want to sort integers using radix
sort, however, we do need to know a little bit about how numbers are
stored. I gave you a piece of code to extract bytes from a 32-bit
integer:

    subkeys = (k         & 0xff
              ,(k >> 8)  & 0xff
              ,(k >> 16) & 0xff
              ,(k >> 24) & 0xff)

This extracts four 8-bit bytes from one 32-bit integer and gives us four
sub-keys. What I didn't tell you was that the order you should apply the
bucket sort applications in radix sort to get the 32-bit integers sorted
depends on your architecture. I explain why in the next sub-section.

Manipulation of computer words with bit-operations is very low-level
programming and not something you usually worry about in day to day
problem-solving. If you are not interested in knowing the low-level
details of how we do this, you can skip this section, but if you end up
using radix sort on integers in the future, I recommend that you at
least skim the next sub-section.

In the last sub-section, I explain how computers represent negative
numbers. If you sort by adding a number to all your input to make them
positive and then subtract it again when you are done, you do not need
to know this, and I cannot think of any case where this is relevant for
sorting. But if you are interested in knowing, then check out that
section.

### Layout of bytes in a word

For radix sorting integers, you do need to be able to split a
computer-word into bytes---or in general into $d$ $\log_2 m$ bit
sub-keys to get the $O(dm)$ running time. To extract the bytes for a
computer word, we need two bit-operations: right-shift and bit-AND. A
right-shift simply moves the bits in a computer word to the right.[^20]
If we shift a word by 8 bits, we lose the eight lowest bits, the lowest
byte, and we move the second byte down to replace the first (and the
third to replace the second, the fourth to replace the third; for
integers with more than 32 bits, this just goes on). If we shift by 16,
we move the third byte down to the lowest byte, and if we shift by 24
bits, we move the highest byte down to the lowest
[@fig:extracting-bytes]. A bit-AND operation, the operator `&` in
Python, takes as input two bit-patterns and produce a bit-pattern where
each bit-position only depends on the same positions in the two input
words and each bit is set to one if both the input bits in the input are
one, and otherwise it is set to zero. The hexadecimal numeric `0xff` has
the lowest bits set to one and all others to zero. If we AND a number
with this number, we get the bits in the lowest byte only. AND'ing with
a number like this is known as *masking*. When we mask one bit-pattern
with another, we extract parts of the bits and leave the others at zero.

![Extracting four bytes from a 32-bit
integer.](extracting-bytes.pdf){#fig:extracting-bytes}

When we do a computation such as

``` {.python}
subkeys = (k         & 0xff
          ,(k >> 8)  & 0xff
          ,(k >> 16) & 0xff
          ,(k >> 24) & 0xff)
```

we create a tuple with four components that correspond to the four bytes
in a 32-bit word, see [@fig:extracting-bytes].

Integers in Python comes in two flavours, but Python automatically
translate between them, so you rarely have to worry about it. The first
flavour, *plain integers*, can fit into a computer word. These integers,
therefore, are limited to how many bits there are in a computer word.
You are guaranteed that there are at least 32 bits, but there can be
more. The second type of integers, *long integers*, needs more than one
computer word, but they are not bounded by any constant, only by how
much RAM your computer has. The code above assumes that you have plain
integers and that these fit into 32 bits.

Bytes, consisting of 8 bits, can represent numbers from zero to
$2^8-1=255$. You can think of them as numbers in base 256. A 32-bit
integer, considered as individual bytes $b_1$ to $b_4$, would be
$b_1\times 256^0 + b_2\times 256^1 + b_3\times 256^2 + b_4\times 256^3$
where $b_1$ to $b_4$ are the four bytes in the word. Just as a decimal
number such as 123 is $3\times 10^0 + 2\times 10^1 + 3\times 10^2$. This
is what we exploit when we split a 32-bit integer into four bytes that
we can radix sort.

This sounds easy, and it is, and so of course, hardware designers went
and made it more complicated. Different hardware arranges the bytes in a
computer word differently. Depending on your hardware, the number
represent as a 32-bit integer can be both
$b_1\times 256^0 + b_2\times 256^1 + b_3\times 256^2 + b_4\times 256^3$
and
$b_4\times 256^0 + b_3\times 256^1 + b_2\times 256^2 + b_1\times 256^3$.
Different hardware puts the most-significant byte at the left or at the
right. The different choices are called *endianess*;[^21]
*little-endian* computers put the least-significant byte as the
left-most byte and *big-endian* computers put the least-significant byte
as the right-most byte. There is no *right* way to represent integers
with respect to byte-order, but people can get passionate about it.

In the code above, we put the least-significant byte as the first
sub-key, the second-least significant byte as the second, and so forth.
If we sort the sub-keys in this order, it means that the final result is
sorted first by the right-most byte, $b_4$, then by byte $b_3$, and then
$b_2$ and $b_1$. You are most likely using an x86 architecture since all
personal computers use this architecture these days. If you do, you are
using a little-endian architecture, and this means that a 32-bit integer
is represented as
$b_4\times 256^0 + b_3\times 256^1 + b_2\times 256^2 + b_1\times 256^3$
and the code above gives you sub-keys where a lexicographical sorting
matches a numerical sorting of the original number. If you are on a
big-endian architecture, you need to reverse the order of the elements
of the tuple to get the right order when you sort based on it. Or, you
need to sort the four bytes in the opposite order, as we saw in the
example where we sorted pairs.

### Two-complement representation of negative numbers

The reason that we couldn't simply sort negative integers using radix
sort is that bit-patterns, interpreted as base-two numbers, do not match
how the computer interprets the bit-patterns for negative numbers. If
you have only positive numbers, then you can sort these bit-wise. The
negative numbers, however, will be considered *greater* than the
positive numbers and will end up after the positive numbers in the
sorted list. They will also appear in reverse order.

On computers, we distinguish between *signed* and *unsigned* numbers.
Unsigned numbers are always positive, and with $n$ bits we can represent
$2^n$ different numbers; zero is one of those numbers, so signed numbers
can be any of $0,1,\ldots,2^n-1$. With signed numbers, we can still
represent $2^n$ numbers, but some will be negative, and some will be
positive. A simple approach to represent negative numbers is to take one
of the $n$ bits and use it as the sign. This representation is known as
*sign-and-magnitude* representation. If we do this, we get $2^{n-1}$
positive and $2^{n-1}$ negative numbers---we have $n-1$ bits to
represent the numbers when we use one bit for the sign---so we can
represent the range $2^{n-1}-1,\ldots,2^{n-1}$. We end up having two
zeros, though; one positive and one negative zero.

Another representation of negative numbers is *ones-complement* where a
negative number is represented as the bit-wise negation of the
corresponding positive number. What this means is that to change the
sign of a number, $a$ you negate all its bit, i.e. you change all zeros
to ones and vice versa. A four-bit representation of 2 would be 0010, so
the four-bit representation for -2 would be 1101. We still get two
different zeros, and we can represent that same range as when we use a
sign bit. Ones-complement is slightly easier to implement in hardware
than sign-and-magnitude, and many older computers used this
representation.

The representation that modern computers use is *two's complement* and
is even simpler for hardware to deal with, which is why it has won out
as the dominant representation. I am not aware of any modern computers
that do not use this representation. Arithmetic that mix both positive
and negative numbers can be done by only doing arithmetic on positive
numbers. This means that there is no need for hardware circuits to deal
with negative numbers. For us humans, though, two's complement can be a
little harder to understand.

In two's complement $n$-bit words we can represent the integer range
$-2^{n-1}$ to $2^{n-1}-1$. We have one more negative number than we have
positive, and we have only one zero. To change a positive number, $a$,
into $-a$, you first negate its bits (just as for ones complement) but
then you add one. For four-bit numbers, 1 is 0001, negated this is 1110.
If we add one, we get 1111. This is -1 in two's complement. To go from
-1 to 1, we do the same. We negate the numbers for -1, 1111 to 0000, and
add 1, 0001, and get 0001, which is 1. We do the same for 2, 0010. We
negate it and get 1101, then add one, 0001, and we get 1110. This is -2
in two's complement. Going back we do 1110 to 0001 and one, 0001, and
get 0020, or 2 in decimal. For 3, 0011 in binary, we get 1100 + 0001 =
1101 for -3.

In two's complement, positive numbers have 0 at the most significant
bit, and negative numbers have 1 at the most significant bit. This looks
like a sign bit but isn't exactly. There is only one zero, the
bit-pattern with all bits set to zero. If only the most significant bit
is set, this is not interpreted as negative zero, but rather the
smallest negative number we can represent.

With four bits, the largest positive number we can represent is 0111, or
7 in decimal. We cannot represent 8; that would put a one-bit in the
fourth position, and such a number we would consider negative. We can
represent -8, however; it will be the bit-pattern 1000. The positive
number 8 does require four bits to represent, and it would be since this
is 1000. The negation of this is 0111, and if we add one to it, we get
1000, which is -8 in two's complement. We end up with the same bit
pattern as the unsigned value for the positive number, but we interpret
the bit pattern differently.

What makes two's complement particularly smart is that we can do
arithmetic with both positive and negative numbers using only rules for
positive numbers. For example, to compute $a-b$ we can add the two's
complement representation of $a$ and $-b$ in binary modulo $2^n$, where
$n$ is the number of bits we have. Modulo $2^n$ in binary means using
the $n$ least significant bits, so any over-flow of bits are simply
ignored.

$$2_{10} - 1_{10} = 0010_2 - 0001_2 = 0010_2 + 1111_2 = 10001_2= 0001_2 = 1_{10}$$
$$3_{10} - 4_{10} = 0011_2 - 0100_2 = 0011_2 + 1100_2 = 1111_2 = -1_{10}$$
$$5_{10} - 3_{10} = 0101_2 - 0011_2 = 0101_2 + 1101_2 = 10010_2 = 0010_2 = 2_{10}$$

This means that we do not need separate hardware for addition and
subtraction, we only need addition, which greatly simplifies the
computer. The same goes for multiplication and division. I won't prove
this here, but you can almost see why if you consider how we would solve
multiplication and (integer) division through repeated addition. If you
want to compute $a\cdot b$ you can set an accumulator to zero and then
add $a$ to it $b$ times. Easy enough. If you want to compute $a/b$ you
can start a counter at zero, then add $b$ to it until you get a number
above $a$. One minus the count is $a/b$. If you can reduce all
arithmetic to the addition of positive numbers, then you have simpler
hardware. Now, modern hardware is smarter than this simple approach to
multiplication and division, but it can still avoid explicitly dealing
with negative numbers by using two's complement.

To see why we can replace subtraction with addition, we need a little
algebra. The reason for has to do with how we add modulo $2^n$. In the
ring of modulo $2^n$, $-a$ is the same as $2^n-a$, so instead of
subtracting $a$ from a number, you can add $2^n-a$ to it. In two's
complement, $-a$ is the same as $2^n-a$ when $n$-bit words are
considered unsigned. For example, in four-bit words (where we do
addition modulo $2^4=16$), -2 is $1110_2$ (the negation of 2, 0010, is
1101, and you add one to that to get 1110). Unsigned, $1110_2$ is
$14_{10}$, which is $(16-2)$ modulo 16. So if we want to compute
$10-2=8$, we can do this as $10 + (16-2) = 10+14=24$ which is 8 modulo
16.

The way we shift bits is affected by the two's complement representation
of integers as well. If we shift a number $k$ bits to the left,
$n\ll k$, we always fill the right-most bits with zeros, and this always
amounts to multiplying $m$ by $2^k$ (modulo $2^n$).

$$3_{10} \ll 2 = 0011_2 \ll 2 = 1100_2 = 12_{10} = 3_{10}\times 2^2$$

$$-2_{10} \ll 2 = 1110_2 \ll 2 = 1000_2 = 8_{10} \mod 16$$

$$-2_{10}\times 2^2 \mod 16 = -8_{10}\mod 16 = 8_{10}\mod 16$$

Whether shifting to the right by $k$ bits amounts to dividing by $2^k$
depends on whether we do logical- or arithmetic shift. With
logical-shift, we fill the left-most bits with zeros, and this amounts
to dividing by $2^k$ for positive numbers but not negative numbers.

$$6_{10} \gg 1 = 0110_2 \gg 1 = 0011_2 = 3_{10} = 6_{10}/2^1$$

but

$$-2_{10} \gg 1 = 1110_2 \gg 1 = 0011_2 = 3_{10} \mod 16$$

where, of course, $-2/2^1=-1=15\mod 16$.

With the arithmetic shift, we fill the left-most bits with the value the
left-most bit has before we shift. For positive numbers, where the
left-most bit is zero, this doesn't change anything, but for negative
numbers, where the left-most bit is one, it ensures that shifting $k$
bits to the right amounts to dividing by $2^k$:

$$-2_{10} \gg 1 = 1110_2 \gg 1 = 1111_2 = 15_{10} \mod 16 = -1\mod 16$$

In Python, shifting to the right is the arithmetic shift.

Functions {#sec:functions}
=========

So far, we have implemented algorithms where we have a reference to our
input before we run our computations and where we print the output of
the algorithm. Our algorithm is the code between the input and the
output. But what happens if, for example, we need to sort more than one
list, or if we need to search a list for more than one key?

With the approach we have seen so far, we would need to copy the entire
code for each time we need to run an algorithm. This will give us many
copies of the same code, so what if there is an error in the code? We
would need to fix the code each time we have a copy---and remember where
each copy is in our program. This is not efficient, and writing large
programs this way is infeasible. We need a mechanism to write implement
algorithms once and reuse the implementation whenever we need to use the
algorithm. Since the input and output of each use of the algorithms will
vary each time we execute it, we need a mechanism for handling this as
well.

Once approach to reusing implementations is *functions*. A function is a
piece of code that we can invoke from multiple places in a program. We
can tell it what its input should be, so we can vary that from call to
call of the function. Each time we invoke a function, and it finishes
its computation, our program will continue from the place where we
called the function.

**FIXME:** I do *not* have a good example here!

FIXME: appendix here
--------------------

Recursion {#sec:recursion}
=========

In this chapter, we consider an immensely powerful technique for solving
problems: *recursion*. Recursion involves recognising that a problem
really consists of the same kind of problem, just on a smaller scale.
For example, to sort $n$ elements, we can first find the smallest, then
sort all the others and put them after the smallest. This is, in its
essence, what selection sort does, we just didn't explain it in these
terms. When we do describe the algorithm like this, the recursive part
is that we sort all but the smallest object as part of sorting all the
items. To sort $n$ elements, we need to sort $n-1$. This is what
recursion is.

Recursion is both a way to write functions and a way to design
algorithms. When used to develop new algorithms, it is also called
*divide and conquer*, and we return to this in [Chapter
@sec:divide-and-conquer]. In this chapter, we will focus on recursive
functions.

Definitions of recursion
------------------------

Recursion means defining something in terms of itself, and you have
no-doubt seen recursive definitions before, even if they were not called
that. A classical example is the factorial of a number $n!$. The
factorial is usually defined as this:

$$n! = \begin{cases}
 1 & n=1 \\
 n\times(n-1)! & \text{otherwise}
\end{cases}$$

The *Fibonacci* numbers can be defined as this:

$$
F(n) = \begin{cases}
0 & n = 0 \\
1 & n = 1 \\
F(n-1) + F(n-2) & \text{otherwise}
\end{cases}
$$

The pattern we see for these definitions is that we define the value for
a number, $n$, as either a fixed constant or some expression that
involves the function we are defining itself, applied to some smaller
number. The cases where we can get a result immediately from the
definition are called *base cases*. For factorial, the base case is
$n=1$ where we directly get the value 1. For Fibonacci numbers, the base
cases are $n=0$ and $n=1$, where we get the values 0 or 1 right away.
The other cases are called the *recursive cases*.

One way of defining natural numbers is also recursive. A number $n$ is a
natural number if it is zero or if $n-1$ is a natural number.

For a recursive definition to be well-defined, the recursive cases must
bring us closer to base cases, so we do not have an infinite regression
that never brings us to termination. And when I say termination here, it
is not unlike the issue with the termination of algorithms; it is the
same problem, just in a different disguise. We cannot take an arbitrary
recursive function and an input and determine if the function will
evaluate to a function or go infinitely deep in recursions. Just as we
cannot take a general program and its input and decide if it halts. They
are two sides of the same coin. We must take some care in defining
recursive functions to avoid this, just as we must take care to ensure
that our algorithms terminate. In the case of recursions, we have a
natural termination function---how far a function call is from a base
case. If we can show that each recursive call brings us closer to a base
case, then we are in the clear.

Because recursion is self-referential---it solves a smaller instance of
the problem it is solving---comic definition of recursion is this:

> Recursion, *see Recursion.*

The more useful definition of recursion is definitions where we have one
or more base cases and one or more formulae that covers all other cases
with references to the definition itself.

Strictly speaking, this would be a definition of *recursive
definitions*, but it works equally well when we consider computational
problems. We have a recursive algorithm when we have some base cases
that we can handle directly, and some rules for solving all other cases
by resolving the same problem on smaller parts of the input.

Recursive functions
-------------------

We used recursion several times in [Chapter @sec:searching-and-sorting]
even though we never called it that. Consider the linear search
algorithm. When we search through a list `x`, if we have reached the end
of the list without finding the element we are searching for, we are
done and can report that the object is not in the list. Otherwise, we
look at the first item in the list, and if that is the item that we are
looking for we are done and can report that we found it. These two cases
are the base cases. Otherwise, we do a linear search in the remainder of
the list. That is the recursive case.

We can make the recursive nature of linear search more explicit by
defining a *recursive function:*

``` {.python}
def linear_search(x, e, i = 0):
    if i == len(x):
        return False
    if e == x[i]:
        return True
    else:
        return linear_search(x, e, i + 1)
```

This does exactly what we described above. There are two base cases and
one recursive case. For the function, the recursive case is handled by
the function calling itself.

This version of linear search is, unmistakably, much more complicated
than the one we had before, and I do not recommend that you use it
instead of iterating through `x`. You should, however, be able to
convince yourself that it does the same thing.

The only difference between a recursive definition and a recursive
function in Python is that the former defines something while the latter
actually computes something. There is no other difference. For example,
we can write a function for computing---as opposed to defining---the
factorial of a number like this:

``` {.python}
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
```

**Exercise:** Implement a recursive function that computes the $n$'th
Fibonacci number.

Binary search is another example of a recursive algorithm. In this
algorithm, we either have an empty interval to search in, in which case
we can report `False`. Or, we have the object we are searching for right
in the middle of the range we need to explore, in which case we can
report `True`. If all else fails, we have the recursive case, we
continue our search in either the lower or, the higher half of the
range.

Again, we can be more explicit in defining this as a recursive
computation by implementing it as a recursive function:

``` {.python}
def bsearch(x, e, low = 0, high = len(x)):
    if low >= high:
        return False
    mid = (low + high) // 2
    if x[mid] == e:
        return True
    elif x[mid] < e:
        return bsearch(x, e, mid + 1, high)
    else:
        return bsearch(x, e, low, mid)
```

You should convince yourself that this, indeed, does the same as the
binary search we have seen earlier.

If you recall, we required of recursive definitions that the recursive
cases must move us closer to base cases and observed that this was
related to termination. If each recursive call moves us closer to a base
case---whatever that means---then the computation will eventually
terminate. If not, then there is no such guarantee. You should think
about recursive functions as more general termination functions and
prove that they reach a base case for all input.

For binary search, the termination function was `high - low`. This works
equally well for the iterative version we have seen earlier as for the
recursive function defined above. We didn't use a termination function
for our earlier implementation of linear search; we didn't need one
because we know that a `for`-loop over a finite sequence will terminate.
For the recursive case, we cannot make as simple an argument, but of
course, the situation is the same. In each recursive call, the index `i`
gets closer to the end of `x`. So, we can use as termination function
`len(x)-i`.

Some people find recursion a challenging concept, primarily when we use
recursion for computation. Most people do not have any problem with
accepting recursive definitions, but when we solve a problem by solving
the exact same problem, it feels like a circular definition. "For
recursion, see recursion". It isn't, however, and the reason is that we
never solve a problem by trying to solve exactly the same problem. We
solve a problem that is closer to a base case; our termination function
decreases with every recursive function call.

If you still find recursive functions hard to wrap your mind around, you
might take comfort in knowing that many early computer scientist did as
well. Early programming languages could not define recursive functions.
It just didn't occur to people that this might be useful. This doesn't
mean that they didn't solve problems recursively; they just didn't use
recursive functions. Just like we did the linear and the binary search
without recursive functions before we reformulated the algorithms as
recursive. Recursion is such a powerful technique, however, that all
modern languages support it. Some even go so far that they have replaced
loops with recursion entirely; they will not let you implement loops at
all, only recursive functions.

Recursion stacks
----------------

To understand how recursive functions work, we first need to understand
a little deeper how function calls work. Recall that we have two
different kinds of variables in Python, global and local variables.
There are a bit more to variables than this, but we do not need to worry
about that for now. Global and local variables are all we have seen so
far. Global variables are those we assign to at the outermost level in a
Python program while local variables are either function parameters or
variables we assign to inside a function. For example, in this program:

``` {.python}
x = 2
def add_one(x):
    return x + 1
add_one(2 * x)
```

We have two global variables, `x` and `add_one`. The `x` variable is one
we have defined by assigning two to it. The `add_one` variable is the
result of a function definition. Inside the `add_one` function we have
another variable named `x`, we have created it by making a function
parameter. This variable is distinct from the global variable `x`; they
have the same name but can refer to two different objects. Inside
`add_one`, `x` is a local variable; outside of `add_one`, `x` is a
global variable. When we call `add_one(2 * x)` we first look up what the
variable `add_one` refers to and finds the function. Before we can call
the function, we must evaluate the expression that will be its argument,
that is, we must evaluate `2 * x`. Since we call `add_one` at the
outermost level, the global scope, `x` is the global variable. It refers
to the value two, so `2 * x` is four. We then call `add_one` the
parameter, which is the local variable `x`, will then refer to four.
This does not change the global variable, that variable still refers to
two. When we return `x + 1`, we use the local variable, which refers to
four, so we return five.

You should be comfortable with the difference between global and local
variables by now, but what happens when a function calls itself, as we
did with the factorial function.

``` {.python}
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
```

When we call

``` {.python}
factorial(4)
```

the local variable, `n` will be set to refer to four. There is no
problem there. But then we call `factorial` with `n - 1` to evaluate
`n * factorial(n - 1)`. This makes the local variable refer to three,
but we still need it to refer to four when, after the recursive call, we
multiply the result of `factorial(n - 1)` by `n`. We need the local
variable to refer to both four and three in the recursive case. How is
that achieved?

This is something early programming languages usually couldn't handle.
In these early languages, local variables were tied to functions---each
function had memory locations reserved for their local variables. Those
were modified when calling a function and by updating variables inside
the function body. If you called the same function twice, you would
overwrite the memory locations assigned to the local variables. This
isn't a problem if you do not use recursion, but it apparently is if you
do. You cannot use the same memory location to hold both $n=4$ and
$n=3$.

The solution to this problem is beautiful in its simplicity: instead of
reserving fixed memory locations for local variables for each function,
you reserve memory for the local variables in each function *call*. The
memory locations you need for local variables are not hardwired in the
program but will be allocated when you call a function. This memory is
allocated on a so-called *call stack*, and it works as follows. You have
a piece of your computer's memory set aside for this stack. You keep
track of the top of the stack, and the function call you are currently
executing has access to the top of the stack, and any global variables,
but not the rest of the stack. When you call a function, you reserve
memory for the variables used in the function at the top of the stack.
The memory set aside in this way is known as a function's *call frame*,
but it isn't that important what we call it; what is essential is that
we have it.[^22]

Consider the call:

``` {.python}
factorial(4)
```

If we make this call at the outermost level, the call stack is empty.
When we make the function call, Python puts two things on the call stack
and increases the call stack pointer to point to the top of the stack.
The function will know where to get to the local variables relative to
the top of the stack. Not the direct memory addresses that hold them but
where they can be found below the stack pointer. Knowing the absolute
memory addresses is what early programming languages would do, and it
fails if we need to have more instances of function calls at the same
time. Knowing the offset below the stack pointer instead resolves this
problem.

When we return from a function call, we also need to know where to
return to. A function can be called from different places in your
program, and we need some way of knowing where a function was called
from so we can return to that location in the program. We cannot use a
fixed memory location to hold this information any more than we can use
fixed locations for local variables, so we need put this information on
the stack as well.

When we call recursively, Python will put the information it needs for
each function call---local variables and the return location---onto the
stack and grow it as needed, see [@fig:growing-call-stack].

![Growing the call stack in recursive
calls.](growing-call-stack.pdf){#fig:growing-call-stack}

When we reach $n=1$, we hit a base case and immediately return one as
the result. Now, Python needs to do two things. It needs to provide the
return value of the function to its caller, and it t needs to continue
executing the program from the point where the function call was made.
The caller location is found in the call stack, so we can always
determine where the program needs to jump to. What about the return
value, though?

We hadn't thought about where Python stores result of expressions
before; we just assumed that it could remember them somehow. But of
course, on a computer, you need to store intermediate results of
expressions somewhere. Since results of (local) expressions are local to
a function call, the only appropriate place is on the stack.[^23]

When we return a value from a function, we need to put that value on the
stack. We cannot make assumptions about where our function is called
from so we cannot use the caller's call frame. Instead, what is commonly
done, is to pop the current call frame off the stack, which means we
decrease the stack pointer to where it was before the function call, and
then put the result of the function call just one position above the new
position of the stack pointer. To be able to do this, it needs to
remember the return position if it overwrites that memory location, or
it needs to allocate space on the stack for the return value. Let us
just assume that it is able to return and also put the function
result-value in its call-frame.

Since we write the return value on the call-frame of the function, we do
not muck about in the caller's call frame, and the caller knows where to
get the result. When we return from a recursion, we pop call frames from
the stack, put the return values above the stack (overwriting the call
frame), and keep doing this until we leave the recursion, see
[@fig:shrinking-call-stack].

![Shrinking the call stack when returning from recursive
calls.](shrinking-call-stack.pdf){#fig:shrinking-call-stack}

If the calling function wants to remember the returned value, it needs
to move it somewhere else before it can make further function calls. If
it only calls a function for its side-effects, it can ignore any value
the called function might return, but if it needs to use the result, it
must remember it. If it calls another function, the call frame of this
function will be written on the stack, overwriting the returned value.
We do not call other functions before we have used the result of the
recursive call for `factorial`, but we do multiply a number with the
result of a call. The simplest way to handle this is to save the result
of the recursion and then handle the multiplication as we would handle
any temporary result in an expression. With the factorial function, we
can make the optimisation where we use the returned value direction. We
cannot always do this, however. For example, when computing Fibonacci
numbers, we need to make two recursive calls and then add their returned
values together. We need somewhere to store the result of the first
recursive call so we can add it to the result of the second call. In
general, we might need to store the result of many function calls before
we can use them in a local expression. Everything we need to save for
later, we need to move to a location in the current call frame before we
call another function.

The call stack is not only used for recursion. It works the same way
with all function calls. Consider this program:

``` {.python}
def add_one(x):
    return x + 1

def add_two(x):
    return add_one(add_one(x))

add_two(1)
```

[@Fig:call-stack-add-two] shows the call stack when evaluating this
program. The call to `add_two` will put a return location and the local
variable `x` on the stack. It also allocates space for the temporary
value that it gets from the first call to `add_one` so it can remember
this for the second call. The `add_two` function then calls `add_one`.
This call will put a return location and another `x` on the call stack.
Once the call frame is set up, `add_one` will do its calculations, move
the stack pointer down to where it was before the call, in effect
pop'ing the call frame from the stack, it will put the result of the
function call just above the stack pointer, and then return to whence it
was called.

![Call stack when evaluating
~\`add\_two(1)\`~.](call-stack-add-two.pdf){#fig:call-stack-add-two}

Now, the `add_two` function needs to call `add_one` once more. Since
this call would overwrite the result of the first call, we need to save
this value. We do this by moving the value from just above the stack
pointer to the memory cell we allocated for this very purpose. We can
then set up the call frame for the second call to `add_one`, make this
call, and grab the result. This result is also the result of the
`add_two` call, but we cannot simply use this result. We need to pop the
call frame from the stack, which means we also need to move the
`add_one` result down to where the caller of `add_two` expects to see
it.

This is example does not involve recursive calls, but the principle
behind all function calls is the same. We might be able to optimise a
specific combination of calls. For `add_two` we might manage to avoid
moving the return value of the first call to `add_one` but simply
putting it where it is needed for the second call; or, we might be able
to put the return value from the second call to `add_one` where it is
needed when we return from `add_two`. Such optimisation would only work
for particular combinations of calls, however, while the operations we
did in the example would work for all combinations of functions.

**Exercise:** Draw the call stack for computing the fourth Fibonacci
number using the implementation you did in the previous exercise.

All this call stack business can look complicated, but the good news is
that you never need to worry about it unless you implement recursion
yourself. The call stack is the reason why recursive function calls are
possible, but you only need to know that Python can handle them.

Well, you *almost* never have to worry about the call stack. You might
run into problems with a call stack if you fill it up. For example, if
you do something like this:

``` {.python}
def f(x):
    return f(x + 1)
f(1)
```

This example results in an infinite recursion; the function doesn't even
have a base case. You will not get an infinite recursion if you execute
the code, however, instead you will get an error that says
"RecursionError: maximum recursion depth exceeded". This happens because
the memory set aside for the call stack is limited and if the recursion
gets too deep, there is no more stack available for more call frames.

For infinite recursions, we wouldn't expect something meaningful anyway,
but there are many cases where there *is* a result of a recursion, but
you do not have sufficient stack space. Linear or binary search, if
implemented recursively, could run into this problem if they are called
on sufficiently many elements.

You will not run into this if you use iteration instead of recursion. It
is certainly possible to write an infinite loop, but you will not run
out of stack-space as a result. Loops are also more efficient than
recursive calls because the latter needs to handle call frames while the
former does not. If you can implement an algorithm using iteration just
as easily as you can do with recursion, you should always prefer the
looping version. If you do need recursion, but the recursion is deeper
than your call stack allows, you have no choice but to use a loop. There
are general ways of handling recursion that avoids filling up the call
stack (and we will return to this in \[Chapter
sec:return-to-functions\]), but for some recursive functions, it is
particularly easy. These are *tail-recursive* functions. We get to those
in [@sec:tail-recursion]. First, though, we will consider the
relationship between iteration and recursion in more detail.

Recursion and iteration {#sec:recursion-and-iteration}
-----------------------

There is a close correspondence between recursion and iteration. You can
always, directly, translate a loop into a recursive function; you cannot
necessarily do the opposite. There just are more things you can do with
a stack than you can with a loop. Obviously, you can implement the stack
functionality yourself and then avoid recursive function calls, but this
is just an implementation detail. Conceptually, will still be using
recursion and not a simple loop.

Just because you can implement all loops as recursive function calls
doesn't mean that you should. Besides the problems with exceeding the
stack limit, there is a substantial overhead in calling functions, so a
recursive solution to a problem will always be slower than one that
relies on loops. Programming languages that do not allow loops but only
recursive function calls actually translate recursion into loops under
the hood whenever possible. Python does not do such optimisations of
recursive functions, so you should always prefer loops over recursions
when you can. If you can solve a problem directly using loops, you
should do that. Sometimes, however, it is easier first to derive a
recursive solution to a problem and then translate it into a loop if
possible. Divide and conquer algorithms ([Chapter
@sec:divide-and-conquer]) are more naturally constructed in terms of
recursion, but can still often be implemented using loops.

The purpose of this section is not to convince you that recursion is a
better tool than iteration. If we can implement an algorithm using
loops, then that is the better choice. When we cannot, then recursion is
the only choice. We see examples of this when we discuss divide and
conquer algorithms. The purpose of this section is to get you
familiarised with the relationship between recursion and iteration. In
[@sec:tail-recursion] we consider simple recursive functions that we can
translate into loops. In this section, we will translate looping
functions into recursive ones.

We will take a problem with an iterative solution and translate it into
a recursive one. The result, I hope you will agree, is more
straightforward than the iterative solution. This is why we usually
prefer to develop an algorithm using recursion before we consider
iteration. We do the translation in the opposite direction here. We
start with loops, which you are already familiar, and show you how these
loops can be simplified using recursion. The only reason for this is to
get from something familiar, loops, and see how it relates to something
new, recursion. As a side-effect, I also hope to convince you that
recursive solutions can be much more straightforward than iterative
ones.

The problem we will consider is that of merging two lists. This was an
exercise in [Chapter @sec:algorithmic-efficiency]; if you haven't solved
it already, give it a go before continuing.

The problem we need to solve is this: given two sorted lists, `x` and
`y`, we want to create a list that contains the same elements as in `x`
and `y`, combined, in sorted order.

One implementation could look like this:

``` {.python}
def merge(x, y):
    result = []
    i, j = 0, 0
    while True:
        if i == len(x):
            # no more elements in x
            while j < len(y):
                result.append(y[j])
                j += 1
            return result
        if j == len(y):
            # no more elements in y
            while i < len(x):
                result.append(x[i])
                i += 1
            return result
        if x[i] < y[j]:
            result.append(x[i])
            i += 1
        else:
            result.append(y[j])
            j += 1
```

The function doesn't do anything complicated, but it is rather long. It
can, therefore, be hard to see, at a glance, what it is doing. It is
simple enough: We move through `x` and `y`, using the indices `i` and
`j`, pick the smallest of `x[i]` and `y[j]`, and append that to our
result. If we have made it to the end of either `x` or `y`, the first
two `if`-statements in the loop, we copy the remainder of the other
list.

A much simpler implementation of the same idea is this:

``` {.python}
def merge(x, y):
    if len(x) == 0: return y
    if len(y) == 0: return x
    if x[0] < y[0]:
        return [x[0]] + merge(x[1:], y)
    else:
        return [y[0]] + merge(x, y[1:])
```

Here we can directly see the two base cases and the recursive case---the
recursive case is one of two recursive calls, depending on which list
has the smallest element. The most straightforward recursive solution is
usually *much* simpler than an iterative solution. It is often also a
lot less efficient, even if we ignore the function call overhead.

For reasons that I have not explained yet, slicing to get everything
except the first element of a list, as we do when we call `x[1:]` and
`y[1:]`, is an expensive operation. It takes time proportional to the
length of the lists (minus one). There is another implementation of
lists than the one Python uses, where this would be a constant time
operation, but for Python `list` objects it is not. Therefore, the
recursive call takes time $O(n)$, where the lengths of `x` and `y` are
in $O(n)$, plus how long it might take to compute the recursive
function, and the result is an $O(n^2)$ running time all in all. I won't
go into details about why we get this running time since we cover that
in [Chapter @sec:divide-and-conquer].

The iterative implementation runs in time $O(n)$---if you cannot see why
immediately, try to work through the analysis. The recursive
implementation runs in $O(n^2)$. This isn't a great advertisement for
recursion. We generally do not want to trade efficiency for simplicity.

We can get rid of the expensive slicing of the first elements by
reintroducing the index variables and get this implementation:

``` {.python}
def merge(x, y, i = 0, j = 0):
    if i == len(x): return y[j:]
    if j == len(y): return x[i:]
    if x[i] < y[j]:
        return [x[i]] + merge(x, y, i + 1, j)
    else:
        return [y[j]] + merge(x, y, i, j + 1)
```

Unfortunately, this isn't much better. We avoid the slicing, but
concatenating two lists, as we do in the recursive case, is also an
$O(n)$ operation, so we end up with the same $O(n^2)$ running time.

To avoid both concatenation and slicing, we can do this:

``` {.python}
def merge(x, y, i = 0, j = 0, result = []):
    if i == len(x):
        # no more elements in x
        while j < len(y):
            result.append(y[j])
            j += 1
        return result
    if j == len(y):
        # no more elements in y
        while i < len(x):
            result.append(x[i])
            i += 1
        return result
    if x[i] < y[j]:
        result.append(x[i])
        return merge(x, y, i + 1, j, result)
    else:
        result.append(y[j])
        return merge(x, y, i, j + 1, result)
```

This leaves us pretty much back where we started. We now have a
recursive solution to the problem, but it is just as complex as the
iterative function we started with.

All is not lost, however. We can reconsider why we couldn't use the
simpler recursive solutions. The main problem here was
concatenation---we could avoid the slicing simply by using indices.
Maybe we can avoid the concatenation in some other way? Indeed we can:

``` {.python}
def merge_rec(x, y, i = 0, j = 0):
    if i == len(x): return y[j:]
    if j == len(y): return x[i:]
    if x[i] < y[j]:
        res = merge_rec(x, y, i + 1, j)
        res.append(x[i])
        return res
    else:
        res = merge_rec(x, y, i, j + 1)
        res.append(y[j])
        return res

def merge(x, y):
    return list(reversed(merge_rec(x, y)))
```

Since prepending one element to a list involves a concatenation
operation, which is expensive, we replace it with an append operation,
which is cheap.[^24] We construct the merged list in the reversed order,
so we need to reverse it to get the right order once we are done with
the merge. I have split this into two functions, one that recursively
constructs the reversed result and one that reverses it to get the
result in the right order. In the basis cases we still slice a list, but
since this takes time proportional to the length of the list, it is not
slower than the `while`-loops we used earlier to do the same thing. In
fact, it is likely to be faster since slicing is a built-in operation in
Python and implemented very efficiently.

This solution is not quite as simple as the first recursive function,
but we can make it almost so by moving the append operation to a
function:

``` {.python}
def app(lst, x):
    lst.append(x)
    return lst

def merge_rec(x, y, i = 0, j = 0):
    if i == len(x): return y[j:]
    if j == len(y): return x[i:]
    if x[i] < y[j]:
        return app(merge_rec(x, y, i + 1, j), x[i])
    else:
        return app(merge_rec(x, y, i, j + 1), y[j])
```

This solution is almost as simple as the first recursive function, and
it runs in $O(n)$; we have replaced the expensive operations in the
first recursive function with constant time operations in this function.
It is not as efficient as the iterative function. Function calls are
constant time operations but expensive ones, and we use those
extensively here. We also need to reverse the result, which adds
additional computations. The iterative solution avoids any function call
beyond the call to the `merge` function and directly construct the
result list.

It is the simplicity of the recursive solution, compared to the
iterative version, that makes it easier to construct recursive
algorithms. Once we have a recursive solution, we usually then want to
replace it with an iterative solution. In the next section, we will
start with a recursive solution and use that to guide us to an iterative
solution. Usually, we end up with an implementation very similar to what
we would get if we set out to implement an iterative solution in the
first place, but starting with a recursive solution and then modifying
it, step by step, until we have an efficient iterative solution makes
the programming task more manageable. As an added benefit, it also makes
it easier to test our implementation; we can use the simplest solution
to check the more complicated solutions against (see [Chapter
@sec:testing] for more details on approaches to testing). As we,
stepwise, transform a function to make it more efficient, we can test
each rewrite. Since it is easier to get a simple solution correct, and
since it is easier to make incrementation changes to a working
implementation than it is to construct a function from scratch,
implementing efficient solutions using this approach is a good strategy.
Building an efficient function by a series of changes from a simple to
an efficient one is more often than the most effective way to get a fast
and correct solution to a problem; aiming directly for a sophisticated,
efficient solution is usually not a practical approach.

Before we get to translating recursive functions into iterative ones,
however, you should do some exercises to test that you have understood
recursion.

**Exercise:** To compute the sum of the elements in a list, we can
obviously do this iteratively:

``` {.python}
result = 0
for e in x:
  result += e
```

Implement a recursive function that computes the sum of the elements of
a list.

**Exercise:** We can find the smallest element in a non-empty list, `x`,
like this:

``` {.python}
smallest = x[0]
for e in x:
    smallest = min(smallest, e)
```

s Write a recursive function for finding the smallest element in a list.
To avoid copying the list using slices, you will want to have the
function take an index parameter as an argument.

**Exercise:** Modify your function, so it returns `None` if the list is
empty. The easiest way to do this is probably to include the "smallest
element seen so far" as a parameter to the function, with a default
value of `None`. To compute the smallest value and still handle `None`
you can use this function:

``` {.python}
def my_min(x, y):
    return y if x is None else min(x, y)
```

**Exercise:** Write a recursive function that reverses a list.

**Exercise:** Recall the exercise where you had to translate a base-10
number into some other base $b$ (where we restricted the base to be less
than 16). We can get the last digit of a number $i$, in base $b$ using
this function:

``` {.python}
def get_last_digit(i, b):
    return digits[i % b]
```

where we defined the `digits` list as

``` {.python}
digits = {}

for i in range(0,10):
    digits[i] = str(i)

digits[10] = 'A'
digits[11] = 'B'
digits[12] = 'C'
digits[13] = 'D'
digits[14] = 'E'
digits[15] = 'F'
```

We can then reduce the problem to the second-to-last digit by dividing
$i$ by $b$. Implement this idea using a recursive function.

Tail-calls {#sec:tail-recursion}
----------

You can always translate an iterative algorithm into a recursive one,
but since iterative algorithms are more efficient, you shouldn't do
this. Recursive algorithms are more straightforward, though, so you will
often find yourself in the situation that you have an elegant recursive
solution to a problem, and you want to translate it into a more
efficient iterative solution. You cannot always translate a recursive
function into an iterative one,[^25] but this section is about the cases
where you can.

Functions that can always be translated into loops are so-called
*tail-cakk* functions. In many programming languages, tail-recursive
functions are automatically translated into loops---this is called the
*tail call optimisation*---but Python is not one of them. Not to worry,
though, the translation is so simple that you can always do it by hand
with minimal effort.

A function is *tail-recursive* when the recursive case only consists of
a recursive call. Consider the factorial function:

``` {.python}
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
```

The recursive case involves a recursive call but not as the single
result of the recursive case. We make a recursive call, and then we
multiply the result with `n`. Because we have to multiply the result of
the recursive call with `n`, the function is not tail-recursive. We can
translate it into a tail-recursive function by adding an accumulator to
the function:

``` {.python}
def factorial(n, acc = 1):
    if n == 1:
        return acc
    else:
        return factorial(n - 1, n * acc)
```

The accumulator handles the multiplication with `n`. We multiply the
accumulator by `n` as we go down the recursion rather than multiply the
result of recursive calls by `n` when we return from the recursion.
Functions that only involve a single recursive call in the recursive
case can always be translated into tail-recursive versions by adding an
accumulator.

**Exercise:** Rewrite your recursive function for computing the sum of a
list of numbers such that it becomes tail-recursive.

**Exercise:** Rewrite your recursive function for finding the smallest
element in a list to a version that is tail-recursive.

With tail-recursive functions, we do not need to do anything with the
result of the recursive call. Not doing anything with the result of a
recursive call is just another way of saying that a function is
tail-recursive. The reason that this is important is that, when we do
not need to do anything after the recursive call, then we can reuse the
call frame for the recursive call. We can directly update the local
variables to those we would use in the recursive call frame and go from
there; we can replace a recursive call with a simple update of the
function argument local variables.

When we call a function we assign values to the function arguments. If
we have a tail-recursive function, we can directly update the arguments
we already have and then start executing the function body from the
beginning again. If we wrap the function body in one big `while True`
loop, we can replace the recursive function call with an update to the
function arguments and then `continue` the loop. If the recursive case
is put at the end of the loop, we do not even need to `continue`; we are
at the end of the loop, so we return to the beginning right after we
update the variables.

For the factorial function, this transformation gives us:

``` {.python}
def factorial(n):
    acc = 1
    while True:
        if n == 1:
            return acc
        n, acc = n - 1, n * acc
```

If you split the variable updates over multiple statements, you have to
be careful about the order. When you update a variable, you affect
expressions that depend on it. So you have to update the variables in
the right order.

This will work

``` {.python}
def factorial(n):
    acc = 1
    while True:
        if n == 1:
            return acc
        acc = n * acc
        n = n - 1
```

This will not:

``` {.python}
def factorial(n):
    acc = 1
    while True:
        if n == 1:
            return acc
        n = n - 1
        acc = n * acc
```

A parallel-assignment, as we did for the first iterative implementation
of the factorial function, will usually work. If we never do any
operations with side-effects, i.e., whenever we need to update a data
structure such as a list, we create a new one instead, then
parallel-assignment will work. If we actually modify a data structure,
we cannot use parallel assignment so we must be careful that we perform
the update operations in the same order as they would have been
performed in a function call.

**Exercise:** Do this transformation for your tail-recursive summation
function.

**Exercise:** Do this transformation for your tail-recursive "find
minimum" function.

**Exercise:** Consider our recursive implementation of binary search:

``` {.python}
def bsearch(x, e, low = 0, high = len(x)):
    if low >= high:
        return False
    mid = (low + high) // 2
    if x[mid] == e:
        return True
    elif x[mid] < e:
        return bsearch(x, e, mid + 1, high)
    else:
        return bsearch(x, e, low, mid)
```

This function is tail-recursive, so use the transformation to replace it
with a loop. Compare it to the iterative solution we considered before
this chapter.

To see a more complex case of using an accumulator in a tail-recursive
function, and then translate it into an iterative function, we can
return to the problem of merging two lists. We left this problem with
this recursive implementation:

``` {.python}
def app(lst, x):
    lst.append(x)
    return lst

def merge_rec(x, y, i = 0, j = 0):
    if i == len(x): return y[j:]
    if j == len(y): return x[i:]
    if x[i] < y[j]:
        return app(merge_rec(x, y, i + 1, j), x[i])
    else:
        return app(merge_rec(x, y, i, j + 1), y[j])

def merge(x, y):
    return list(reversed(merge_rec(x, y)))
```

The reason we had to construct the merged list in reverse order, and
then reverse it when we are done, was actually because we didn't use an
accumulator. If we add an accumulator, we can build the merged list in
the right order:

``` {.python}
def merge(x, y, i = 0, j = 0, acc = None):
    if acc is None:
        acc = []
    if i == len(x): return acc + y[j:]
    if j == len(y): return acc + x[i:]
    if x[i] < y[j]:
        return merge(x, y, i + 1, j, app(acc, x[i]))
    else:
        return merge(x, y, i, j + 1, app(acc, y[j]))
```

The way we handle the default value of the accumulator might look a bit
weird, but it is crucial. If we set the default value of `acc` to an
empty list, each call to `merge` that rely on the default parameter will
get the *same* list. This means that if you call `merge` twice, the
result of the first call will still be in the accumulator, and the new
merge will be appended to it. This is not what we want, and it is
because of this that we handle the default parameter the way we
do.[^26].

This function is tail-recursive so we can translate it into a looping
version. The `app` function simply append its second argument to its
first, and it does this before the recursive call (because function
arguments are evaluated before a function is called). Because of this,
we can get rid of it and simply append instead. We have to be careful to
append before we update the indices, though. The rewritten function
looks like this:

``` {.python}
def merge(x, y, i = 0, j = 0, acc = None):
    if acc is None:
        acc = []
    while True:
        if i == len(x): return acc + y[j:]
        if j == len(y): return acc + x[i:]
        if x[i] < y[j]:
            acc.append(x[i])
            i += 1
        else:
            acc.append(y[j])
            j += 1
```

If you want to avoid copying the accumulator in the base cases, you can
use the `extend` method on the accumulator list. Using `extend` and a
slice on one of the input lists is unlikely to be slower than a
`while`-loop where we move individual elements, since `extend` and slice
are builtin operations and therefore highly optimised.

``` {.python}
def merge(x, y, i = 0, j = 0, acc = None):
    if acc is None:
        acc = []
    while True:
        if i == len(x):
            acc.extend(y[j:])
            return acc
        if j == len(y):
            acc.extend(x[i:])
            return acc
        if x[i] < y[j]:
            acc.append(x[i])
            i += 1
        else:
            acc.append(y[j])
            j += 1
```

If in the first iterative solution, we used the expend method as well,
we would have this solution. So, we end up back where we started.
Hopefully, we have learned something along the way.

Computer architecture {#sec:architecture}
---------------------

APPLICATIONS ON TOP OF HARDWARE AND VIRTUAL MACHINES

Higher order functions and closures
===================================

Trampolines {#sec:trampolines}
-----------

Functional programming
----------------------

Divide and conquer and dynamic programming {#sec:divide-and-conquer}
==========================================

Divide and conquer is the algorithmic version of recursion. The term
comes from the political doctrine *divide et impera*, but for
algorithms, a more correct description would be *divide and combine*.
The key idea is to

1.  Split a problem into subproblems of the same type.
2.  Recursively solve these problems.
3.  Combine the results of the recursive calls to a solution of the
    original problem.

Step one and three can be very simple or very complex, while step two is
usually one or two recursive calls.

The binary search algorithm that we have seen several times by now is an
example of a divide and conquer algorithm. Step one in the algorithm is
identifying whether we should search to the left or to the right of the
midpoint, the recursive step (step two) is searching in one of these
intervals. Step three is almost non-existing since we just return the
result of the recursive solution.

The recursive step(s) in divide and conquer algorithms are often
implemented as recursive function calls, but need not be. Conceptually,
we recurse, but as we saw in binary search, we can replace recursive
calls with loops. It is not necessary to use recursion in your
implementation of a divide and conquer algorithm; the defining component
of this class of algorithms is that we solve a subproblem of the same
type as the original problem. Since we are using recursion, even if it
is only conceptually, we need to have basis cases and recursive cases.
The basis case in binary search is when we have an empty interval or
when the midpoint is the element we are looking for. The recursive case
handles everything else.

As another example of divide and conquer, we can consider a sorting
algorithm known as *merge sort*. This algorithm works as follows:

1.  Split the initial input into two pieces of half the size of the
    original problem: the first and the second half of the input list.
2.  Sort these two smaller lists recursively.
3.  Combine the two sorted lists using merge.

The algorithm involves two recursive subproblems, so it is not easy to
implement it as an iterative solution. We will, therefore, deal with it
recursively. The basis cases for the recursion are when we have empty
lists or lists of length one---these will be lists that are already
sorted. The recursive case handles everything else.

A straightforward implementation of this could look as follows:

``` {.python}
def merge_sort(x):
    if len(x) <= 1: return x
    mid = len(x) // 2
    return merge(merge_sort(x[:mid]), merge_sort(x[mid:]))
```

The function performs what we identified as the three steps of merge
sort should in the most straightforward manner, but you might be
uncomfortable with the slicing we do to split the input `x`. For
`merge`, as we saw in [@sec:recursion-and-iteration] using this form of
slicing increased the running time from $O(n)$ to $O(n^2)$. It is not
quite as bad in this algorithm since the linear time slice operation is
slower than the time it takes to sort the sub-lists---we discuss the
running time shortly, but it will be $O(n\log n)$. Still, we could avoid
it by using indices into `x` instead:

``` {.python}
def merge_sort_rec(x, low, high):
    if high - low <= 1: return x[low:high]
    mid = (low + high) // 2
    return merge(merge_sort_rec(x, low, mid), 
                 merge_sort_rec(x, mid, high))

def merge_sort(x):
    return merge_sort_rec(x, 0, len(x))
```

I have implemented this using two separate functions, one that handles
the actual sorting but takes indices as arguments, and one that only
takes `x` as its argument and calls the former. We cannot set `low` and
`high` as default arguments, since `high` should be set to the length of
`x`, and we do not know what `x` is until we call the function (recall
that the default arguments of a function must be known when we *define*
the function, not when we call it). We could use the trick of setting
them to `None` and then check if they are that, as we did `merge`, but
then we would need to check the arguments in each recursive call. This
wasn't a problem when we translated `merge` into an iterative algorithm,
but we cannot do this with `merge_sort` since it is not tail recursive.
Therefore, I prefer to split the algorithm into two functions.

We still slice `x` when the interval is one or zero, and we still need
to concatenate two lists when we merge. We can also avoid this by doing
the sorting in-place. For this we need an in-place merge. Doing this was
an exercise earlier in the book, but a recursive solution could look
like this:

``` {.python}
def inplace_merge(x, i, j, k, l):
    # invariant: i <= j <= k <= l
    if i == j or k == l: return # nothing left to be done
    if x[i] < x[k]:
        inplace_merge(x, i + 1, j, k, l)
    else:
        x[i], x[k] = x[k], x[i]
        inplace_merge(x, i + 1, j, k, l)
```

Since this is a tail recursive function, we can transform it into an
iterative algorithm in the straightforward way:

``` {.python}
def inplace_merge(x, i, j, k, l):
    while True:
        # invariant: i <= j <= k <= l
        if i == j or k == l: return # nothing left to be done
        if x[i] < x[k]:
            i += 1
        else:
            x[i], x[k] = x[k], x[i]
            i += 1
```

With the in-place merge we can implement an in-place merge sort like
this:

``` {.python}
def merge_sort_rec(x, low, high):
    if high - low <= 1: return
    mid = (low + high) // 2
    merge_sort_rec(x, low, mid)
    merge_sort_rec(x, mid, high)
    inplace_merge(x, low, mid, mid, high)
    
def merge_sort(x):
    merge_sort_rec(x, 0, len(x))
```

Divide and conquer running times
--------------------------------

Figuring out the running time for recursive functions---or algorithms
that are recursive even if they are not implemented as recursive
functions---means solving recurrence equations. If $T(n)$ denotes the
running time on an input of size $n$, then a recurrence equation could
look like this:

$$T(n) = 2\cdot T(n/2) + O(n)$$

This is the recurrence equation for merge sort. To sort a list of length
$n$ we solve two problems of half the size, $2T(n/2)$, and do some
additional work in time $O(n)$. In the first version of merge sort,
where we sliced the input, we used linear time both for the slicing and
then for the merge; in the final version, we only spend linear time
doing the merge. In either case, we spend linear time in addition to the
recursive calls.

What characterises recurrence equations is similar to what defines
recursive solutions to problems. The equations refer to themselves.
Strictly speaking, we need basis cases for the recurrence equations to
be well defined so we would have

$$T(n) = \begin{cases}
 O(1) & n \leq 1 \\
 2\cdot T(n/2) + O(n) & \text{otherwise}
\end{cases}$$

but when we consider the running time of an algorithm, the basis cases
almost always involve constant time, so we often leave that out.

You can solve such recurrence equations by expanding them:

\begin{align*}
    T(n) &= O(n) + 2\cdot T(n/2) \\
       &= O(n) + 2\left[
            O(n/2) + 2\cdot T(n/4)
       \right] \\
       &= O(n) + 2\left[
            O(n/2) + 2\cdot \left[
                O(n/4) + T(n/8)
            \right]
       \right] \\
       &= \ldots
\end{align*}

You have to be a little careful with the expansion and big-Oh notation,
here. We see that we get a $O(n/2)$ in the first expansion, and normally
we would consider this equal to $O(n)$. It is, but as we keep expanding,
we see the series $O(n)+O(n/2)+O(n/4)+\cdot+O(n/n)$. If we pretend that
all the $O(n/2^k)$ components are $O(n)$ this would give us
$n\times O(n)=O(n^2)$. This *is* an upper bound on the expression, but
it is not really tight. If you multiply into the parentheses in the
equation, you will also get

$$2\left[O(n/2) + 2\cdot T(n/4)\right] = 2 O(n/2) + 4 T(n/4) = O(n) + 4 T(n/4)$$

which is actually okay, but if you translated $O(n/2)$ into $O(n)$, you
would get

$$T(n) = 2O(n) + 4O(n) + 8O(n) + 16\cdot T(n/8)$$

where each of the $O(n)$ components are multiplied by a number $2^k$.
You can consider that a constant in each step, but $k$ depends on $n$,
so it isn't really a constant. Neither is the number we divide $n$ by
inside the big-Oh.

The problem here is that we blindly translate the expanded numbers
$2 O(n/2)$ into $O(n)$ are do not take into account that, as we continue
the expansion, the number we multiply with and the number we divide by,
changes for each expansion. They depend on $n$ in how many times we do
this and what the numbers are in each step. They are not constants. The
arithmetic rules we have learned for the big-Oh notation are correct;
the problem is not that. The problem is that we consider the numbers in
the expansion as constants when they are not. This is usually not a trap
you will fall into when reasoning about iterative algorithms as we have
done earlier, but it is easy to fall into here.

When expanding a recurrence equation, it is easier to translate $O(n)$
into $cn$ for some constant $c$. We know such a constant exists such
that $cn$ is an upper bound for whatever the $O(n)$ is capturing. Then
we get an expansion like this:

\begin{align*}
    T(n) &= cn + 2\cdot T(n/2) \\
       &= cn + 2\left[
           cn/2 + 2\cdot T(n/4)
       \right] \\
       &= cn + 2\left[
           cn/2 + 2\left[cn/4) + 2\cdot T(n/8)
           \right]
       \right]\\
       &= \ldots
\end{align*}

If we take this expansion all the way down, we get

$$T(n)=\sum_{k=0}^{\log n} c\cdot 2^k n / 2^k =\sum_{k=0}^{\log n} c\cdot n = c\cdot n\log n$$

where $\log n$ is the base-two logarithm, and we get that limit because
$2^{\log n}=n$ is when we reach $n/n=1$. This means that this recurrence
is in $O(n\log n)$, so this is the big-Oh running time for merge sort.

Usually, you can solve recurrence equations just by expanding them and
recognising the form of the sum you get back from it. This often takes
the form of a series, and if you know what it converges to, you are
done. Almost all the divide and conquer algorithms you will run into are
in one of the forms listed below, though, so I find it easier just to
remember these.

#### Case 1:

$$T(n) = 2\cdot T(n/2) + O(n) \in O(n\log n)$$

We just saw an example of this. Whenever you can break a problem into
two subproblems of half the length as the original, and you do not spend
more than linear time splitting or combining, you get a $O(n\log n)$
algorithm. The merge sort is one such algorithm. This is also the first
comparison-based sorting algorithm we have seen that runs in this time,
and it can be shown to be optimal (in the sense of big-Oh) because all
comparison-based sorting algorithms need to do $\Omega(n\log n)$
comparisons. We see more optimal comparison-based sorting algorithms in
[Chapter @sec:return-to-sorting].

#### Case 2:

$$T(n) = T(n-1) + O(1) \in O(n)$$

If we, in constant time, remove one from the problem size we have an
algorithm that runs in linear time. If we consider linear search a
recursive problem---the basis case is when we find the element, or we
are at the end of the list, and the recursive case is doing a linear
search on the rest of the input---then that would be an example of such
an algorithm.

#### Case 3:

$$T(n) = T(n-1) + O(n) \in O(n^2)$$

If we need linear time to reduce the problem size by one, then we get a
quadratic time algorithm. Selection sort, where we find the smallest
element in the input, in linear time, swap it to the first element, and
then recursively sort the rest of the list is an example of this.

#### Case 4:

$$T(n) = T(n/2) + O(1) \in O(\log n)$$

If you can reduce the problem to half its size in constant time, then
you have a linear time algorithm. Binary search is an example of this.

#### Case 5:

$$T(n) = T(n/2) + O(n) \in O(n)$$

If you can reduce the problem to half its size in linear time, and get
the solution for the full problem after the recursive computation in
linear time as well, then you have a linear time algorithm. Notice that
this equation is different from the one we had for merge sort; in that
recursion, we needed *two* recursive calls, in this we only need one.

As an example of this running time, consider a function that adds a list
of numbers by first adding them pairwise and then adding all the
pairwise sums in a recursive call:

``` {.python}
def binary_sum(x):
    if len(x) == 0: return 0
    if len(x) == 1: return x[0]

    # O(n) work
    y = []
    for i in range(1, len(x), 2):
        y.append(x[i - 1] + x[i])
    if i + 1 < len(x): # handle odd lengths
        y[0] += x[i + 1]
    
    return binary_sum(y) # recurse on n//2 size
```

This looks like just a complicated way of adding numbers---and in some
ways it is---but it can be relevant if you need to compute the sum of
floating point numbers (see the last section of this chapter). When you
add two floating point numbers, you might not end up with their sum. If
this surprises you, remember that a number must be represented in finite
computer memory, but not all real numbers can. For example, the decimal
representation of $1/3$ requires infinitely many decimals,
$0.333333\ldots$. In your computer, you do not use decimal notation but
binary, but the problem is the same. (You can, of course, represent
rational numbers like $1/3$ as two integers, and you can represent
arbitrarily large integers, but there are more real numbers than
rational numbers).

If you add two floating point numbers, you will lose bits of information
proportional to how many orders of magnitude the numbers are apart, so
the greater the difference, the less precise your addition is. If you
add the numbers in a long list, starting from the left and moving right,
as we have done many times before, then this can become a problem. The
accumulator will grow and grow as we add more and more numbers, and if
the numbers in the list are of roughly the same order of magnitude, the
accumulator might end up many orders of magnitude larger than the next
number to be added. If the difference gets large enough, adding a number
to the accumulator results in just the value of the accumulator.

If you start with numbers of the same order of magnitude, then adding
them pairwise as in the algorithm above, will keep them at roughly the
same order of magnitude in the recursion, and this will alleviate the
problem of losing precision in floating point numbers.

#### Case 6:

$$T(n) = 2\cdot T(n/2) + O(1) \in O(n)$$

If we can split and combine in constant time but require two recursive
calls on half the size, we also get a linear time algorithm. Again,
notice that this is different from the recurrence equation for merge
sort where we needed linear time to merge the results of the two
recursive calls.

An example of an algorithm that has this recurrence consider the problem
of finding the largest difference between any two numbers in a list. You
could, of course, run through all pairs and find the largest, but that
would take time $O(n^2)$. Instead, you can solve a slightly harder
problem and get the solution from there---whereby "harder" I mean that
it solves more than just finding the maximum difference; I do not mean
that this is a harder complexity class. We can actually solve this
problem in linear time using a divide and conquer algorithm with the
recurrence above.

The problem we will solve is to find the smallest and the largest number
in a list as well as the largest difference. We do this recursively. We
split the input into two halves, find the smallest and largest elements
in both halves, as well as the largest difference in the two halves. We
can then combine these. The smallest element for the full list is the
smallest of the smallest in either half. The largest element is the
maximum of the two we got from the recursive calls. The largest
difference in the full list is either found in one of the two halves, or
we can get it as the difference between the largest element in one half
and the smallest in the other. We can implement the entire algorithm
like this:

``` {.python}
def min_max_maxdiff(x, i, j):
    # Invariant: j > i
    if i + 1 == j:
        return x[i], x[i], 0
    else:
        mid = (i + j) // 2
        min_l, max_l, maxdiff_l = min_max_maxdiff(x, i, mid)
        min_r, max_r, maxdiff_r = min_max_maxdiff(x, mid, j)
        min_res = min(min_l, min_r)
        max_res = max(max_l, max_r)
        maxdiff_res = max(maxdiff_l, maxdiff_r,
                          max_r - min_l, max_l - min_r)
        return min_res, max_res, maxdiff_res
```

If we only want the maximum difference, we can wrap the function:

``` {.python}
def maxdiff(x):
    if len(x) == 0: return None
    _, _, md = min_max_maxdiff(x, 0, len(x))
    return md
```

Splitting the data and combining the results from the recursive calls
can be done in constant time and we make two recursive calls of half the
size, so by the recurrence equation above, the running time is $O(n)$.

Dynamic programming
-------------------

By now, We have seen how recursion is a powerful tool for both
programming and algorithmic design, i.e., divide and conquer. But you
will not be surprised to learn that not all recursive programs are
efficient. For some recursive functions there is not much we can do
about that but for others

Consider the recursive function for computing the $n$'th Fibonacci
number

$$
F(n) = \begin{cases}
1 & n=1 \,\mathrm{or}\, n=0 \\
F(n-1) + f(n-2) & n > 1
\end{cases}
$$

To compute $F(5)$ you must compute $F(4)$ and $F(3)$. To $F(4)$ you must
compute $F(3)$ and $F(2)$, for $F(3)$ you must compute $F(2)$ and so on,
see [@fig:fib-recursive] where I have marked the base cases with
check-marks and the recursive cases with which recursive calls they
make. The structure of the graph of recursive calls leads clearly leads
to an explosion in the number of calls as $n$ increases, see
[@fig:fib-recursive-calls-count]. That makes this recursive calculation
an unfeasible approach for computing $F(n)$ for large $n$.

![The graph of recursions necessary to compute the 5'th Fibonacci
number.](Recursive.pdf){#fig:fib-recursive}

![The number of recursive calls made when evaluating the Fibonacci
function.](fib.pdf){#fig:fib-recursive-calls-count}

If we could store the values of each function, illustrated
in[@fig:fib-memorisation], we would get a linear time algorithm
([@fig:fib-memo-count]). This only requires a table to store results in
and to look up values in.

![The recursivion graph for computing the 5'th Fibonacci number if we
remember the problems we have already
solved](Memorisation.pdf){#fig:fib-memorisation}

![Number of recursions for increasing
$n$.](fib-memo.pdf){#fig:fib-memo-count}

``` {.python}
def fib(n):
    tbl = {}
    if n <= 1:
        return 1
    else:
        if n not in tbl:
            tbl[n] = fib(n - 1) + fib(n - 2)
        return tbl[n]
```

The $F(n)$ function is simple; we always know exactly which recursions
we need and the sequence of recursions we need. This lets us turn the
calculations around and start at the base cases and build
$F(i)=F(i-1)+F(i-2)$ from 0 and up to $n$, see [@fig:fib-iteratively].

![The graph for computing the 5'th Fibonacci number
iteratively.](iteratively.pdf){#fig:fib-iteratively}

With two variables, representing $F(i-2)$ and $F(i-1)$, the iterative
function look like this:

``` {.python}
def fib(n):
    if n <= 1:
        return 1
    fi1, fi2 = 1, 1
    for i in range(n - 1):
        fi1, fi2 = fi1 + fi2, fi1
    return fi1
```

The iterative function is faster than the recursion function with a
table, even both take linear time. The iterative function avoids using a
table---which has a small overhead---and avoid function calls---with a
larger overhead.

Dynamic programming is the straightforward idea that you should only
calculate each value once. When we compute a value recursively and store
values in a table, then we call it *memorisation* or *top-down* dynamic
programming. When we build our way up from base cases to the one we want
we call it *bottom-up* dynamic programming. I personally think that the
term memorisation is more informative about what an implementation
actually does, so I will use memorisation rather than top-down dynamic
programming. I will refer to button-up dynamic programming as dynamic
programming .

For dynamic programming and memorisation to work you need a problem that
you can split into subproblems that you can then solve independently. In
that way it matches the requirements for divide and conquer algorithms.
For dynamic programming to give you any speedup you also need the
recursions to overlap, i.e., during the computation your algorithm
should solve the same instance of a subproblem multiple times. With
dynamic programming we make sure to only solve each instance of a
subproblem once---after that we can look it up in a table when we need
it. If all subproblems are unique then we do not gain anything from
dynamic programming. If the subproblems are only solved once we are in
the domain of divide and conquer (notice that in the divide and conquer
algorithms above we only solved each subproblem once). Frequently
dynamic programming algorithms are recursive problems that would take
exponential time if we implemented them naïvely but where we have a
polynomial solution using dynamic programming or memorisation.

Representing floating point numbers
-----------------------------------

Floating point numbers, the computer analogue to real numbers, can be
represented in different ways, but they are all variations of the
informal presentation I give in this section. If you are not
particularly interested in how these numbers are represented, you can
safely skip this section. You can already return to it if you think you
are getting weird behaviour when working with floating point numbers.

The representation used by modern computers is standardised as IEEE 754.
It fundamentally represents numbers as explained below, but with some
tweaks that let you represent plus and minus infinity, "not a number"
(NaN), and with higher precision for numbers close to zero than the
presentation here would allow. It also uses a sign bit for the
coefficient while it represents the exponent as a signed integer for
reasons lost deep in numerical analysis. All that you need to know is
that floating point numbers work roughly as I have explained here, but
with lots of technical complications. If you find yourself a heavy user
of floating point numbers, you will need to study numerical analysis
beyond what we can cover in this book, and you can worry about the
details of number representations there.

Floating point numbers are similar to the *scientific notation* for
base-$b$ numbers, where numbers are represented as

$$x = \pm a\times b^{\pm q}$$

where $a = a_1.a_2a_3\ldots a_n, a_i\in\{0,1,\ldots,b-1\}$ is the
*coefficient* and $q = q_1q_2q_3\ldots q_m, q_i\in\{0,1,\ldots,b-1\}$ is
the *exponent* of the number. To get a binary notation, replace $b$ by
$2$. For non-zero numbers, $a_1$ must be 1, so we do not represent it
explicitly, which gives us one more bit to work with. Not all real
numbers can be represented with this notation if we require that both
$a$ are $q$ are finite sequences,[^27] but if we allow them to be
infinite we can. We can approximate any number arbitrarily close by
using sufficiently long sequences numbers of digits; $n$ for the
coefficient and $m$ for the exponent. We usually assume that if
$x\neq 0$ then $a_1\neq 0$ since, if $a_1 = 0$ we can update $a$ to
$a_2.a_3\ldots a_n$ and decrease $q$ by one if positive or increase it
by one of positive.

Where floating point numbers differ from the real numbers is that we
have a fixed limit on how many digits we have available for the
coefficient and the exponent. To represent any real number, we can
choose sufficiently high values for $n$ and $m$, but with floating point
numbers there is a fixed number of digits for $a$ and $b$. You cannot
approximate all numbers arbitrarily close. For example, with $b=2$ and
$n=m=1$, we have $\pm a\in\{-1,0,1\}, \pm q\in\{-1,0,1\}$, so we can
only represent the numbers $\{-1, -1/2, 0, 1/2, 1\}$:
$\pm 1/2 = \pm 1\times 2^{-1}$, $\pm 0 = \pm 0\times 2^q$, and
$\pm 1 = \pm 1\times 2^{\pm 0}$ (where $\pm 0$ might be represented as
two different numbers, signed and unsigned zero, or as a single unsigned
zero, depending on the details of the representation). If we use two
bits for the exponent, we get the number line shown in
[@fig:number-line].

![Number line when we have one bit for the coefficient and two bits for
the exponent.](number-line.pdf){#fig:number-line}

As a rule of thumb, floating point numbers have the property that is
illustrated in [@fig:number-line]. The numbers are closer together when
you get closer to zero and further apart when their magnitude increase.
There is a positive and a negative minimal number; you cannot get closer
than those to zero except by being zero. If you need to represent a
non-zero number of magnitude less than this, we say that you have an
*underflow* error. There are also a smallest and a largest number (the
positive and negative numbers furthest from zero). If you need to
represent numbers of magnitude larger than these, we say you have an
*overflow* error.

There isn't really much you can do about underflow and overflow problems
except to try to avoid them. Translating numbers into their logarithm is
often a viable approach if you only multiply numbers, but can be tricky
if you also need to add them.

In the binary sum example from earlier, the problem is not underflow or
overflow, but rather losing significant bits when adding numbers. The
problem there is the fixed number of bits set aside for the coefficient.
If you want to add two numbers of different magnitude, i.e. their
exponents are different, then you first have to make the exponents
equal, which you can do by moving the decimal point. Consider
$1.01101\times 2^{3}$ to $1.11010\times 2^0$---where we have five bits
for the coefficients (plus one that is always 1, i.e. $n=6$). If you
want to add $1.01101\times 2^{3}$ to $1.11010\times 2^0$ you have to
move the decimal point in one of them. With the representation we have
for the coefficients, $a=a_1.a_2\ldots a_n$, we can only have one digit
before the decimal point so we cannot translate $1.01101\times 2^3$ into
$1011.01\times 2^0$, so we have to translate $1.11010\times 2^0$ into
$0.00111010\times 2^3$. We want the most significant bit to be one, of
course, but we make this representation for the purpose of addition;
once we have added the numbers, we put it in a form where the most
significant bit in the coefficient is one. The problem with addition is
that we cannot represent $0.00111010\times 2^3$ if we only have five
bits in the coefficient. We have five bits because our numbers are six
bits long and the first one must always be one. So we have to round the
number off and get $0.00111\times 2^3$. The difference in the sum is
$2^{-4} = 0.0625$, so not a large difference in the final result, but we
have lost three bits of accuracy from the smaller number.

    1.01101    * 2**3 +
    1.11010    * 2**0 =
    1.01101    * 2**3 +
    0.00111010 * 2**3 =
    1.01101    * 2**3 +
    0.00111010 * 2**3 =
    1.10100010 * 2**3 !=
    1.01101    * 2**3 +
    0.00111    * 2**3 =
    1.10100    * 2**3

In general, you expect to lose bits equal to the difference in the
exponents of the numbers. The actual loss depends on the details of the
representation, but as a rule of thumb, this is what you will lose.

Assume we have one informative bit for the coefficient ($n=2$) and two
for the exponent, ($m=2$), and we wanted to add six ones together
$6\times 1.0_2 \times 2^0 = 1.1_2\times 2^2$. Adding the numbers one at
a time we get:

    1.0 * 2**0 +
    1.0 * 2**0 = 1.0 * 2**1 +
    1.0 * 2**0 = 0.1 * 2**1 = 1.1 * 2**1 +
    1.0 * 2**0              = 0.1 * 2**1 = 1.0 * 2**2 +
    1.0 * 2**0                           = 0.0 * 2**2 = 1.0 * 2**2 +
    1.0 * 2**0                                        = 0.0 * 2**2 = 1.0 * 2**2

which is off by 2. If we add the numbers as we did with our `binary_sum`
function, we instead have

    1.0 * 2**0 +
    1.0 * 2**0 = 1.0 * 2**1 +
    1.0 * 2**0 + 
    1.0 * 2**0 = 1.0 * 2**1 = 1.0 * 2**2 +
    1.0 * 2**0 +
    1.0 * 2**0 = 1.0 * 2**1 = 0.1 * 2**2 = 1.1 * 2**2

which is correct.

Obviously, the floating point numbers you use in Python have a much
higher precision than one bit per coefficient and two per exponent so
you will not run into problems with accuracy as fast as in this example.
The principle, is the same, however. If you add enough numbers, you risk
that the accumulator becomes too large for the addition with the next
number to have an effect. If you run into this, then adding the numbers
pairwise as in `binary_sum` can alleviate this.

Data structures, interfaces, classes and objects
================================================

Implementing dynamic dispatch and the cost of it
================================================

Class hierarchies and inheritance
=================================

Object oriented programming
===========================

Stacks
======

Parsers
-------

We now leave data structures for for the rest of the chapter and look at
a fundamental problem: parsing. That is the process of taking a flat
text format, describing for example some data or a program, and
translate it into data that your program can use. Parsing does not
always involve a stack, but it usually does.

Conclusions
===========

Well, that's it. You have reached the end of the book. But I hope you
haven't reached the end of your programming and algorithmic career.

The techniques we have covered in this book should give you a better
understanding of how a computer stores and manipulate data, and how
different choices in how you implement this will affect the performance
of programs you write. We have used Python to implement the algorithms
we have explored, but the techniques are general. Built in data
structures will vary between different programming languages, and
different software libraries will provide alternative algorithms and
data structures, but you should now be able to understand the tradeoffs
when choosing between alternatives.

Most commonly used algorithms and data structures will be available in
any high-level programming language environment, so you will rarely need
to implement them yourself. Knowing the pros of cons of different
choices, however, is essential for using your programming environment
effectively, and this knowledge is likely to be the most important
lessons you can take from this book. When you cannot use algorithms and
data structures readily available in your programming environment, you
now also have the skills to adapt them to your needs, and when
necessary, to implement alternatives that better suits your needs.

Python is a very high-level programming language, and it has many
powerful features that makes programming in it more effective. I have
not used those constructions in this book, where they are not strictly
needed, so what you have learned here can most likely be directly
translated to other programming languages, if needed. That being said,
different programming languages have idiomatic ways of solving problems.
If you learn a new programming language, it is worthwhile to learn these
idioms. You shouldn't simply use the constructions from Python in a
different language. If you simply use the language constructions you
know from Python, you can write programs in other languages, but you
will be using only the subset of constructions common to both Python and
other languages, and that is not the most effective approach. It is
always worthwhile to know the idioms in the language you are using.
Since this book is primarily about computing and algorithmic thinking, I
have used the simplest constructions in Python that will get the job
done, but if you want to become an effective Python programmer, you
should spend some time learning the more advanced features you have in
the language. Likewise, if you want to be an effective R or Ruby
programmer, you should learn the idiomatic ways of solving problems in
those languages. The computational issues you need to deal with,
however, will be the same.

Python is not a particular fast language, by which I mean that Python
programs are likely to run slower than similar programs in more
low-level languages. As a general rule of thumb, this is usually the
case; programs written in a high-level language are likely to run slower
than programs written in a low-level language. This isn't always the
case, and depends strongly on the interpreter or compiler you use, but
is often the case. If you want complete control of how your programs are
executed so you can get the utmost performance out of your computer, you
will need to program in a very low-level language---close to the iron,
as we say. This, however, is usually not an effective way to solve
problems. Programs written in a low-level language might run faster, but
it comes at a cost in programmer time---programs written in a high-level
language are much faster to write. There is always a trade-off between
programmer efficiency and program efficiency, and optimising at a low
level is rarely worth the effort. Sometimes it is worthwhile to optimise
key hotspots in a program by rewriting those parts in a lower level
language, but choosing the right algorithms and the right data
structures is much more important. A low-level implementation of a slow
algorithm is always going to be outperformed by a smarter algorithm
implemented in a high-level language when you work with large data. You
now have the skills to evaluate algorithms and to choose the best for
your tasks. That is much more important than the skills to program in a
low-level language.

Where to go from here
---------------------

After reading this book, you should be familiar with basic programming,
you should be able to construct and reason about algorithms, and have
some understanding of how a computer represents and manipulate data.
These are the cornerstones of writing efficient programs and effectively
analyse data. There is much more to learn to use computers and Python
optimally, however.

The next step you should take in becoming a better programmer or data
scientist depends on what you wish to achieve in your future use of
Python. If you have gotten a taste for programming and want to start
developing software, you should pick up some books on Python
programming. I have only covered the aspects of Python that I needed to
teach you about algorithms and data structures. There are many features
in Python aimed at making your programming more effective or aimed at
making your software more reusable. At the very least, you should learn
about object-oriented programming and how classes and objects can be
used to develop software that can be extended to solve many more
problems than it was originally developed for.

If your aim is to get into heavy-duty scientific programming, you will
need to study some numerical analysis, so you understand the issues you
might run into when working with floating point numbers. You will also
want to get familiar with working with linear algebra and possibly
tensors. Your next step should almost certainly be to get familiar with
`numpy` and `scipy`.

If you would rather learn more about data science in Python, your next
step should be learning about the `pandas` package. This is a Python
package for manipulating and analysing structured data of the kind you
will usually run into in data analysis projects.

If you want to get into machine learning, then `scikit-learn` and
`tensorflow` are good places to start. After that, you might want to
study the `keras` package, which is a very efficient implementation of
*deep-learning neural networks*, a technology used in many high-profile
artificial intelligence projects.

If you are more interested in learning more about algorithms and
computational complexity, you should instead find some text books on
those topics. There are many good ones that covers topics beyond what we
have covered in this book, but they are typically not based on Python.
Most general algorithmic books are language agnostic and use pseudocode
instead of real programming languages.

There are many places to go from here, and those are some of the
directions you might want to go in if you want to learn more about
computing and Python.

I will just end the book by wishing you good luck, and if you have found
the book useful, I would love to hear from you.

[^1]: There are exceptions to the requirement that an algorithm should
    always complete in a finite number of steps. When we implement
    something like a web service or an operating system, we don't want
    our programs to terminate after a finite number of calculations, but
    instead want them to run, and be responsive, indefinitely. In those
    cases, we relax the requirement and require that they can respond to
    all events in a finite number of steps. We also have exceptions to
    always getting correct answers. Sometimes, we can accept that we get
    the right answer with high probability---if we can quickly test if
    the answer is correct and maybe rerun the algorithm for another
    solution, and continue this until we get lucky. These are unusual
    cases, however, and we do not consider them in this book.

[^2]: Ok, at a more fundamental level, a computer is a rock you can
    communicate with through electricity, but from a computational
    perspective, basic arithmetic operations are as primitive as they
    come.

[^3]: If you think about it, there is an interesting question on how
    programs that translate high-level instructions into low-level
    instructions are written. It is hard enough to write a program that
    works correctly in a high-level programming language; it is
    substantially harder to do in the language the machine understands.
    You want to write the programs for dealing with high-level
    abstractions in programming languages that support these
    abstractions. But to support the abstractions, you need a program
    that implements them. That is a circular dependency, and that is
    problematic. You can solve it by first writing primitive programs
    that support some abstractions. Now you can use these abstractions
    to write a *better* program that can handle more abstractions. This,
    in turn, lets you write even better programs with better
    abstractions. At this point, you can throw away the most primitive
    programs because you have implemented a programming language that
    you can use to implement the programming language itself. This
    process is known as *bootstrapping*, named after the phrase *"to
    pull oneself up by one's bootstraps"*.

[^4]: An interesting thing is that to inexperienced programmers, and
    with simple programs, it is a lot easier to read a program than to
    write it. The opposite is the case for experienced programmers
    working in more extensive and more complex programs. Once programs
    reach a certain level of complexity, they get harder to read than to
    write, and a lot of software engineering aims at alleviating this.

[^5]: There is also graphical processing units, GPUs. These are often
    used for running many simple calculations in parallel. For the
    purpose of this chapter, you can just consider them a different kind
    of CPU.

[^6]: In Python, iterating over sequences doesn't actually require that
    we know how many elements we have, because the `for`-loop
    construction is vastly more powerful than what we implement with
    this simple `while`-loop, but using the length is the simplest we
    can do if we implement the `for`-construction ourselves.

[^7]: Again we have an operation that Python provides for us, like the
    `for`-loop construction, that is actually more powerful than we give
    it credit for when we count the number of primitive operations the
    operation takes. We have to have to limit the level of detail we
    consider, so this is as deep as I want to take us down this
    particular rabbit hole.

[^8]: In this particular case, we could just as easily count the
    `if`-body as constant time as well, but it doesn't matter for the
    big-Oh analysis. The entire algorithm runs in $\Theta(n)$.

[^9]: It is possible to multiply matrices faster than this, but that is
    beyond this book.

[^10]: In this chapter, we assume we are working with numbers, but we
    can search for any type of data as long as we can compare two items
    to see if they are equal. With only this assumption, the linear
    search will get the job done. If we furthermore assume that our data
    has a total order, i.e. for any two items we can decide if they are
    equal, or if the first is smaller than or greater than the second,
    then the elements can be sorted and we can use binary search. These
    properties are satisfied by more than just numbers, and we briefly
    discuss what it takes to handle more general sequences in
    [@sec:general-search-sort].

[^11]: If we have a list or a tuple of numbers, we can always get the
    element at any given index in constant time. This property is called
    *random access* and data structures we can get an element by index
    in constant time are called *random access* data structures. It is
    necessary to have the distinction between random access data and not
    because there are many data structures where we do not have constant
    time random access. In [@sec:linked-lists], we shall see one common
    sequence structure, linked lists, that enable us to scan through its
    elements in linear time but not access items by index in constant
    time. There are many more.

[^12]: Unless you have a good reason to, you should use the `in`
    operator to check membership of an item in a data structure. It will
    work for all sequences, using the linear search algorithm, but for
    data structures that allow for faster lookup, such as dictionaries
    or sets, the `in` operator will use the faster algorithms. The only
    case I can think of where you wouldn't necessarily use `in` is for
    sorted, random-access sequences. Python cannot know if a sequence is
    sorted or not so it will use linear search when you use the `in`
    operator on general sequences. Even for sorted sequences, I would
    probably use `in` unless the search is a bottleneck in my algorithm
    because of the simpler syntax and because it makes it easier to
    replace a sequence with another data structure that provides faster
    membership checks. In [Chapter @sec:data-model] we will see how we
    can make Python use a custom algorithm to implement the `in`
    operator so we can tailor searching to our data.

[^13]: "As the situation at ski resorts of young women looking for
    husbands and husbands looking for young women, the situation is not
    as symmetric as it first appears." --- Unknown

[^14]: Some might also classify as in-place algorithms that use
    $O(\log n)$ extra memory. This is to explicitly allow for the number
    of bits it takes to represent numbers up to magnitude $n$. We will
    not get this technical here.

[^15]: Timsort modifies the input list in-place when it can get away
    with it but uses additional memory to speed up the computations when
    necessary.

[^16]: "Seeing the wrong solution to a problem (and understanding why it
    is wrong) is often as informative as seeing the correct solution."
    --- W. Richard Stevens

[^17]: Strictly speaking, we are not guaranteed that appending to a list
    is always constant time, but there is a guarantee that if we append
    to a list $n$ times, then all $n$ operations can be done in $O(n)$.
    So although some operations are not in $O(1)$, on average, they are.
    Using a different data structure, a so-called *doubly linked list*
    (see [@sec:doubly-linked-lists]), we *can* achieve worst-case
    constant time for all append and prepend operations---at the cost of
    linear time to look up elements. If we use these, then we need a
    list `x` with constant time lookup, as we have for python `list`
    objects, and other lists, `y`, where prepend or append are constant
    time, but where we do not need to access random indices. We consider
    linked lists later in the book; for the sorting algorithms we
    consider now, we can still use Python's `list` objects without
    affecting the worst-case running time.

[^18]: At this point, you are excused for getting the impression that we
    can always sort numbers in linear time using radix sort. It sounds
    like that is what I just wrote. This isn't true, however. I did
    write that we needed the numbers to fit into a constant number of
    computer words. This put a bound on how large the integers can be.
    If you want to be able to hold at least $n$ distinct elements in
    your input, you need $O(\log n)$ bits. The time usage depends on the
    size of the integers so they cannot grow arbitrarily larger. If you
    want to sort $n$ distinct numbers, you need a logarithmic number of
    sub-keys, and then you have the same runtime complexity as the
    fastest comparison-sorting algorithms.

[^19]: Strictly speaking, how negative numbers are represented is
    hardware dependent. The hardware can represent numbers in any way it
    wants. I know of no modern architecture that does not represent
    positive and negative numbers as two-complement numbers, see
    [@sec:bin-repres-of-numbers]. The most significant bit might not be
    where you think it is, though, because the order of significance for
    bytes in a word does vary between architecture.

[^20]: What happens to the bits at the left end of a shifted word can
    vary from hardware to hardware and according to which type of shift
    we use. There are really two different versions of right-shift. One
    will always fill the bits on the left of the result with zeros. This
    is called a logical shift. Another shift, called arithmetic shift,
    will fill the bits with zeros or ones depending on whether the most
    significant bit is zero or one. It will fill the left-most bits with
    the same value as the most significant bit in the input. The
    right-shift operator in Python, `>>` does arithmetic shift. The
    reason that you might fill with ones if the top bit is one has to do
    with how negative numbers are represented.

[^21]: The name refers to Jonathan Swift's *Gulliver's Travels* where a
    civil war is fought over which end of an egg should be cracked when
    eating a soft-boiled egg. Fighting over which byte should be
    considered the most significant is equally silly, but you need to
    consider it when you manipulate bit-patterns that represent
    integers.

[^22]: The way Python handles global and local variables, and how it
    handles call frames, is a bit different from what I explain below.
    Python runs in a so-called *virtual machine*, which is a program
    that understands Python better than the raw hardware does and that
    works as an intermediate between the two. The virtual machine runs
    as actual machine instructions on the CPU and Python runs on the
    virtual machine. My description of how calls work is almost correct,
    and all programming languages will do something similar to it, but
    the details can vary. See [@sec:architecture] for what it means that
    Python runs on a virtual machine rather than on the raw hardware.

[^23]: The way Python actually deals with local values, and how it deals
    with the results of local expressions differ from the explanation I
    give here. Python does use a stack for this, it actually uses
    several, but that is beyond the scope of this book. Programs that
    run on the raw hardware on your computer do not just use a stack. It
    is more efficient to put values in a CPU's registers than put them
    in memory, and that is what is usually done. Python has a layer
    between the raw hardware and your programs, the virtual machine. The
    virtual machine runs on the actual hardware, and it uses registers
    to hold temporary values and for passing values between functions.
    Your program, on the other hand, runs on the virtual machine, and
    this machine uses a different approach. If your Python programs
    actually ran on the real CPU, the description here wouldn't be far
    off of what would actually be happening with function calls.

[^24]: Why appending is cheap while prepending is expensive comes down
    to how lists are implemented by Python. We return to this in
    [@sec:dynamic-arrays]. For now, you just have to take my word for
    it.

[^25]: In the interest of complete honesty, I am lying here. You can
    always translate a recursive function into an iterative one. It just
    requires some tricks we are not ready for here. I will show you how
    it can be done in [@sec:thunks_and_trampolines]. The general
    solution, however, usually isn't a particularly good idea. It is not
    efficient and more often than not you get a more efficient solution
    by implementing your own stack as a substitute for the recursion
    stack. If speed is not an issue, but stack size is, the general
    translation from recursion to iteration is more straightforward and
    therefore the preferred solution.

[^26]: A slightly more *Pythonic* way of writing the `if` statement
    would be to use the `or` operator instead. You could write
    `ac = acc or []`. Because
    `` or` will return the second argument if the first is `False`, and because `None` is interpreted as `False` in this context, you will get `[]` when `acc` is `None`. You will also get a new empty list if `acc` is an empty list because empty lists are also interpreted as `False ``.
    We never recurse on an empty list, so that is not a problem.

[^27]: Which real numbers are representable using a finite number of
    digits depends on the base, $b$. You cannot represent $1/3$ using a
    finite decimal ($b=10$) notation but in base $b=3$ it is simply
    $1\times 3^{-1}$. Likewise, you cannot represent $1/10$ in binary in
    a finite number of digits, where you trivially can in base 10.
