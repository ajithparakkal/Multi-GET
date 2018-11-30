# Script that downloads part of a file from a web server, in chunks.
# reference URL used for HTTP requests {'http://docs.python-requests.org/'}

import requests, os, sys

# let the user choose an input URL
url = input("Enter the download URL: ")

# Function to download files in multiple Chunks
def file_download(url, output_path, chunk_size_bytes, total_size):
    # HTTP range function to request only first 4MiB of the file
    total_size = str(total_size-1) #converting to string for adding range
    headers = {'Range': 'bytes=0-'+total_size}
    try:
        # get request for the URL
        response = requests.get(url, stream=True, headers=headers)
    except requests.exceptions.MissingSchema:
        #exit if the URL is invalid
        print("Invalid URL")
        sys.exit()
        
    #creating output file name from url and output path
    file_name = os.path.basename(url) + ".part1"
    output_file_name = os.path.join(output_path, file_name)
    output_file = open(output_file_name, "wb")

    ## loop to download the file in multiple chunks of 1MiB size
    
    for chunk in response.iter_content(chunk_size=chunk_size_bytes):
        if chunk:
            output_file.write(chunk)
    output_file.close() 

#let the user choose 'no of chunks and chunk size'
input_string = "Enter no of chunks and chunksize(MiB) seperated by commas: "
try:
    chunk_no, chunk_size = tuple(map(int,input(input_string).split(',')))
except ValueError:
    #exit program if non integer values are entered
    print("Wrong values entered for chunks and/or chunksizes")
    sys.exit()

#calculating the chunk sizes(bytes) and total file size(bytes) for download    
chunk_size_bytes = chunk_size*1024*1024
total_size = chunk_size_bytes*chunk_no

# let the user choose an output file path
output_path = input("Enter path for saving downloaded file: ")
if os.path.exists(output_path):
    file_download(url, output_path, chunk_size_bytes, total_size)
else:
    #exit program if path doesnot exist
    print("Path doesnot exist")
    sys.exit()


