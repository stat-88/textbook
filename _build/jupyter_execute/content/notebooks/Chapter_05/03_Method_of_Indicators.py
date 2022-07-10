#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datascience import *
import numpy as np


# ## Method of Indicators ##
# 
# The additivity property of expectation says that for any two random variables $X$ and $Y$ defined on the same space,
# 
# $$
# E(X+Y) ~ = ~ E(X) + E(Y)
# $$
# 
# regardless of the joint distribution of $X$ and $Y$.
# 
# In particular, expectation is additive regardless of the dependence or independence of the two random variables being added.
# 
# Remember that throughout this course, you can assume that there are no problems with the existence of expectations of random variables that have infinitely many values. In more advanced courses you will have to be careful about infinities in the statement of additivity.

# ### Random Counts ###
# 
# In this section we will use additivity to find expectations of random counts such as the number of sixes in rolls of a die, the number of aces in a poker hand, the number of categories of individuals that appear in a random sample, and so on.
# 
# We can do this because of a fundamental property of counting:
# 
# **Counting is the same as adding zeros and ones.** Use the Boolean value 1 as a code for each element you are counting, and 0 as a code for all the others. Then the count is the same as the sum of all the zeros and ones. 
# 
# For example, suppose you are trying to count the number of times the color red appears in the list below:
# 
# blue, red, red, green, blue, red, blue, blue
# 
# Code the list as 0, 1, 1, 0, 0, 1, 0, 0, using 1 for red and 0 for everything else.
# 
# Then the sum of the coded list is 3, which is the number of times red appears in the list.
# 
# In Python too you can count in two ways:

# In[2]:


booleans = make_array(0, 1, 1, 0, 0, 1, 0, 0)
np.count_nonzero(booleans), sum(booleans)


# Thus any random count can be written as a sum of *indicator* random variables.

# ### Indicators ###
# Recall from an earlier section that the *indicator* of an event $A$ is a random variable that has the value 1 if $A$ occurs and 0 if $A$ doesn't occur. You can think of the indicator of $A$ as a Boolean that indicates whether $A$ is true or false.
# 
# Let $I_A$ denote the indicator of $A$. 
# 
# $$
# E(I_A) ~ = ~ 1\cdot P(A) + 0(1 - P(A)) ~ = ~ P(A)
# $$
# 
# as we have seen before.
# 
# We can write a random count as a sum of indicators, and the expectation of an indicator is the probability that it is 1. By additivity, this will give us the expectation of the random count. Let's see how.

# ### Binomial ###
# 
# Let $X$ have the binomial $(n, p)$ distribution. We will use indicators to find the expectation of $X$.
# 
# We know that $X$ can be thought of as the number of successes in $n$ independent repeated success/failure trials with probability $p$ of success on each trial. More succinctly, we say that $X$ is the number of 1's in $n$ i.i.d. Bernoulli $(p)$ trials.
# 
# Write the random count $X$ as the sum of indicators, one indicator per trial.
# 
# $$
# X ~ = ~ I_1 + I_2 + \cdots + I_n
# $$
# 
# where for each $j$, the random variable $I_j$ is the indicator of a success on Trial $j$.
# 
# By additivity of expectation,
# 
# $$
# E(X) ~ = ~ E(I_1) + E(I_2) + \cdots + E(I_n)
# $$
# 
# The expectation of an indicator is the probability that the indicator has the value 1. For each $j$, we have 
# 
# $$
# P(I_j = 1) ~ = ~  P(\text{Trial } j \text{ is a success}) ~ = ~ p
# $$
# 
# So
# 
# $$
# E(X) ~ = ~ p + p + \cdots + p ~ = ~ np
# $$
# 
# This formalizes our intuition that we expect a proportion $p$ of the $n$ trials to be successes and hence we expect the count of successes to be $np$.
# 
# Here are some applications of this result.
# 
# - The number of heads in 100 tosses of a coin has the binomial $(100, 1/2)$ distribution, so the expected number of heads is $100 \times \frac{1}{2} = 50$. 
# - The expected number of heads in 25 tosses of a coin is $25 \times \frac{1}{2} = 12.5$. Remember that expectation doesn't have to be a possible value of the random variable.
# - The number of sixes in 30 rolls or a die has the binomial $(30, 1/6)$ distribution, so the expected number of sixes is $30 \times \frac{1}{6} = 5$.
# - When $n$ is large and $p$ is small, we can approximate the binomial $(n, p)$ distribution by the Poisson distribution with parameter $\mu = np$. Remember that the parameter $\mu$ of a Poisson random variable is its expectation. You can now see that we construct the approximating Poisson distribution by equating expectations: the expectation $\mu$ of the approximating Poisson distribution is taken to be equal to $np$, the expectation of the exact binomial distribution. Thus for example in 1000 independent repeated trials with chance $1/1000$ of success on each trial, the distribution of the number of successes is exactly binomial $(1000, 1/1000)$ and approximately Poisson $(1)$.
# 
# Not only does this calculation by indicators give us an important result, it also *never used the independence* of the indicators. Additvity of expectation doesn't require independence. 
# 
# So we can use the same method in settings where the indicators are not independent, as in the examples below.

# ### Hypergeometric ###
# 
# Let $X$ have the hypergeometric $(N, G, n)$ distribution. We will use indicators to find the expectation of $X$.
# 
# We know that $X$ can be thought of as the number of good elements in a simple random sample of size $n$ drawn from a population of $N$ elements of which $G$ are good. Once again, $X$ is the sum of $n$ Bernoulli random variables.
# 
# Write the random count $X$ as the sum of indicators, one indicator per draw.
# 
# $$
# X ~ = ~ I_1 + I_2 + \cdots + I_n
# $$
# 
# where for each $j$, the random variable $I_j$ is the indicator of drawing a good element on Draw $j$.
# 
# These indicators are not independent, but additivity still applies. 
# 
# $$
# E(X) ~ = ~ E(I_1) + E(I_2) + \cdots + E(I_n)
# $$
# 
# For each $j$, we have 
# 
# $$
# E(I_j) ~ = ~ P(I_j = 1) ~ = ~  P(\text{Draw } j \text{ yields a good element}) ~ = ~ \frac{G}{N}
# $$
# 
# by a now-familiar symmetry argument in random sampling without replacement. So
# 
# $$
# E(X) ~ = ~ \frac{G}{N} + \frac{G}{N} + \cdots + \frac{G}{N} ~ = ~ n\frac{G}{N}
# $$
# 
# This formalizes our intuition that we expect a proportion $\frac{G}{N}$ of the $n$ draws to be good and hence we expect the number of good elements in the sample to be $n\frac{G}{N}$.
# 
# Applications:
# 
# - The number of aces in a 5-card poker hand dealt from a standard deck has the hypergeometric $(52, 4, 5)$ distribution, so the expected number of aces in the hand is $5 \times \frac{4}{52} \approx 0.3846$. You shouldn't expect a lot of aces in a poker hand!
# - If a simple random sample of 65 participants forms the treatment group in a randomized controlled experiment in which 30 of the 100 participants are Californians, then the expected number of Californians in the treatement group is $65 \times \frac{30}{100} = 19.5$.
# - In the example above, suppose the 65 draws had been made at random *with* replacement instead of without. Then the number of times Californians appeared among the draws would have had the binomial $(65, 30/100)$ distribution, and the expected number of times Californians appeared in the sample would still have been $65 \times \frac{30}{100} = 19.5$. On average, sampling with replacement produces the same number of successes as sampling without replacement. The difference is in the variability of the count, as we will see later in the course.

# ### Missing Classes ###
# No, this is not an example about not going to class. Instead, consider a population in which each element belongs to one of three classes. Suppose 40% of the elements are in Class 1, 35% in Class 2, and 25% in Class 3.
# 
# If you draw $n$ times at random with replacement from the population, what is the expected number of classes that don't appear in the sample?
# 
# Let $X$ be the number of classes that don't appear. Then $X$ is a random count *of classes*. So write $X$ as a sum of three indicators, *one indicator per class*.
# 
# $$
# X ~ = ~ I_1 + I_2 + I_3
# $$
# 
# where $I_j$ is the indicator of the event that Class $j$ doesn't appear in the sample.
# 
# The indicators are not independent (for example, they can't all be 1), but additivity still works:
# 
# $$
# \begin{align*}
# E(X) ~ &=~ E(I_1) + E(I_2) + E(I_3) \\
# &= ~ P(\text{Class 1 doesn't appear}) + P(\text{Class 2 doesn't appear}) + P(\text{Class 3 doesn't appear}) \\
# &= ~ 0.6^n + 0.65^n + 0.75^n
# \end{align*}
# $$
# 
# The answer goes to 0 as $n$ gets large. That makes sense. In a very large sample, you expect all classes to appear.
# 
# The number of classes that *do* appear in the sample is $Y = 3 - X$. The expected number of classes that appear is therefore
# 
# $$
# E(Y) ~ = ~ 3 - E(X) ~ = 3 - \big{(} 0.6^n + 0.65^n + 0.75^n \big{)}
# $$
# 
# Notice the use of additivity in the first equality above, applied to $Y = 3 + (-X)$. In the next section we will make some general observations about expectations of linear functions. 

# ### The Method of Indicators ###
# All the examples above have been applications of the *method of indicators*. The method is intended for finding the expectation of a random count that has an upper limit (not counts that can be arbitrarily large). In the binomial and hypergeometric examples, the count could be at most $n$. In the random classes example, the count could be at most 3.
# 
# The method is highly recommended when you just want the expectation of a random count, not the entire distribution of the count. To set up the right indicators to use, look carefully at what is being counted. If for example it is the number of *classes* that have a specified property, then use one indicator per class.
# 
# We end the section with another example of the decision process and calculation.

# ### Birthday Emails ###
# A company has 50 employees. Each month, the company sends out a "happy birthday" email to each employee whose birthday is in that month. If there is a month in which no employee has a birthday, no birthday email is sent that month.
# 
# Suppose each employee's birthday is equally likely to be in any of the 12 months of the year, independently of the birthdays of all others. In a year, what is the expected number of months in which the company sends out more than one birthday email?
# 
# **Answer:** The question asks for an expected count: the expected number of months that have a specified property. So let's try the method of indicators.
# 
# We are counting months, so it's a good idea to use one indicator per month. In a year, the count can be at most 12.
# 
# Let $X$ be the number of months in which the company sends out more than one birthday email. Then
# 
# $$
# X ~ = ~ I_1 + I_2 + \cdots + I_{12}
# $$
# 
# where $I_j$ is the indicator of the event that the company sends more than one birthday email in Month $j$. That's the same as the event that more than one employee's birthday is in Month $j$.
# 
# For each $j$,
# 
# $$
# \begin{align*}
# E(I_j) ~ &= ~ P(\text{more than one birthday in Month }j) \\
# &=~ 1 - \big{(} \binom{50}{0}(1/12)^0(11/12)^{50} + \binom{50}{1}(1/12)^1(11/12)^{49} \big{)}
# \end{align*}
# $$
# 
# and hence 
# 
# $$
# E(X) ~ = ~  12\big{(} 1 - \big{(} \binom{50}{0}(1/12)^0(11/12)^{50} + \binom{50}{1}(1/12)^1(11/12)^{49} \big{)} \big{)}
# $$
# 
# Equivalently,
# 
# $$
# E(X) ~ = ~ 12 \big{(} \sum_{k=2}^{50} \binom{50}{k}(1/12)^k(11/12)^{50-k} \big{)}
# $$

# In[ ]:




