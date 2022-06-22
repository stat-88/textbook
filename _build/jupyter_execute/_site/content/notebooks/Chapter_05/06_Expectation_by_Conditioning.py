#!/usr/bin/env python
# coding: utf-8

# ## Expectation by Conditioning ##

# Expectation is a long-run average, so properties of expectation are properties of averages. The method of calculating expectation by conditioning, developed in the previous section, is equivalent to the calculation of the average of a group based on information about subgroups.
# 
# As an example, suppose a class of 60 students is split into two sections of sizes 40 and 20. After the midterm, the average scores in the two sections are recorded in a table.
# 
# |Section| A | B |
# |------:|:---:|:---:|
# |Average| 80  | 70  |
# |Size   | 40  | 20  |
# 
# Then the class average can be calculated as
# 
# $$
# \text{class average} ~ = ~ 80\cdot \frac{40}{60} ~ + ~ 70 \cdot \frac{20}{60} ~ \approx ~ 76.7
# $$
# 
# The overall average is the weighted average of the section averages, where the weights are the proportions in the sections.
# 
# Analogously, if $X$ and $Y$ are two random variables then the the expectation of $X$ can be found by taking the weighted average of the conditional expectations $E(X \mid Y=y)$, where the weights are the probabilities $P(Y = y)$. 
# 
# This can be written as a formula for finding expectation by conditioning:
# 
# $$
# E(X) ~ = ~ \sum_{\text{all }y} E(X \mid Y = y)P(Y = y)
# $$
# 
# The proof is routine after writing $E(X)$ in terms of all the cells of the joint distribution table of $X$ and $Y$. We won't do the details.
# 
# Instead, we will just focus on the natural idea that just as we can find an average as a weighted average of group averages, we can also find an expectation as a weighted average of conditional expectations.
# 
# Here are some examples where we can do such calculations without even writing out a joint distribution table.

# ### Time to Reach Campus ###
# A student has two routes to campus. Each route has a random duration. The student prefers Route A because its expected duration is 15 minutes compared to 20 minutes for Route B. However, on 10% of her trips she is forced to take Route B because of road work on Route A. On the remaining 90% of the days she takes Route A.
# 
# What is the expected duration of her trip on a random day?
# 
# The answer is the weighted average of the two conditional expectations given the different routes:
# 
# $$
# 15(0.9) + 20(0.1) ~ = ~ 15.5 \text{ minutes}
# $$

# ### Tosses of a Random Coin ###
# In Bayesian statistics, parameters that we have thus far considered constant can be thought of as random variables. Let's consider 10 tosses of a coin picked at random from a bag that contains one fair coin, one coin that lands heads with chance 0.2, and two that land heads with chance 0.9. What is the expected number of heads?
# 
# If we knew which coin we were tossing, we would know the expected number of heads. 
# 
# - If we were tossing the coin that lands heads with chance 0.2, then the expected number of heads would be $10 \times 0.2 = 2$. 
# - If we were tossing the fair coin then the expected number of heads would be $5$.
# - If we were tossing a coin that lands heads with chance 0.9 then the expected number of heads would be $9$. 
# 
# This is our signal to condition on which coin we got. The expected number of heads is the weighted average of the conditional expectations above.
# 
# $$
# 2(1/4) + 5(1/4) + 9(2/4) ~ = ~ 6.25
# $$
# 
# This is the weighted average of the conditional expectations given which coin was selected, where the weights are the chances of selecting the coins.

# ### Catching Misprints ###
# The number of misprints in a document about to be printed is a random variable $N$ that has a Poisson $(5)$ distribution. Each misprint is caught before printing with chance $0.95$ independently of all other misprints. What is the expected number of misprints that are caught before printing?
# 
# Let $M$ be the number of misprints that are caught before printing.
# 
# As a starting point, suppose we happen to know that the number of misprints $N$ has the value 8. Then the number of misprints that are caught has the binomial distribution with parameters $n = 8$ and $p = 0.95$. So $E(M \mid N = 8) = 8 \times 0.95$.
# 
# In general, suppose we are given that the total number of misprints is $N = n$ for some fixed positive number $n$. Conditional on the event $N=n$, the distribution of $M$ is binomial $(n, 0.95)$, and therefore $E(M \mid N = n) = n \times 0.95$.
# 
# The result is true also for $n = 0$. If there are no misprints, then no misprints will be caught.
# 
# So for each possible value $n$ of the number of misprints $N$, we have $E(M \mid N=n) = 0.95n$. By our rule for finding expectations by conditioning,
# 
# $$
# E(M) ~ = ~ \sum_{n=0}^\infty 0.95n P(N=n) ~ = ~ 0.95 \sum_{n=0}^\infty nP(N=n) ~ = ~ 0.95E(N) ~ = ~ 0.95 \times 5
# $$
# 
# because $N$ has the Poisson $(5)$ distribution and hence $E(N) = 5$.

# ### Expectation of a Geometric Waiting Time ###
# 
# We will now use the method of finding expectation by conditioning to find the expectation of a waiting time that has the geometric $(p)$ distribution on $1, 2, 3, \ldots $.
# 
# Remember that a random variable $X$ has this distribution if $X$ is the number of trials till the first success in independent, identically distributed Bernoulli $(p)$ trials.
# 
# Set $x$ equal to the as yet unknown value of $E(X)$. We will develop an equation for $x$ and then solve it.
# 
# The equation is based on conditioning on the result of the first trial, as follows.
# 
# If the first trial is a success, then $X$ is 1.
# 
# If the first trial is a failure, then one trial has been used up and we still have to wait for the first success. The crucial observation is that at this point *the game starts over*. The excess amount we have to wait after the failure on the first trial *has the same distribution as $X$, and hence the same expectation as $X$*.
# 
# The equation for $x = E(X)$ is thus
# 
# $$
# x ~ = ~ p \cdot 1 ~ + ~ q(1 + x)
# $$
# 
# That is,
# 
# $$
# (1 - q)x ~ = ~ p + q = 1
# $$
# 
# That's the same as
# 
# $$
# px ~ = ~ 1, ~~~~~~ \text{so } x ~ = ~ \frac{1}{p}
# $$
# 
# We have shown that if $X$ has the geometric $(p)$ distribution on $1, 2, 3, \ldots$ then $E(X) = 1/p$.
# 
# This result agrees with our intuition. For example,
# 
# - The expected number of tosses till a coin lands heads is $1/0.5 = 2$.
# - The expected number of rolls till a die shows the face with six spots is $1/(1/6) = 6$.

# ### Waiting Till 10 Sixes ###
# Let $T_{10}$ be the number of rolls of a die till a total of 10 sixes have appeared. Find $E(T_{10})$.
# 
# To get 10 sixes, you have to wait for one six, then for the second one, then for the third one, and so on, up to the tenth one. Thus
# 
# $$
# T_{10} ~ = ~ X_1 + X_2 + \ldots + X_{10}
# $$
# 
# where 
# 
# - $X_1$ is the number of rolls till the first six appears
# - $X_2$ is the number of rolls following $X_1$ till the second six appears,
# - and so on, till
# - $X_{10}$ is the number of rolls following $X_9$ till the tenth six appears.
# 
# Each of $X_1, X_2, \ldots, X_n$ has the geometric $(1/6)$ distribution on $1, 2, 3, \ldots $. By additivity of expectation,
# 
# $$
# E(T_{10}) ~ = ~ E(X_1) + E(X_2) + \ldots + E(X_{10}) ~ = ~ 6 + 6 + \cdots + 6 ~ = ~ 60
# $$

# In[ ]:




