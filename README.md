# Multi-GET
#App that downloads part of a file from a web server, in chunks.

#Language:
Python 3.6.7

#Build details(OS):
macosx-10.9-x86_64

#Specific App Requirements added:

• Source URL should be specified with a required command-line option
• File is downloaded in 4 chunks (4 requests made to the server)
• Only the first 4 MiB of the file should be downloaded from the server
• Output file may be specified with a command-line option
• No corruption in file - correct order, correct size, correct bytes
• File is retrieved with GET requests


#References:
http://docs.python-requests.org/en/latest/

