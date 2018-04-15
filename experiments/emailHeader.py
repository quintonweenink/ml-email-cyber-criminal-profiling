# Import the email modules we'll need
from email.parser import BytesParser, Parser
from email.policy import default

messagefile = "../maildir/maildir/allen-p/inbox/1."

# Read in email file:
with open(messagefile, 'rb') as fp:
    headers = BytesParser(policy=default).parse(fp)

#  Now the header items can be accessed as a dictionary:
print('To: {}'.format(headers['to']))
print('From: {}'.format(headers['from']))
print('Subject: {}'.format(headers['subject']))

# You can also access the parts of the addresses:
print('Recipient username: {}'.format(headers['to'].addresses[0].username))
print('Sender name: {}'.format(headers['from'].addresses[0].display_name))

# The email:
#print(headers)