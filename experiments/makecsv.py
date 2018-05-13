import datetime

# Did this so you don't overwrite previous things by mistake
now = str(datetime.datetime.now().replace(microsecond=0))
enroncsv = "./experiments/enron-" + now + ".csv"
metadataHeaders = './experiments/metadataHeaders.csv'
emailDir = "./experiments/maildir/maildir"

import pandas as pd
columns = pd.read_csv(metadataHeaders, sep=',').columns.tolist()


def getPersonAndDiretory(root):
    dindex = root.rfind('/')
    left = root[:dindex]
    directory = root[dindex + 1:]

    pindex = left.rfind('/')
    person = root[pindex + 1:dindex]

    return person, directory


import os
import csv

# Using the built in python email parser to get all the info required
from email.parser import BytesParser, Parser
from email.policy import default

# Using the `|` separator here so that we don't have issues with `,` in the data.
# Not 100% there are no pipes but it has worked so far.
with open(enroncsv, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, delimiter='|', quotechar='|', fieldnames=columns)
    for root, dirs, files in os.walk(emailDir):
        person, directory = getPersonAndDiretory(root)
        print("Prossessing Person: " + person + " Directory: /" + directory)
        for name in files:
            with open(os.path.join(root, name), 'rb') as fp:
                email = BytesParser(policy=default).parse(fp)
                email['Filename'] = name
                email['Person'] = person
                email['Directory'] = directory
                try:
                    writer.writerow(email)
                except Exception as e:
                    print("Error: Couldn't write email")
                    print(e)

print("-- DONE --")