import os
import sys
import requests
import zipfile

server_url = "https://xilinx-staging.fluidtopics.net/api/admin/khub/sources/ftml/upload"
HEADERS = {'FT-Authorization': 'Basic DsxpPQX26uW7BlqFZfc4K6jqH6grWobn' }

zf = zipfile.ZipFile('techdocs.zip', "w")
for dirname, subdirs, files in os.walk("./build/html"):
    zf.write(dirname)
    for filename in files:
        print(filename)
        zf.write(os.path.join(dirname, filename))
zf.close()

fileobj = open ('techdocs.zip', 'rb')
r = requests.post(server_url, headers=HEADERS, files={"archive": ('techdocs.zip', fileobj)})
            
