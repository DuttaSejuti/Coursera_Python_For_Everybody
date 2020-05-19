import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
uh = urllib.request.urlopen(address, context=ctx)


data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

lst=tree.findall('.//count')
print('Comments Count:',len(lst))
print(lst)
sum=0
for item in lst:
    num=item.text
    sum=sum+int(num)
print(int(sum))
