# Multi-GET
#App that downloads part of a file from a web server, in chunks.

#Language:
Python 3.6.7

#Build details(OS):
macosx-10.9-x86_64

#Specific App Requirements added:

1. Source URL should be specified with a required command-line option
2. File is downloaded in 4 chunks (4 requests made to the server)
3. Only the first 4 MiB of the file should be downloaded from the server
4. Output file may be specified with a command-line option
5. No corruption in file - correct order, correct size, correct bytes
6. File is retrieved with GET requests
7. Support files smaller than 4 MiB (less chunks/adjust chunk size)
8. Configurable number of chunks/chunk size/total download size

#Test URL:
http://f39bf6aacedfcf.bwtest-aws.pravala.com/384MB.jar


#References:
http://docs.python-requests.org/

