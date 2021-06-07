## A Data-Fitted Network Model for Polarization of Political Opinion


### Objectives
1.	Fit the network model for polarization of political opinion proposed by Higham and Mantzaris,<sup>[1](#1)</sup> to the opinion network datasets gathered by De et al.<sup>[2](#2)</sup>

2.	Compare the performance of the data-fitted network model with state-of-the-art opinion network models on the opinion network datasets.
If time permits, an extended model will be explored, potentially improving on shortcomings observed in the results.


### Background
Opinion dynamics have applications in social and political sciences and in recent times, have been useful for explaining the polarization that occur on social medias. Thus, a model which accurately describes how opinion formation occurs in a population is desirable. In 2020, Higham and Mantzaris published an article, in which they explore a new network model for political opinion dynamics.<sup>[1](#1)</sup> The model takes inspiration from the work of Cobb,<sup>[3](#3)</sup> by introducing a nonlinear term to the change of an individual’s opinion between timesteps. Cobb described a political opinion model using stochastic differential equations (SDE), such that politically polarized individuals (extremists) become less receptive to the opinion of their peers. The introduction of the nonlinear term to the network model makes it so that politically polarized individuals behave similarly as in Cobb’s SDE model. The network model is significant and unique in that it applies SDEs to network-based opinion dynamics. Hence, a positive performance of the model could show potential for more application of SDEs to network-based opinion dynamics. Further, the model is specialized for political opinion dynamics, making it more apt for that domain than general opinion models. Although Higham and Mantzaris performed simulations to study the behaviour of their model, they did not test it on any real-life data. Thus, the aim of this project is to determine the real-life performance of the model.

### References

<a id="1">1</a>. Desmond J. Higham, and Alexander V. Mantzaris. “A Network Model for Polarization of Political Opinion.” *Chaos: An Interdisciplinary Journal of Nonlinear Science*, vol. 30, no. 4, 2020, p. 043109.

<a id="2">2</a>. Abir De, Sourangshu Bhattacharya, Parantapa Bhattacharya, Niloy Ganguly, and Soumen Chakrabarti. “Learning a Linear Influence Model from Transient Opinion Dynamics.” *Proceedings of the 23rd ACM International Conference on Information and Knowledge Management*, 2014.

<a id="3">3</a>. Cobb, Loren, and R. M. Thrall. “Stochastic Differential Equations for the Social Sciences.” *Mathematical Frontiers of the Social and Policy Sciences*, by Loren Cobb, Westview Pr, 1981. 

