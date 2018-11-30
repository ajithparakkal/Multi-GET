# Script that downloads part of a file from a web server, in chunks.
# reference URL for HTTP requests{'http://docs.python-requests.org/en/latest/'}

import requests, os

# let the user choose an input URL
url = input("Enter the download URL: ")

# Function to download files in multiple Chunks
def file_download(url, output_path):
    # HTTP range function to request only first 4MiB of the file
    headers = {'Range': 'bytes=0-3999999'} 
    try:
        # get request for the URL
        response = requests.get(url, stream=True, headers=headers)
    except requests.exceptions.MissingSchema:
        #exit if the URL is invalid
        print("Invalid URL")
        exit()
        
    #creating output file name from url and output path and appending 'part1' to it
    file_name = os.path.basename(url) + ".part1"
    output_file_name = os.path.join(output_path, file_name)
    output_file = open(output_file_name, "wb")

    ## loop to download the file in multiple chunks of 1MiB size from response
    for chunk in response.iter_content(chunk_size=1000000):
        if chunk:
            output_file.write(chunk)
    output_file.close() 

# let the user choose an output file path
output_path = input("Enter path for saving downloaded file: ")
if os.path.exists(output_path):
    file_download(url, output_path)
else:
    print("Path doesnot exist")
    exit()


