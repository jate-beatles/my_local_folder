import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
###Input the url to parse
url = input('Enter- URL')
c = int(input('Enter count'))
po =int( input('Enter position'))

for i in range(c):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = 0
    for tag in tags:
        count = count +1
   
        #make it stop at position 3#
        if count>po:
            break
        url = tag.get('href', None)

print(url)


g
