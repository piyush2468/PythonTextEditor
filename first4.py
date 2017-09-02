file=open("depth_5_1.txt","r")
file1=open("depth_6.txt","w")
wordcount={}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
t = 0
for (k,v) in wordcount.items():


    file1.write(k)

    file1.write(" - ")
    file1.write(str(v))
    file1.write("\n")
    t=t+1

print t
file.close()
file1.close()