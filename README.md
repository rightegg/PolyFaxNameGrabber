# PolyFax with NameGrabber

# Changes

Changed "type" in polyfax.py to "name"

Changed csv.field_size_limit input to 2147483647 in Util.py and Analyzer.py

Created NameCrawler class

Added "Repos" entry to Config file

# How to Use

Run python polyfax.py -a crawler to collect information on repositories specific in Config file.

Other functions are untouched.

# PolyFax ReadMe

# Introduction
![PolyFax](https://github.com/Daybreak2019/PolyFax/blob/main/images/polyfax.png)
***
PolyFax provides basic features, including repository crawler, commit classification, and language interaction categorization.
Its precision and recall indicate the possibility of being applied for multiple purposes.
For example, the VCC can be used for empirical analysis and provide abundant training data for machine learning (or deep learning) based vulnerability detectors since the code snippets, issues, or even CVEs of the commits can be retrieved on the results of VCC.
Moreover, it is not limited to the type of language due to the language-independent implementation.

Meanwhile, PolyFax provides a multi-task wrapper in implementation. Hence it enables parallel processes for **Crawler** and **Analyzer** and can retrieve and analyze 10 million commits in 24 hours.
Moreover, developers or researchers can easily extend or customize the PolyFax based on its object-oriented design.

# Setup PolyFax

Here we present the procedure to setup PolyFax through source code in three steps as below:
1. Check prerequisites. PolyFax is well tested with Python3 under OS ubuntu 18.04; the suggested python version is 3.8+.
2. Download source code through [this](https://github.com/Daybreak2019/PolyFax).
3. Enter directory PolyFax and run [dependence.sh](https://github.com/Daybreak2019/PolyFax/blob/main/dependence.sh) to install the necessary dependencies (e.g., fuzzywuzzy, nltk).

# Use PolyFax
Following sections demonstrate how to use PolyFax with its three primary functionalities: grabbing repositories from GitHub and running the two analyzers of vulnerability-fixing commit and language interaction categorization.

### Default parameters
PolyFax has a default configure file under [config.ini](https://github.com/Daybreak2019/PolyFax/blob/main/Data/Config/config.ini) with the content as below:
1. UserName: the username of GitHub account 
2. Token: the access token of GitHub account
3. TaskNum: the number of process for PolyFax 
4. Languages: the languages the projects should contain
5. Domains: the domains the projects belong to
6. MaxGrabNum: the maximum number of projects to grab

Specifically, {Languages=[]} and {Domains=[]} means the ***Crawler*** would not check languages and domains.
{MaxGrabNum=-1} indicates ***Crawler*** will grab repositories as many as possible.

### Grabbing repositories from GitHub
With the {MaxGrabNum=5} configured for demonstration,
run the following command to grab the repository from GitHub.
In this step, ***Crawler*** will grab the repository profile, clone the repositories, and grab commits to local storage.

```
    python polyfax.py -a crawler
```

The runtime log is similar as:

![PolyFax](https://github.com/Daybreak2019/PolyFax/blob/main/images/crawler-log.png)



### Run analyzer of vulnerability-fixing commit categorization (VCC)}
When repository profiles and commits are grabbed to local,
users can use the following command to categorize vulnerability-fixing commits:
```
    python polyfax.py -a vcc
```

The runtime log is similar as:

![PolyFax](https://github.com/Daybreak2019/PolyFax/blob/main/images/vcc-log.png)



### Run analyzer of language interaction categorization (LIC)}
When repository profiles and the sources of repositories are cloned to local in 2.2,
users can use the following command to categorize the projects by language interaction mechanisms:

```
    python polyfax.py -a lic
```

The runtime log is similar as:

![PolyFax](https://github.com/Daybreak2019/PolyFax/blob/main/images/lic-log.png)
