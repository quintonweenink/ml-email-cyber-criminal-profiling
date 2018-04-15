### Email Cyber Criminal Profiling

*Abstract:* None

#### Research paper

Research paper is under `/docs`

#### Getting Started:

##### Install dependencies:
`sudo -H pip install -r requirements.txt`

##### Running a simulation:

1. Go to the directory of the file
2. Run `python3 experiments/pso/boundaryConstraintInvestigation.py`

#### Process

1. Data Acquisition / Generation / Fabrication: Use an email header meta-data structure, such as what is available for Gmail, and acquire from a publicly available email dataset, such as the Enron email dataset, at least 200000 emails. Alternatively you can fabricate your own email dataset as long as the emails are created according to a standard metadata email structure and you are able to eventually discover some cyber threats in it.

We will be using the Enron dataset ( [@Bernhard](https://github.com/BernhardSchuld) sorted this out )

2. Data Cleaning: Your data needs to be reliable. Dirty data is data which has values that are missing, incorrect or inconsistent. Do data cleaning on your dataset with a program / script.

I think we will just do headers for now:

Info on headers:
[What Can You Find in an Email Header?](https://www.howtogeek.com/108205/htg-explains-what-can-you-find-in-an-email-header/)
