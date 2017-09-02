import re, urllib

textfile = file('depth_3.txt','wt')
#print "Enter the URL you wish to crawl.."
#print 'Usage  - "http://zeenews.india/" <-- With the double quotes'
myurl ="http://www.jansatta.com/"
#myurl1="http://khabar.ndtv.com"
for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(myurl).read(), re.I):
        print i
        for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
                print ee
                textfile.write(ee+'\n')
#for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(myurl1).read(), re.I):
        #print i
        #for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
               # print ee
              #  textfile.write(ee+'\n')
textfile.close()