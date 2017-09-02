file=open("depth_4.txt","r")
file1=open("depth_5.txt","w")
wordcount={}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
t=0
for (k,v) in wordcount.items():
        #s1=""
        #if k.endswith("."):
         #   for index in range(len(k) - 1):
          #      s1 = s1 + k[index]
           #     file1.write(s1)
        #elif k.endswith(","):
         #   for index in range(len(k) - 1):
          #      s1 = s1 + k[index]
           #     file1.write(s1)
        #elif k.endswith(".."):
         #   for index in range(len(k) - 2):
          #      s1 = s1 + k[index]
           #     file1.write(s1)
        #elif k.endswith("..."):
         #   for index in range(len(k) - 3):
          #      s1 = s1 + k[index]
           #     file1.write(s1)
        #elif k.endswith("!"):
         #   for index in range(len(k) - 1):
          #      s1 = s1 + k[index]
           #     file1.write(s1)
        #elif k.endswith('[0-9]'):
         #   for index in range(len(k) - 1):
          #      s1 = s1 + k[index]
           #     file1.write(s1)

        file1.write(k)

        file1.write(" - ")
        file1.write(str(v))
        file1.write("\n")
        t=t+1
print t
file.close()
file1.close()