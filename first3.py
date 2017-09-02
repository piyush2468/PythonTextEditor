import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

g = open("depth_5_1.txt","w")
with open("depth_5.txt","r") as f:
    lines=f.read().splitlines()
for line in lines:
    nstr = re.sub(r'[?|$|.|!]',r'',line)
    nestr = re.sub(r'[a-z ,-- / ~ $ # A-Z {{ }} ! ; ) ( _ '' ` < > | : 0-9 \']',r'',nstr)#print nestr
    g.write(nestr)
    g.write("\n")
g.close()
f.close()


