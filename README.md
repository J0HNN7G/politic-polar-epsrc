## A Data-Fitted Network Model for Polarization of Political Opinion


### Introduction and Aims

The original aim of the project was to measure the performance of Higham and Mantzaris’ network model for polarization of political opinion on real-life data.<sup>[1](#1)</sup> The 5 datasets gathered by De et al., were selected for testing the model as they contained opinions recorded over different time frames (1 hour, 1 week, 6 months) and two of the datasets had opinions from a political context; tweets about the 2013 Delhi Assembly election and Reddit posts from the politics forum.<sup>[2](#2)</sup>

When analysing the datasets, it was found that they were all invalid for testing Higham and Mantzaris’ model. Hence, the aim of the project became to find an eligible dataset. For a dataset to be valid, it had to 

1.	Contain features that could capture the political opinion of the participants, not just their emotions (the model is intended for political opinion only).
2.	Express a negative relationship between influenceability and political extremism in participants (the underlying hypothesis of the model).

I was able to find a Twitter dataset based on the US 2020 election that satisfied the first requirement, however, not the second.<sup>[3](#3)</sup> Hence, the focus switched to analysing features of the data available.


### Background
Opinion dynamics have applications in social and political sciences and in recent times, have been useful for explaining the polarization that occur on social medias. Thus, a model which accurately describes how opinion formation occurs in a population is desirable. In 2020, Higham and Mantzaris published an article, in which they explore a new network model for political opinion dynamics.<sup>[1](#1)</sup> The model takes inspiration from the work of Cobb,<sup>[4](#4)</sup> by introducing a nonlinear term to the change of an individual’s opinion between timesteps. Cobb described a political opinion model using stochastic differential equations (SDE), such that politically polarized individuals (extremists) become less receptive to the opinion of their peers. The introduction of the nonlinear term to the network model makes it so that politically polarized individuals behave similarly as in Cobb’s SDE model. The network model is significant and unique in that it applies SDEs to network-based opinion dynamics. Hence, a positive performance of the model could show potential for more application of SDEs to network-based opinion dynamics. Further, the model is specialized for political opinion dynamics, making it more apt for that domain than general opinion models. Although Higham and Mantzaris performed simulations to study the behaviour of their model, they did not test it on any real-life data.

### Methods

For the US Twitter dataset, the product of the opinion and party polarity (Republican = -1, Democrat = 1) was used to represent the political opinion of a tweet along the conservative-democrat axis. The feature assumes that in a two-party system, a negative opinion of a party is an opposing party opinion. A 99.98% winzorization was applied to the feature before linearly scaling it to [-1,1] as it had outlying maximum and minimum values.

The ability of the new feature to capture political opinion was tested by having myself and a non-group member annotate, 500 and 140 tweets respectively, by their perceived political opinion, e.g., positive/negative to democrats/conservatives. Then comparing this to the classification of the opinion value and party assigned by the sentiment analysis and word-tagging in the dataset. Inter-annotator agreement by Cohen’s Kappa score was used to determine consensus of annotations.<sup>[5](#5)</sup> Precision, recall and F1-score were calculated for each label between agreed upon labels by annotators and the dataset classification. Using metrics other than accuracy was useful as the annotation of the tweets was imbalanced. 

Experiments were created to determine the relationship between influenceability and political extremism. For all the methods, the independent variable was the absolute difference between the initial opinion of a participant and the central value, i.e., the higher value, the more extreme initial opinion. A variety of dependent variables were tested, all revolved around measuring the correlation of various manipulations of the participant’s opinion timeseries and the mean opinion timeseries of all the participants that had contacted them, over all time, or by each time the participant’s opinion changed. Due to the size of the US Twitter dataset, a sample of 1000 participants in the largest strongly connected component of the mention network was used for the experiments, whilst for the other datasets, all participants were included in the experiments. A potential critique to the independent variable is that a single opinion of a participant should not be indicative of their political stance, however, it was unclear how many opinions should then be representative.

Naïve methods were devised for fitting a few of Higham and Mantzaris’ model parameters, however, without all parameters fit, the usefulness of these methods is untested.

### Results

The the product of VADER sentiment analysis,<sup>[6](#6)</sup> and the party mentioned was a significant classifier of the political opinion of the tweets along the conservative-democrat axis. If the classifier were random, it would have an accuracy of ~0.20, however, it had an accuracy of 0.55.

Experiments conducted on all datasets, suggest that there is no/very weak correlation between extremity of political/non-political opinion (or emotion for 2/5 of the datasets) and influenceability on expressed opinions or emotions by online and social media contacts. This is by no means a comprehensive study; however, it does suggest that Higham and Mantzaris’ model should not be applied to online or social media data without finding support for the relationship in the data first.

### Discussion

I was able to create a feature that captured the political opinion of the participants in a two-party system. The simplicity of the feature means that it can easily be implemented for any social media content. 

No datasets studied had a negative relationship between influenceability and political extremism in participants. The lack of datasets that satisfy this property would suggest that Higham and Mantzaris’ model is not applicable to general political opinion data as the model is based on that this property exists.

Difficulties arose when handling the US Twitter dataset as it had millions of users. Due to computational constraints, the analysis required sampling for 1000 users per experiment, a very small portion in relation to the dataset population. This calls into question the reliability of the results derived. A potential improvement would be to perform the experiments with larger samples of the dataset population.

### Summary 

The original aim of the project was to fit a political opinion model to real-life data, however, the project’s aim changed to finding a dataset which satisfied the model’s input requirement and hypothesis, as none of the originally collected datasets did. A dataset was found which satisfied the model’s input requirement, i.e., a property of the data entries could accurately capture political opinion. However, yhe dataset did not support the hypothesis that the opinion of politically extreme individuals is less influenced by their online contacts.

### Acknowledgements

I am very grateful to Dr. Higham for his supervision and insights, especially when I was stuck. Further, I am thankful to Dr. De and Ibrahim Sabuncu for providing me with the datasets used in this project. Finally, I thank the School of Mathematics for funding this project with an EPSRC Vacation Internship.

### References

<a id="1">1</a>. Desmond J. Higham, and Alexander V. Mantzaris. “A Network Model for Polarization of Political Opinion.” *Chaos: An Interdisciplinary Journal of Nonlinear Science*, 2020.

<a id="2">2</a>. Abir De, Sourangshu Bhattacharya, Parantapa Bhattacharya, Niloy Ganguly, and Soumen Chakrabarti. “Learning a Linear Influence Model from Transient Opinion Dynamics.” *Proceedings of the 23rd ACM International Conference on Information and Knowledge Management*, 2014. Available upon request.

<a id="3">3</a>. Ibrahim Sabuncu. “USA Nov.2020 Election 20 Mil. Tweets (with Sentiment and Party Name Labels) Dataset.” 2020. Available at: https://dx.doi.org/10.21227/25te-j338.

<a id="4">4</a>. Cobb, Loren, and R. M. Thrall. “Stochastic Differential Equations for the Social Sciences.” *Mathematical Frontiers of the Social and Policy Sciences*, 1981. 

<a id="5">5</a>. Jacob Cohen. “A Coefficient of Agreement for Nominal Scales." *Educational and Psychological Measurement*. 1960.

<a id="6">6</a>. C.J. Hutto, and Eric Gilbert. “VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text.” *Eighth International Conference on Weblogs and Social Media*. 2014.


