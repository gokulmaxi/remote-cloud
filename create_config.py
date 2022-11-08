#!/usr/bin/env python3


#!/usr/bin/env python3
import pymongo
from jinja2 import Template

myclient = pymongo.MongoClient(
    "mongodb://mongouser:mongoPass@localhost:27017/?authSource=admin"
)
mydb = myclient["mydatabase"]
mycol = mydb["users"]
template = """
 location /remote/{{OID}}/ {
   proxy_pass https://remote_{{roll}}:6901/;
   proxy_set_header Upgrade $http_upgrade;
   proxy_set_header Connection $connection_upgrade;
   add_header Cache-Control no-cache;
   # proxy_ssl_session_reuse off;
   # proxy_set_header Host $http_host;
   # proxy_cache_bypass $http_upgrade;
 }
 location /{{OID}}/websockify{
    proxy_pass https://remote_{{roll}}:6901/;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "Upgrade";
    proxy_set_header Host $host;}
    add_header Cache-Control no-cache;
"""
t = Template(template)
file1 = open("myfile.txt", "w")  # write mode
x = mycol.find()
for data in x:
    html = t.render({"OID": data["_id"], "roll": data["roll_no"]})
    file1.write(html)
    print(html)
