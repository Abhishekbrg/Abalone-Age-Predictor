# Abalone-Age-Predictor
Predicting the age of abalone through regression using data set given by UCI
link to download abolone data set: https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/

<h1>Introduction</h1><br>
Abalone is a shellfish considered a delicacy in many parts of the world. An excellent source of iron and pantothenic acid, and a nutritious food resource and farming in Australia, America and East Asia. 100 grams of abalone yields more than 20% recommended daily intake of these nutrients. The economic value of abalone is positively correlated with its age. Therefore, to detect the age of abalone accurately is important for both farmers and customers to determine its price. However, the current technology to decide the age is quite costly and inefficient. Farmers usually cut the shells and count the rings through microscopes to estimate the abalones age. Telling the age of abalone is therefore difficult mainly because their size depends not only on their age, but on the availability of food as well. Moreover, abalone sometimes form the so-called 'stunted' populations which have their growth characteristics very different from other abalone populations This complex method increases the cost and limits its popularity. Our goal in this report is to find out the best indicators to forecast the rings, then the age of abalones.redicting the age of abalone from physical measurements. The age of abalone is determined by cutting the shell through the cone, staining it, and counting the number of rings through a microscope -- a boring and time-consuming task. Other measurements, which are easier to obtain, are used to predict the age.<br>

<h3>Description</h3><br>
From the original data examples with missing values were removed (the majority having the predicted value missing), and the ranges of the continuous values have been scaled for use with an ANN (by dividing by 200). For the purpose of this analysis, we will scale those variables back to its original form by multiplying by 200.<br>

Total number of observations in dataset: 4176<br>

Total number of variables in dataset : 8
<br>
Metadata and attribute information:<br>

<h3>Variable List</h3><br>
1.Name	           Data Type	     Measurement	           Description<br>
2.Sex   	         categorical 		                       M, F, and I (Infant)<br>
3.Length           continuous	       mm	                 Longest shell measurement<br>
4.Diameter         continuous	       mm	                 perpendicular to length<br>
5.Height	         continuous	       mm	                 with meat in shell<br>
6.Whole weight	   continuous	      grams	               whole abalone<br>
7.Shucked weight	 continuous  	    grams	               weight of meat<br>
8.Viscera weight	 continuous	      grams                gut weight (after bleeding)<br>
9.Shell weight	   continuous	      grams	               after being dried<br>
10.Rings	         continuous		    +1.5                 gives the age in years<br>


<h3>Data Set Characteristics:Multivariate</h3><br>

<h3>Number of Instances:4177</h3><br>

<h3>Area:Life</h3><br>

<h3>Attribute Characteristics:Categorical, Integer, Real</h3><br>

<h3>Number of Attributes:8</h3><br>

<h3>Date Donated:1995-12-01</h3><br>

<h3>Associated Tasks:Classification</h3><br>

<h3>Missing Values:No</h3><br>

<h3>Number of Web Hits:775152</h3><br>


<h2>Library Need:</h2><br>
1.Numpy<br>
2.Pandas<br>
3.Matplotlib<br>
4.Seaborn<br>


