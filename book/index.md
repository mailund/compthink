## Representing floating point numbers

Floating point numbers, the computer analogue to real numbers, can be represented in different ways, but they are all variations of the informal presentation I give in this section. If you are not particularly interested in how these numbers are represented, you can safely skip this section. You can already return to it if you think you are getting weird behaviour when working with floating point numbers.

The representation used by modern computers is standardised as IEEE 754. It fundamentally represents numbers as explained below, but with some tweaks that let you represent plus and minus infinity, “not a number” (NaN), and with higher precision for numbers close to zero than the presentation here would allow. It also uses a sign bit for the coefficient while it represents the exponent as a signed integer for reasons lost deep in numerical analysis. All that you need to know is that floating point numbers work roughly as I have explained here, but with lots of technical complications. If you find yourself a heavy user of floating point numbers, you will need to study numerical analysis beyond what we can cover in this book, and you can worry about the details of number representations there.

Floating point numbers are similar to the *scientific notation* for base-$b$ numbers, where numbers are represented as

$$x = \pm a\times b^{\pm q}$$

where $a = a_1.a_2a_3\ldots a_n, a_i\in\{0,1,\ldots,b-1\}$ is the *coefficient* and $q = q_1q_2q_3\ldots q_m, q_i\in\{0,1,\ldots,b-1\}$ is the *exponent* of the number. To get a binary notation, replace $b$ by $2$. For non-zero numbers, $a_1$ must be 1, so we do not represent it explicitly, which gives us one more bit to work with. Not all real numbers can be represented with this notation if we require that both $a$ are $q$ are finite sequences,[^1] but if we allow them to be infinite we can. We can approximate any number arbitrarily close by using sufficiently long sequences numbers of digits; $n$ for the coefficient and $m$ for the exponent. We usually assume that if $x\neq 0$ then $a_1\neq 0$ since, if $a_1 = 0$ we can update $a$ to $a_2.a_3\ldots a_n$ and decrease $q$ by one if positive or increase it by one of positive.

Where floating point numbers differ from the real numbers is that we have a fixed limit on how many digits we have available for the coefficient and the exponent. To represent any real number, we can choose sufficiently high values for $n$ and $m$, but with floating point numbers there is a fixed number of digits for $a$ and $b$. You cannot approximate all numbers arbitrarily close. For example, with $b=2$ and $n=m=1$, we have $\pm a\in\{-1,0,1\}, \pm q\in\{-1,0,1\}$, so we can only represent the numbers $\{-1, -1/2, 0, 1/2, 1\}$: $\pm 1/2 = \pm 1\times 2^{-1}$, $\pm 0 = \pm 0\times 2^q$, and $\pm 1 = \pm 1\times 2^{\pm 0}$ (where $\pm 0$ might be represented as two different numbers, signed and unsigned zero, or as a single unsigned zero, depending on the details of the representation). If we use two bits for the exponent, we get the number line shown in [@fig:number-line].


![Number line when we have one bit for the coefficient and two bits for the exponent.](number-line.pdf "number-line")


As a rule of thumb, floating point numbers have the property that is illustrated in [@fig:number-line]. The numbers are closer together when you get closer to zero and further apart when their magnitude increase. There is a positive and a negative minimal number; you cannot get closer than those to zero except by being zero. If you need to represent a non-zero number of magnitude less than this, we say that you have an *underflow* error. There are also a smallest and a largest number (the positive and negative numbers furthest from zero). If you need to represent numbers of magnitude larger than these, we say you have an *overflow* error.

There isn’t really much you can do about underflow and overflow problems except to try to avoid them. Translating numbers into their logarithm is often a viable approach if you only multiply numbers, but can be tricky if you also need to add them.

In the binary sum example from earlier, the problem is not underflow or overflow, but rather losing significant bits when adding numbers. The problem there is the fixed number of bits set aside for the coefficient. If you want to add two numbers of different magnitude, i.e. their exponents are different, then you first have to make the exponents equal, which you can do by moving the decimal point. Consider $1.01101\times 2^{3}$ to $1.11010\times 2^0$—where we have five bits for the coefficients (plus one that is always 1, i.e. $n=6$). If you want to add $1.01101\times 2^{3}$ to $1.11010\times 2^0$ you have to move the decimal point in one of them. With the representation we have for the coefficients, $a=a_1.a_2\ldots a_n$, we can only have one digit before the decimal point so we cannot translate $1.01101\times 2^3$ into $1011.01\times 2^0$, so we have to translate  $1.11010\times 2^0$ into $0.00111010\times 2^3$. We want the most significant bit to be one, of course, but we make this representation for the purpose of addition; once we have added the numbers, we put it in a form where the most significant bit in the coefficient is one. The problem with addition is that we cannot represent $0.00111010\times 2^3$ if we only have five bits in the coefficient. We have five bits because our numbers are six bits long and the first one must always be one. So we have to round the number off and get $0.00111\times 2^3$. The difference in the sum is $2^{-4} = 0.0625$, so not a large difference in the final result, but we have lost three bits of accuracy from the smaller number.

Without limiting the number of bits we have this calculation.

\begin{align}
1.01101 \times 2^3 + 1.11010 \times 2^0    &= \\
1.01101 \times 2^3 + 0.00111010 \times 2^3 &= \\
1.01101 \times 2^3 + 0.00111010 \times 2^3 & = 1.10100010 \times 2^3 \\
\end{align}

If we cannot go beyond five bits, translating $1.11010$ into $0.00111010\times 2^3$ will get us  $0.00111\times 2^3$ and using that we get:

$$1.01101 \times 2^3 + 0.00111 \times 2^3 = 1.10100 \times 2^3$$

This is clearly different from the calculation with more bits.

In general, you expect to lose bits equal to the difference in the exponents of the numbers. The actual loss depends on the details of the representation, but as a rule of thumb, this is what you will lose.

Assume we have one informative bit for the coefficient ($n=2$) and two for the exponent, ($m=2$), and we wanted to add six ones together $6\times 1.0_2 \times 2^0 = 1.1_2\times 2^2$. Adding the numbers one at a time we get:

\begin{align}
1.0 \times 2^0 + 1.0 \times 2^0 &= 1.0 \times 2^1 \\
1.0 \times 2^1 + 0.1 \times 2^1 &= 1.1 \times 2^1 \\
1.1 \times 2^1 + 0. 1 \times 2^1 &= 1.0 \times 2^2 \\
1.0 \times 2^2 + 0.01 \times 2^2 &= 1.01 \times 2^2 = 1.0 \times 2^2 \\
\end{align}

which is off by $0.1\times 2^2$. If we add the numbers as we did with our `binary_sum` function, we instead have

\begin{align}
1.0 \times 2^0 + 1.0 \times 2^0 &= 1.0 \times 2^1 \quad (\times 3)\\
1.0 \times 2^1 + 1.0 \times 2^1 &= 1.0 \times 2^2 \\
1.0 \times 2^2 + 1.0 \times 2^2 &= 1.1\times 2^2
\end{align}

which is correct.

Obviously, the floating point numbers you use in Python have a much higher precision than one bit per coefficient and two per exponent so you will not run into problems with accuracy as fast as in this example. The principle, is the same, however. If you add enough numbers, you risk that the accumulator becomes too large for the addition with the next number to have an effect. If you run into this, then adding the numbers pairwise as in `binary_sum` can alleviate this.

[^1]:	Which real numbers are representable using a finite number of digits depends on the base, $b$. You cannot represent $1/3$ using a finite decimal ($b=10$) notation but in base $b=3$ it is simply $1\times 3^{-1}$.  Likewise, you cannot represent $1/10$ in binary in a finite number of digits, where you trivially can in base 10.