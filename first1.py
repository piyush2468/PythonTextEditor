from __future__ import unicode_literals
from bs4 import BeautifulSoup
import urllib
import urllib2
import re
f2 = file('depth_4.txt','a')
f1 = file('depth_3.txt','r')
while True:
    url = f1.readline()
    if url =="" : break
    if url.startswith("http://") :
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)

        html = response.read()
    #else   :
     #   continue
#print html
#print html1


    #paragraphs = re.findall(r'<p>(.*?)</p>',str(html))
    #for eachp in paragraphs:
     #   print eachp
        soup = BeautifulSoup(html)

    # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()  # rip it out

        # get text
        text = soup.get_text()

    # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        f2.write(text.encode('utf-8'))
f1.close()
f2.close()