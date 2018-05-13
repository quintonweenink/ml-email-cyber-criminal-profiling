import datetime

# Did this so you don't overwrite previous things by mistake
now = str(datetime.datetime.now().replace(microsecond=0))
spamcsv = "./experiments/spam-" + now + ".csv"
spamDir = "./experiments/spam"

import pandas as pd

import os
import csv

# Using the built in python email parser to get all the info required
from email.parser import BytesParser, Parser
from email.policy import default

# Using the `|` separator here so that we don't have issues with `,` in the data.
# Not 100% there are no pipes but it has worked so far.
with open(spamcsv, 'w') as csvfile:
    writer = csv.writer(csvfile)
    for root, dirs, files in os.walk(spamDir):
        for name in files:
            with open(os.path.join(root, name), 'rb') as fp:
                email = BytesParser(policy=default).parse(fp)
                try:
                    writer.writerow([email['Subject']])
                except Exception as e:
                    print("Error: Couldn't write email")
                    print(e)

print("-- DONE --")