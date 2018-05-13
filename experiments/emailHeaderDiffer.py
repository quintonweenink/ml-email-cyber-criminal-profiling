# Import the email modules we'll need
import os
import re
import time
import sys

from shutil import copy2
from email.parser import BytesParser, Parser
from email.policy import default


cwd = os.getcwd()
messagefile = cwd+"/../../project-resources/maildir"
# print(messagefile)
spamWords = cwd+"/spamWords.txt"
f = open(spamWords)
lines = f.read().splitlines()
f.close()

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search
def findPartWord(w):
    return re.compile('({0})'.format(w), flags=re.IGNORECASE).search
def hasNumbers(w):
    return any(char.isdigit() for char in w)

def list_files(dir):
    r = []
    counter = 0
    for root, dirs, files in os.walk(dir):
        for name in files:
            # r.append(name)
            # Read in email file:
            with open(os.path.join(root, name), 'rb') as fp:
                headers = BytesParser(policy=default).parse(fp)
                src = os.path.join(root, name)
                pos = src.find('maildir')
                dest = root[:pos] + 'copy' + root[pos:]

                pos = dest.find('Project/experiments')
                dest = dest[:pos] + dest[pos+26:]

                # print(src)
                # print(dest)
                # print(headers)
                if not findWholeWord("attachment is free")(format(headers['subject'])):
                    for phrase in lines:
                        if findWholeWord(phrase)(format(headers['subject'])):
                            print('Subject: {}'.format(headers['subject']) + ': ' + phrase)
                            counter += 1
                            continue
                    # if hasNumbers((format(headers['from']))):
                    #     print('From: {}'.format(headers['from']))
                    #     counter += 1
                    # if findWholeWord("win")(format(headers['subject'])):
                    #     print('Subject: {}'.format(headers['subject']))
                    #     if not os.path.exists(dest):
                    #         os.makedirs(dest)
                    #         copy2(src, dest)
                    #     counter += 1
                    # elif findWholeWord("free")(format(headers['subject'])):
                    #     print('Subject: {}'.format(headers['subject']))
                    #     if not os.path.exists(dest):
                    #         os.makedirs(dest)
                    #         copy2(src, dest)
                    #     counter += 1
                    # elif findPartWord("\$")(format(headers['subject'])):
                    #     print('Subject: {}'.format(headers['subject']))
                    #     if not os.path.exists(dest):
                    #         os.makedirs(dest)
                    #         copy2(src, dest)
                    #     counter += 1
            #  Now the header items can be accessed as a dictionary:
            # print('To: {}'.format(headers['to']))
            # print('From: {}'.format(headers['from']))
            # print('Subject: {}'.format(headers['subject']))
            # counter += 1
    # return r
    return counter

# start_time = time.time()
print(list_files(messagefile))
sys.stdout.write('\a')
sys.stdout.flush()
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
