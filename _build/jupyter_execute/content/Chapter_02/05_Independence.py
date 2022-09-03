#!/usr/bin/env python
# coding: utf-8

# ## Independence ##

# Events $A$ and $B$ are *independent* if the information that one of them occurred does not change the chance of the other.
# 
# - If you don't know whether $A$ has occurred, then the chance of $B$ is just $P(B)$. 
# - If you do know that $A$ occurred, then you have to update the chance of $B$ to $P(B \mid A)$, the conditional chance of $B$ given $A$.
# 
# The definition of independence says that $A$ and $B$ are independent if $P(B \mid A) = P(B)$.
# 
# For example, suppose you roll a die once and see an odd number. What does that tell you about the chance that the next roll is a 2? If your answer is, "Nothing – the chance that the next roll is a 2 is still 1/6," then you have said that the two events "first roll is an odd number" and "second roll is 2" are independent. 

# ### Dice Versus Cards ###
# 
# Suppose you are rolling a die twice. Then
# 
# $$
# \begin{align*}
# &P(2 \text{ on the second roll} \mid \text{odd number on the first roll}) \\
# &= ~ P(2 \text{ on the second roll}) ~ = ~ \frac{1}{6}
# \end{align*}
# $$
# 
# Independence is a natural assumption about successive rolls of a die. But when cards are dealt (at random without replacement, as we consistently assume) from a deck, then the situation is different.
# 
# Suppose two cards are dealt from a standard deck in which four out of 52 cards are aces. We know that by symmetry,
# 
# $$
# P(\text{second card is an ace}) ~ = ~ \frac{4}{52}
# $$
# 
# It's worth reviewing the reason for this: since we have no other information, all 52 cards are equally likely to be appear on the second draw, and four of them are aces.
# 
# However,
# 
# $$
# \begin{align*}
# P(\text{second card is an ace} \mid \text{first card is an ace})~ &= ~ \frac{3}{51} \\ 
# &\neq ~ P(\text{second card is an ace})
# \end{align*}
# $$
# 
# The information that the first card is an ace *changes the probability* that the second card is an ace. The events "the first card is an ace" and "the second card is an ace" are not independent. Knowing that the first card is an ace eliminates an ace from the deck, and probabilities have to be recalculated accordingly.

# ### A Special Case of the Multiplication Rule ###
# 
# Suppose you deal two cards. By the multiplication rule,
# 
# $$
# \begin{align*}
# & P(\text{both cards are aces}) \\
# &= ~ P(\text{first card is an ace})P(\text{second card is an ace} \mid \text{first card is an ace}) \\
# &= ~ \frac{4}{52} \times \frac{3}{51}
# \end{align*}
# $$
# 
# If you roll two dice, then by the multiplication rule again,
# 
# $$
# \begin{align*}
# & P(\text{odd number on the first roll and } 2 \text{ on the second roll}) \\
# &= ~ P(\text{odd number on the first roll})P(2 \text{ on the second roll} \mid \text{odd number on the first roll}) \\
# &= ~ \frac{3}{6} \times \frac{1}{6}
# \end{align*}
# $$
# 
# The second factor in the product is not affected by the condition that the first roll was an odd number.
# 
# What we have observed in the example above can be generalized as follows.
# 
# The multiplication rule says that for any two events $A$ and $B$,
# 
# $$
# P(AB) ~ = ~ P(A)P(B \mid A)
# $$
# 
# In the case of independent events $A$ and $B$ the second factor in the multiplication rule is the same as the unconditional chance of $B$:
# 
# $$
# P(AB) ~ = ~ P(A)P(B) ~~ \text{if } A \text{ and } B \text{ are independent}
# $$
# 
# Notice that if you are trying to find the chance of an intersection, then independence does not affect *whether* you multiply chances. Independence only affects *what* you multiply. 
# 
# It is simplest to just remember the general multiplication rule. Independence is then an easy special case.
# 
# Return to the example of rolling a die twice. We have
# 
# $$
# P(\text{ odd number on the first roll and } 2 \text{ on the second roll}) ~ = ~ 
# \frac{3}{6} \times \frac{1}{6} ~ = ~ \frac{3}{36}
# $$
# 
# We can now check that the assumption of independence is consistent with an assumption that we have made all along: that all 36 outcomes of the two rolls are equally likely. Under that assumption, we would have solved the problem by saying that three pairs $(1, 2)$, $(3, 2)$, and $(5, 2)$ form the event and hence the chance is $3/36$. That's the same as what we got by using independence.
# 
# The definition of independence extends to multiple events. A collection of events are *mutually independent* if knowing that any group of them has occurred doesn't affect the chances of the others.

# ### People v. Collins, 1968 ###
# 
# In 1964, the married couple Michael and Janet Collins were arrested for robbery in California. A jury found them guilty, based in part on a probability calculation. 
# 
# Michael Collins appealed the conviction to the California Supreme Court. In 1968 the Court overturned the jury's conviction. 
# 
# In the [statement](https://law.justia.com/cases/california/supreme-court/2d/68/319.html) of the majority opinion, Justice Raymond Sullivan wrote, "We deal here with the novel question whether evidence of mathematical probability has been properly introduced and used by the prosecution in a criminal case. While we discern no inherent incompatibility between the disciplines of law and mathematics and intend no general disapproval or disparagement of the latter as an auxiliary in the fact-finding processes of the former, we cannot uphold the technique employed in the instant case."
# 
# To see what the Justices could not uphold, we start with their summary of the incident that led to the arrest. We apologize that the quote includes the term used to describe a black person in the statement as well as during the trial.
# 
# "On June 18, 1964, about 11:30 a.m. Mrs. Juanita Brooks, who had been shopping, was walking home along an alley in the San Pedro area of the City of Los Angeles. She was pulling behind her a wicker basket carryall containing groceries and had her purse on top of the packages. She was using a cane. As she stooped down to pick up an empty carton, she was suddenly pushed to the ground by a person whom she neither saw nor heard approach. She was stunned by the fall and felt some pain. She managed to look up and saw a young woman running from the scene. According to Mrs. Brooks the latter appeared to weigh about 145 pounds, was wearing "something dark," and had hair "between a dark blond and a light blond," but lighter than the color of defendant Janet Collins' hair as it appeared at trial. Immediately after the incident, Mrs. Brooks discovered that her purse, containing between \$35 and \$40 was missing.
# 
# About the same time as the robbery, John Bass, who lived on the street at the end of the alley, was in front of his house watering his lawn. His attention was attracted by "a lot of crying and screaming" coming from the alley. As he looked in that direction, he saw a woman run out of the alley and enter a yellow automobile parked across the street from him. He was unable to give the make of the car. The car started off immediately and pulled wide around another parked vehicle so that in the narrow street it passed within 6 feet of Bass. The latter then saw that it was being driven by a male Negro, wearing a mustache and beard. At the trial Bass identified defendant as the driver of the yellow automobile. However, an attempt was made to impeach his identification by his admission that at the preliminary hearing he testified to an uncertain identification at the police lineup shortly after the attack on Mrs. Brooks, when defendant was beardless.
# 
# In his testimony Bass described the woman who ran from the alley as a Caucasian, slightly over 5 feet tall, of ordinary build, with her hair in a dark blonde ponytail, and wearing dark clothing. He further testified that her ponytail was "just like" one which Janet had in a police photograph taken on June 22, 1964."
# 
# In the jury trial, the prosecutor had provided a table of probabilities:
# 
# |Characteristic              |Individual Probability|
# |:---------------------------|---------------------:|
# |A. Partly yellow automobile |1/10                  |
# |B. Man with mustache        |1/4                   |
# |C. Girl with ponytail       |1/10                  |
# |D. Girl with blond hair     |1/3                   |
# |E. Negro man with beard     |1/10                  |
# |F. Interracial couple in car|1/1000                |
# 
# The prosecutor had then multiplied all the probabilities together to get an answer of about 1 in 12,000,000. Quoting again from the Supreme Court's statement, "Applying the product rule to his own factors the prosecutor arrived at a probability that there was but one chance in 12 million that any couple possessed the distinctive characteristics of the defendants."
# 
# Though the jury had been swayed by this calculation, the Supreme Court understood the importance of checking assumptions. 
# 
# - First, they objected to the fact that the prosecution had provided no basis for arriving at the probabilities in the table: "[W]e find the record devoid of any evidence relating to any of the six individual probability factors."
# - Second, they did not accept the assumption of independence of the factors. They pointed out the difficulty of believing that having a beard and having a mustache are independent. It is not hard to come up with other examples of this difficulty. Treating characteristics D, E, and F as independent is hard to justify.
# 
# When probability theory is used in practice, it is important to make sure that the assumptions of the theory are reasonable before doing calculations. Otherwise the analysis might be just as weak as the one in the Collins case, which "lacked an adequate foundation both in evidence and in statistical theory".

# ### Regina v. Clark, 2003 ###
# 
# The lessons learned in the Collins case have been widely broadcast and appear in many statistics textbooks – but clearly not the ones read by expert witnesses in the case of Sally Clark in the United Kingdom. 
# 
# Two of Clark's apparently healthy sons died in infancy. On both occasions, Clark was alone with her baby at the time of death, and there was no evidence of injury. After the second death, Clark was arrested for murder. Her defence was that the babies had died of Sudden Infant Death Syndrome (SIDS), referred to in the UK as Sudden Unexplained Death in Infancy (SUDI) or "cot death". But she was found guilty.
# 
# Clark's conviction was overturned on a second appeal, after she had served three years of her prison sentence. Among the reasons for the reversal were the acknowledgment by the court that there had been serious misuse of statistical reasoning.
# 
# In particular, a medical expert witness claimed that the chance of Clark's two babies dying of SIDS was about 1 in 73 million. He arrived at this figure in two steps:
# 
# - First he estimated the chance of a cot death in a family like Clark's. The estimate was based on a large-scale multidisciplinary analysis of SIDS that reported an overall SIDS death rate of 1 in 1303 live births in the UK. Clark was a lawyer and the family did not have financial struggles. After taking such factors into account, the expert set the rate at 1 in 8543, arguing that SIDS deaths were less likely in families like Clark's than in the general population.
# 
# - Then he found the chance of two SIDs deaths in Clark's family by the calculation 
# 
# $$
# \frac{1}{8543} \times \frac{1}{8543} = \frac{1}{72982849}
# $$
# 
# That's about 1 in 73 million.
# 
# The Royal Statistical Society (RSS) [objected](https://web.archive.org/web/20110824151124/http://www.rss.org.uk/uploadedfiles/documentlibrary/744.pdf) vigorously to this calculation on the grounds that the assumption of independence is hard to justify. Given that there is one SIDS death in a family, the risk to other babies in the family might be larger.
# 
# "There may well be unknown genetic or environmental factors that predispose families to SIDS, so that a second case within the family becomes much more
# likely," the RSS wrote. "The well-publicised figure of 1 in 73 million thus has no statistical basis. Its use cannot reasonably be justified as a "ballpark" figure because the error involved is likely to be very large, and in one particular direction. The true frequency of families with two cases of SIDS may be very much less incriminating than the figure presented to the jury at trial."
# 
# The Society also pointed out that the media had misinterpreted the erroneous figure of 1 in 73 million to be the chance that Clark was innocent. The error was an instance of the Prosecutor's Fallacy in which the likelihood of the evidence given innocence was confused with the chance of innocence given the evidence.
# 
# Thirty-five years after the Collins case, another unjustifiable assumption of independence made by a prosecution witness resulted in a wrongful conviction for Clark. The Sally Clark case is regarded as a great miscarriage of justice and had devastating consequences. Though Clark was strongly supported by her husband throughout, she was in the end unable to cope with the loss of her sons and the injustice she suffered. She died in 2007.
# 
# Apart from statistical error, a serious flaw in the prosecution's case was that another of its medical experts withheld blood test reports showing that the second baby had harmful bacteria in several places in his body including the cerebro-spinal fluid. After Clark's conviction was overturned, the Journal of the Royal Society of Medicine (JRSM) [addressed](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC539414/) the questions the case raised about the conduct of medical expert witnesses.
# 
# The JRSM urged more appropriate investigation of SIDS deaths. It also made an important general recommendation. "[W]hen giving evidence to the police or to the court doctors would be wise to acknowledge the limitations in their understanding. They should present all relevant facts in a balanced manner, offer opinions only within their sphere of expertise and take care not to overstate their case. Wrong conclusions in either direction may be disastrous."

# In[ ]:




