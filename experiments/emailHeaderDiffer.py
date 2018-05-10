# Import the email modules we'll need
import os
import re
import time
from email.parser import BytesParser, Parser
from email.policy import default

messagefile = "../../Project Resources/maildir"

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search
def findPartWord(w):
    return re.compile('({0})'.format(w), flags=re.IGNORECASE).search

def list_files(dir):
    r = []
    counter = 0
    for root, dirs, files in os.walk(dir):
        for name in files:
            # r.append(name)
            # Read in email file:
            with open(os.path.join(root, name), 'rb') as fp:
                headers = BytesParser(policy=default).parse(fp)
                # print(headers)
                if not findWholeWord("attachment is free")(format(headers['subject'])):
                    if findWholeWord("win")(format(headers['subject'])):
                        print('Subject: {}'.format(headers['subject']))
                        counter += 1
                    elif findWholeWord("free")(format(headers['subject'])):
                        print('Subject: {}'.format(headers['subject']))
                        counter += 1
                    elif findPartWord("\$")(format(headers['subject'])):
                        print('Subject: {}'.format(headers['subject']))
                        counter += 1
            #  Now the header items can be accessed as a dictionary:
            # print('To: {}'.format(headers['to']))
            # print('From: {}'.format(headers['from']))
            # print('Subject: {}'.format(headers['subject']))
            # counter += 1
    # return r
    return counter

# start_time = time.time()
print(list_files(messagefile))
# print("--- %s seconds ---" % (time.time() - start_time))

#
# # Read in email file:
# with open(messagefile, 'rb') as fp:
#     headers = BytesParser(policy=default).parse(fp)
#
# #  Now the header items can be accessed as a dictionary:
# print('To: {}'.format(headers['to']))
# print('From: {}'.format(headers['from']))
# print('Subject: {}'.format(headers['subject']))
#
# # You can also access the parts of the addresses:
# print('Recipient username: {}'.format(headers['to'].addresses[0].username))
# print('Sender name: {}'.format(headers['from'].addresses[0].display_name))
#
# # The email:
# #print(headers)
