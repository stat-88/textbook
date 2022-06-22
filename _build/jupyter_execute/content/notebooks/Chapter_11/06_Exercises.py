#!/usr/bin/env python
# coding: utf-8

# ## Exercises ##

# **1.** 
# A newspaper article called [How a Statistical Formula Won the War](https://www.theguardian.com/world/2006/jul/20/secondworldwar.tvandradio) reports a formula for estimating the number of German tanks under the model we have assumed n Section 11.2. 
# 
# Compare the formula with the "augmented maximum" estimator $T_3$ of Section 11.2 (which is what was actually used in the war). Are the two the same? If not, what is the bias of the estimator in the report? How does the variance of that estimator compare with the variance of the augmented maximum $T_3$?

# **2.** 
# Let $\theta_1 < \theta_2$ and suppose $X_1, X_2, \ldots, X_n$ are i.i.d. uniform on the interval $(\theta_1, \theta_2)$. Let $\theta = \theta_2 - \theta_1$ be the length of the interval.
# 
# **a)** Let $M_1 = \min(X_1, X_2, \ldots, X_n)$ be the sample minimum and $M_2 = \max(X_1, X_2, \ldots, X_n)$ the sample max. The statistic $T_1 = M_2 - M_1$ is called the *range* of the sample and is a natural estimator of $\theta$. Without calculation, explain why $T_1$ is biased, and say whether it underestimates or overestimates $\theta$.
# 
# **b)** Find the bias of $T_1$ and confirm that its sign is consistent with your answer to Part **a**. For large $n$, is the size of the bias large or small?
# 
# **c)** Use $T_1$ to construct an unbiased estimator of $\theta$. Call the new estimator $T_2$.
# 
# **d)** Compare $SD(T_1)$ and $SD(T_2)$. Which one is bigger? For large $n$, is it a lot bigger or just a bit bigger?

# **3.**
# Sometimes data scientists want to fit a linear model that has no intercept term. For example, this might be the case when the data are from a scientific experiement in which the attribute $X$ can have values near $0$ and there is a physical reason why the response $Y$ must be $0$ when $X=0$.
# 
# So let $(X, Y)$ be a random pair and suppose you want to predict $Y$ by an estimator of the form $aX$ for some $a$. Find the least squares predictor $\hat{Y}$ among all predictors of this form.

# **4.**
# Find the mean squared error of the least squares predictor in the previous exercise, and hence prove the *Cauchy-Schwarz Inequality*:
# 
# $$
# \vert E(XY) \vert ~ \le ~ \sqrt{E(X^2)E(Y^2)}
# $$

# **5.**
# Let $(X, Y)$ be a random pair.
# 
# **a)** For constants $a \ne 0$ and $b$, let $V = aX + b$. Apply the definition of correlation to find $r(X, V)$. [It might be easier to separate the cases $a < 0$ and $a > 0$.]
# 
# **b)** For constants $a \ne 0$ and $b$, let $W = aY + b$. Find $r(X, W)$ in terms of $r(X, Y)$. 

# **6**.
# Let $(X, Y)$ be a random pair and let $\hat{Y}$ be the least squares linear predictor of $Y$ based on $X$. Assume $r(X, Y) \ne 0$.
# 
# **a)** Find $r(X, \hat{Y})$.
# 
# **b)** Let $D = Y - \hat{Y}$ be the residual. Find $r(D, \hat{Y})$.

# **7.**
# Let $(X, Y)$ be a random pair and let $r = r(X,Y)$. Let $X^*$ be $X$ in standard units and let $Y^*$ be $Y$ in standard units.
# 
# **a)** Find $r(X^*, Y^*)$.
# 
# **b)** Write the equation for $\hat{Y^*}$, the least squares linear predictor of $Y^*$ based on $X^*$.

# **8.** 
# It can be shown that for many football-shaped scatter diagrams it is OK to assume that each of the two variables is normally distributed. 
# 
# Suppose that a large number of students take two tests (like the Math and Verbal SAT), and suppose that the scatter diagram of the two scores is football shaped with a correlation of 0.6. 
# 
# **a)** Let $(X, Y)$ be the scores of a randomly picked student, and suppose $X$ is on the the 90th percentile. Estimate the percentile rank of $Y$.
# 
# **b)** Let $(X, Y)$ be the score of a randomly picked student, and suppose $Y$ is on the 78th percentile. Estimate the percentile rank of $X$.

# **9.**
# Let $(X, Y)$ be a random pair and let $\hat{Y}$ be the linear regression estimate of $Y$ based on $X$. Let $D = Y - \hat{Y}$ be the residual.
# 
# Justify the *decomposition of varinance* formula $Var(Y) = Var(\hat{Y}) + Var(D)$. 
# 
# 
# 

# **10.**
# Let $X$ be a random variable with expectation $\mu_X$ and SD $\sigma_X$. Suppose you are going to use a constant $c$ as your predictor of $X$.
# 
# **a)** Let $MSE(c)$ be the mean squared error of the predictor $c$. Write a formula for $MSE(c)$.
# 
# **b)** Find $\hat{c}$, the least squares constant predictor.
# 
# **c)** Find $MSE(\hat{c})$.

# **11.**
# Let $X$ have the uniform distribution on the three points $-1$, $0$, and $1$. Let $Y = X^2$.
# 
# **a)** Show that $X$ and $Y$ are uncorrelated.
# 
# **b)** Are $X$ and $Y$ independent?
