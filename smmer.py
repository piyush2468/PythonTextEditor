from __future__ import unicode_literals
from Tkinter import *
from tkFileDialog import *
import tkFont
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class MyBoard:





    def __init__(self,master):

       # self.g = open('depth_7.txt','w')
        self.eq=False
        self.current=""
        self.new_num=True
        f=tkFont.Font(size=25)
        topFrame=Frame(master)
        topFrame.pack()
        self.t=Text(topFrame,height=5,width=60,font=f)
        filename = None
        menubar = Menu(master)
        self.filemenu = Menu(menubar)
        self.filemenu.add_command(label="new", command=self.newfile)
        self.filemenu.add_command(label="open", command=self.openfile)
        self.filemenu.add_command(label="save", command=self.savefile)
        self.filemenu.add_command(label="save As...", command=self.saveAs)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="quit", command=root.quit)
        menubar.add_cascade(label="file",menu=self.filemenu)
        master.config(menu=menubar)

        self.t1=Button(topFrame,height=2,width=8,fg="white",bg="black",command=lambda : self.print_it("t1"))
        self.t2=Button(topFrame,height=2,width=8,fg="white",bg="black",command=lambda : self.print_it("t2"))
        self.t3=Button(topFrame,height=2,width=8,fg="white",bg="black",command=lambda : self.print_it("t3"))
        self.t4=Button(topFrame,height=2,width=8,fg="white",bg="black",command=lambda : self.print_it("t4"))
        self.t5=Button(topFrame,height=2,width=8,fg="white",bg="black",command=lambda : self.print_it("t5"))
        self.t6=Button(topFrame,height=2,width=8,fg="white",bg="black",command=lambda : self.print_it("t6"))
        self.t7=Button(topFrame,height=2,width=8,fg="white",bg="black",command=lambda : self.print_it("t7"))
        self.t8=Button(topFrame,height=2,width=8,fg="white",bg="black",command=lambda : self.print_it("t8"))
        self.t9=Button(topFrame,height=2,width=8,fg="white",bg="black",command=lambda : self.print_it("t9"))
        self.t10=Button(topFrame,height=2,width=8,fg="white",bg="black",command=lambda : self.print_it("t10"))
        self.t.grid(row=0,columnspan=10,sticky='EWNS')
        self.t1.grid(row=1,column=0,sticky='EWNS')
        self.t2.grid(row=1,column=1,sticky='EWNS')

        self.t3.grid(row=1,column=2,sticky='EWNS')

        self.t4.grid(row=1,column=3,sticky='EWNS')
        self.t5.grid(row=1,column=4,sticky='EWNS')
        self.t6.grid(row=1,column=5,sticky='EWNS')
        self.t7.grid(row=1,column=6,sticky='EWNS')
        self.t8.grid(row=1,column=7,sticky='EWNS')
        self.t9.grid(row=1,column=8,sticky='EWNS')
        self.t10.grid(row=1,column=9,sticky='EWNS')
        bottomFrame=Frame(master)
        bottomFrame.pack(side=BOTTOM)
        self.button1=Button(bottomFrame,text=u'\u0905',font=f,fg="white",bg="blue",command=lambda j=u'\u0905': self.printText(j))
        self.button2=Button(bottomFrame,text=u'\u0906',font=f,fg="white",bg="blue",command=lambda j=u'\u0906': self.printText(j))
        self.button3=Button(bottomFrame,text=u'\u0907',font=f,fg="white",bg="blue",command=lambda j=u'\u0907': self.printText(j))
        self.button4=Button(bottomFrame,text=u'\u0908',font=f,fg="white",bg="blue",command=lambda j=u'\u0908': self.printText(j))
        self.button5=Button(bottomFrame,text=u'\u0909',font=f,fg="white",bg="blue",command=lambda j=u'\u0909': self.printText(j))
        self.button6=Button(bottomFrame,text=u'\u090A',font=f,fg="white",bg="blue",command=lambda j=u'\u090A': self.printText(j))
        self.button7=Button(bottomFrame,text=u'\u090B',font=f,fg="white",bg="blue",command=lambda j=u'\u090B': self.printText(j))
        self.button8=Button(bottomFrame,text=u'\u090F',font=f,fg="white",bg="blue",command=lambda j=u'\u090F': self.printText(j))
        self.button9=Button(bottomFrame,text=u'\u0910',font=f,fg="white",bg="blue",command=lambda j=u'\u0910': self.printText(j))
        self.button10=Button(bottomFrame,text=u'\u0913',font=f,fg="white",bg="blue",command=lambda j=u'\u0913': self.printText(j))
        self.button11=Button(bottomFrame,text=u'\u0914',font=f,fg="white",bg="blue",command=lambda j=u'\u0914': self.printText(j))
        self.button12=Button(bottomFrame,text=u'\u0902',font=f,fg="white",bg="blue",command=lambda j=u'\u0902': self.printText(j))
        self.button13=Button(bottomFrame,text=u'\u0903',font=f,fg="white",bg="blue",command=lambda j=u'\u0903': self.printText(j))
        self.button14=Button(bottomFrame,text=u'\u094D',font=f,fg="white",bg="blue",command=lambda j=u'\u094D': self.printText(j))
        self.button15=Button(bottomFrame,text=u'\u0915',font=f,fg="white",bg="blue",command=lambda j=u'\u0915': self.printText(j))
        self.button16=Button(bottomFrame,text=u'\u0916',font=f,fg="white",bg="blue",command=lambda j=u'\u0916': self.printText(j))
        self.button17=Button(bottomFrame,text=u'\u0917',font=f,fg="white",bg="blue",command=lambda j=u'\u0917': self.printText(j))
        self.button18=Button(bottomFrame,text=u'\u0918',font=f,fg="white",bg="blue",command=lambda j=u'\u0918': self.printText(j))
        self.button19=Button(bottomFrame,text=u'\u0919',font=f,fg="white",bg="blue",command=lambda j=u'\u0919': self.printText(j))
        self.button20=Button(bottomFrame,text=u'\u091A',font=f,fg="white",bg="blue",command=lambda j=u'\u091A': self.printText(j))
        self.button21=Button(bottomFrame,text=u'\u091B',font=f,fg="white",bg="blue",command=lambda j=u'\u091B': self.printText(j))
        self.button22=Button(bottomFrame,text=u'\u091C',font=f,fg="white",bg="blue",command=lambda j=u'\u091C': self.printText(j))
        self.button23=Button(bottomFrame,text=u'\u091D',font=f,fg="white",bg="blue",command=lambda j=u'\u091D': self.printText(j))
        self.button24=Button(bottomFrame,text=u'\u091E',font=f,fg="white",bg="blue",command=lambda j=u'\u091E': self.printText(j))
        self.button25=Button(bottomFrame,text=u'\u0941',font=f,fg="white",bg="blue",command=lambda j=u'\u0941': self.printText(j))
        self.button26=Button(bottomFrame,text=u'\u0942',font=f,fg="white",bg="blue",command=lambda j=u'\u0942': self.printText(j))
        self.button27=Button(bottomFrame,text=u'\u0943',font=f,fg="white",bg="blue",command=lambda j=u'\u0943': self.printText(j))
        self.button28=Button(bottomFrame,text=u'\u091F',font=f,fg="white",bg="blue",command=lambda j=u'\u091F': self.printText(j))
        self.button29=Button(bottomFrame,text=u'\u0920',font=f,fg="white",bg="blue",command=lambda j=u'\u0920': self.printText(j))
        self.button30=Button(bottomFrame,text=u'\u0921',font=f,fg="white",bg="blue",command=lambda j=u'\u0921': self.printText(j))
        self.button31=Button(bottomFrame,text=u'\u0922',font=f,fg="white",bg="blue",command=lambda j=u'\u0922': self.printText(j))
        self.button32=Button(bottomFrame,text=u'\u0923',font=f,fg="white",bg="blue",command=lambda j=u'\u0923': self.printText(j))
        self.button33=Button(bottomFrame,text=u'\u0924',font=f,fg="white",bg="blue",command=lambda j=u'\u0924': self.printText(j))
        self.button34=Button(bottomFrame,text=u'\u0925',font=f,fg="white",bg="blue",command=lambda j=u'\u0925': self.printText(j))
        self.button35=Button(bottomFrame,text=u'\u0926',font=f,fg="white",bg="blue",command=lambda j=u'\u0926': self.printText(j))
        self.button36=Button(bottomFrame,text=u'\u0927',font=f,fg="white",bg="blue",command=lambda j=u'\u0927': self.printText(j))
        self.button37=Button(bottomFrame,text=u'\u0928',font=f,fg="white",bg="blue",command=lambda j=u'\u0928': self.printText(j))
        self.button38=Button(bottomFrame,text=u'\u0947',font=f,fg="white",bg="blue",command=lambda j=u'\u0947': self.printText(j))
        self.button39=Button(bottomFrame,text=u'\u0948',font=f,fg="white",bg="blue",command=lambda j=u'\u0948': self.printText(j))
        self.button40=Button(bottomFrame,text=u'\u093E',font=f,fg="white",bg="blue",command=lambda j=u'\u093E': self.printText(j))
        self.button41=Button(bottomFrame,text=u'\u092A',font=f,fg="white",bg="blue",command=lambda j=u'\u092A': self.printText(j))
        self.button42=Button(bottomFrame,text=u'\u092B',font=f,fg="white",bg="blue",command=lambda j=u'\u092B': self.printText(j))
        self.button43=Button(bottomFrame,text=u'\u092C',font=f,fg="white",bg="blue",command=lambda j=u'\u092C': self.printText(j))
        self.button44=Button(bottomFrame,text=u'\u092D',font=f,fg="white",bg="blue",command=lambda j=u'\u092D': self.printText(j))
        self.button45=Button(bottomFrame,text=u'\u092E',font=f,fg="white",bg="blue",command=lambda j=u'\u092E': self.printText(j))
        self.button46=Button(bottomFrame,text=u'\u092F',font=f,fg="white",bg="blue",command=lambda j=u'\u092F': self.printText(j))
        self.button47=Button(bottomFrame,text=u'\u0930',font=f,fg="white",bg="blue",command=lambda j=u'\u0930': self.printText(j))
        self.button48=Button(bottomFrame,text=u'\u0932',font=f,fg="white",bg="blue",command=lambda j=u'\u0932': self.printText(j))
        self.button49=Button(bottomFrame,text=u'\u0935',font=f,fg="white",bg="blue",command=lambda j=u'\u0935': self.printText(j))
        self.button50=Button(bottomFrame,text=u'\u0936',font=f,fg="white",bg="blue",command=lambda j=u'\u0936': self.printText(j))
        self.button51=Button(bottomFrame,text=u'\u094B',font=f,fg="white",bg="blue",command=lambda j=u'\u094B': self.printText(j))
        self.button52=Button(bottomFrame,text=u'\u094C',font=f,fg="white",bg="blue",command=lambda j=u'\u094C': self.printText(j))
        self.button53=Button(bottomFrame,text=u'\u0964',font=f,fg="white",bg="blue",command=lambda j=u'\u0964': self.printText(j))
        self.button54=Button(bottomFrame,text=u'\u0937',font=f,fg="white",bg="blue",command=lambda j=u'\u0937': self.printText(j))
        self.button55=Button(bottomFrame,text=u'\u0938',font=f,fg="white",bg="blue",command=lambda j=u'\u0938': self.printText(j))
        self.button56=Button(bottomFrame,text=u'\u0939',font=f,fg="white",bg="blue",command=lambda j=u'\u0939': self.printText(j))
        self.button57=Button(bottomFrame,text=u'\u2423',font=f,fg="white",bg="blue",command=lambda j=' ': self.printText(j))
        self.button58=Button(bottomFrame,text=u'\u232B',font=f,fg="white",bg="blue",command=self.deleteText)
        self.button59=Button(bottomFrame,text="cc",font=f,fg="white",bg="blue",command=self.deleteAllText)
        self.button60=Button(bottomFrame,text="->",font=f,fg="white",bg="blue",command=lambda j="\n": self.printText(j))
        self.button61 = Button(bottomFrame, text=u'\u0946', font=f, fg="white", bg="blue",
                               command=lambda j=u'\u0946': self.printText(j))
        self.button62 = Button(bottomFrame, text=u'\u093F', font=f, fg="white", bg="blue",
                               command=lambda j=u'\u093F': self.printText(j))
        self.button63 = Button(bottomFrame, text=u'\u0940', font=f, fg="white", bg="blue",
                               command=lambda j=u'\u0940': self.printText(j))
        bottomFrame.rowconfigure((0,1),weight=1)

        self.button1.grid(row=0,column=0,sticky='EWNS')
        self.button2.grid(row=0,column=1,sticky='EWNS')
        self.button3.grid(row=0,column=2,sticky='EWNS')
        self.button4.grid(row=0,column=3,sticky='EWNS')
        self.button5.grid(row=0,column=4,sticky='EWNS')
        self.button6.grid(row=0,column=5,sticky='EWNS')
        self.button7.grid(row=0,column=6,sticky='EWNS')
        self.button8.grid(row=0,column=7,sticky='EWNS')
        self.button9.grid(row=0,column=8,sticky='EWNS')
        self.button10.grid(row=0,column=9,sticky='EWNS')
        self.button11.grid(row=0,column=10,sticky='EWNS')
        self.button12.grid(row=0,column=11,sticky='EWNS')
        self.button13.grid(row=0,column=12,sticky='EWNS')
        self.button14.grid(row=1,column=0,sticky='EWNS')
        self.button15.grid(row=1,column=1,sticky='EWNS')
        self.button16.grid(row=1,column=2,sticky='EWNS')
        self.button17.grid(row=1,column=3,sticky='EWNS')
        self.button18.grid(row=1,column=4,sticky='EWNS')
        self.button19.grid(row=1,column=5,sticky='EWNS')
        self.button20.grid(row=1,column=6,sticky='EWNS')
        self.button21.grid(row=1,column=7,sticky='EWNS')
        self.button22.grid(row=1,column=8,sticky='EWNS')
        self.button23.grid(row=1,column=9,sticky='EWNS')
        self.button24.grid(row=1,column=10,sticky='EWNS')
        self.button25.grid(row=1,column=11,sticky='EWNS')
        self.button26.grid(row=1,column=12,sticky='EWNS')
        self.button27.grid(row=2,column=0,sticky='EWNS')
        self.button28.grid(row=2,column=1,sticky='EWNS')
        self.button29.grid(row=2,column=2,sticky='EWNS')
        self.button30.grid(row=2,column=3,sticky='EWNS')
        self.button31.grid(row=2,column=4,sticky='EWNS')
        self.button32.grid(row=2,column=5,sticky='EWNS')
        self.button33.grid(row=2,column=6,sticky='EWNS')
        self.button34.grid(row=2,column=7,sticky='EWNS')
        self.button35.grid(row=2,column=8,sticky='EWNS')
        self.button36.grid(row=2,column=9,sticky='EWNS')
        self.button37.grid(row=2,column=10,sticky='EWNS')
        self.button38.grid(row=2,column=11,sticky='EWNS')
        self.button39.grid(row=2,column=12,sticky='EWNS')
        self.button40.grid(row=3,column=0,sticky='EWNS')
        self.button41.grid(row=3,column=1,sticky='EWNS')
        self.button42.grid(row=3,column=2,sticky='EWNS')
        self.button43.grid(row=3,column=3,sticky='EWNS')
        self.button44.grid(row=3,column=4,sticky='EWNS')
        self.button45.grid(row=3,column=5,sticky='EWNS')
        self.button46.grid(row=3,column=6,sticky='EWNS')
        self.button47.grid(row=3,column=7,sticky='EWNS')
        self.button48.grid(row=3,column=8,sticky='EWNS')
        self.button49.grid(row=3,column=9,sticky='EWNS')
        self.button50.grid(row=3,column=10,sticky='EWNS')
        self.button51.grid(row=3,column=11,sticky='EWNS')
        self.button52.grid(row=3,column=12,sticky='EWNS')
        self.button53.grid(row=4,column=0,sticky='EWNS')
        self.button54.grid(row=4,column=1,sticky='EWNS')
        self.button55.grid(row=4,column=2,sticky='EWNS')
        self.button56.grid(row=4,column=3,sticky='EWNS')
        self.button57.grid(row=4,column=4,columnspan=3,sticky='EWNS')
        self.button58.grid(row=4,column=7,sticky='EWNS')
        self.button59.grid(row=4,column=8,sticky='EWNS')
        self.button60.grid(row=4,column=9,sticky='EWNS')
        self.button61.grid(row=4,column=10,sticky='EWNS')
        self.button62.grid(row=4,column=11,sticky='EWNS')
        self.button63.grid(row=4,column=12,sticky='EWNS')


    def printText(self, txt):
        g = open('depth_7.txt', 'w')
        self.t.insert(END,txt)
        if txt == ' ':
            pass
        else:
            s = self.t.get("1.0", "end-1c")
            s1 = s.rsplit(None,1)[-1]
            with open('depth_6.txt') as f:
                lines = f.read().splitlines()
            count=0
            for line in lines:
                if line.startswith(s1.encode('utf-8')):
                #print line[:-4]
                #with open('depth_7.txt','') as g:
                    g.write(line)
                    g.write("\n")
                    count=count+1
            g.close()
            f.close()
            with open('depth_7.txt') as g:

                lines1 = g.read().splitlines()
            self.t1["text"]=""
            self.t2["text"]=""
            self.t3["text"]=""
            self.t4["text"] = ""
            self.t5["text"] = ""
            self.t6["text"] = ""
            self.t7["text"] = ""
            self.t8["text"] = ""
            self.t9["text"] = ""
            self.t10["text"] = ""
            i=1
            flag = TRUE
            for line in lines1:
                flag = FALSE
                if i == 1:
                    self.t1["text"]=line[:-4]
                elif i == 2:
                    self.t2["text"]=line[:-4]

                elif i == 3:
                    self.t3["text"] = line[:-4]

                elif i == 4:
                    self.t4["text"] = line[:-4]

        #g.cloelif i==2:
                elif i == 5:
                    self.t5["text"] = line[:-4]
                elif i == 6:
                    self.t6["text"] = line[:-4]
                elif i == 7:
                    self.t7["text"] = line[:-4]
                elif i == 8:
                    self.t8["text"] = line[:-4]
                elif i == 9:
                    self.t9["text"] = line[:-4]
                elif i == 10:
                    self.t10["text"] = line[:-4]
                i=i+1

            g.close()
            if flag == TRUE:
                s = self.t.get("1.0", "end-1c")
                txt = s.rsplit(None, 1)[-1]
                self.search(self.t,txt,txt)
                self.t.tag_config(txt,foreground='red')

    def search(self,text_widget, keyword, tag):
        pos = '1.0'
        while True:
            idx = text_widget.search(keyword, pos, END)
            if not idx:
                break
            pos = '{}+{}c'.format(idx, len(keyword))
            text_widget.tag_add(tag, idx, pos)




    def deleteText(self):
        s=self.t.get("1.0","end-1c")
        s1=''
        for index in range(len(s)-1):
            s1=s1+s[index]
        self.t.delete("1.0",END)
        self.t.insert(END,s1)

    def deleteAllText(self):
        self.t.delete("1.0",END)

    def print_it(self,txt):
        s = self.t.get("1.0", "end-1c")
      #  #s.rsplit(' ',1)[0]
        s1 = ' '.join(s.split(' ')[:-1])
        if txt == "t1":
            s2 = self.t1["text"]
        elif txt == "t2":
            s2 = self.t2["text"]
        elif txt == "t3":
            s2 = self.t3["text"]
        elif txt == "t4":
            s2 = self.t4["text"]
        elif txt == "t5":
            s2 = self.t5["text"]
        elif txt == "t6":
            s2 = self.t6["text"]
        elif txt == "t7":
            s2 = self.t7["text"]
        elif txt == "t8":
            s2 = self.t8["text"]
        elif txt == "t9":
            s2 = self.t9["text"]
        elif txt == "t10":
            s2 = self.t10["text"]
        if s1 == '':
            s3=s2
        else:
            s3 = s1 +' '+ s2
        self.t.delete("1.0", END)
        self.t.insert(END, s3)

    def newfile(self):
        global filename
        filename= "untitled"
        self.t.delete(0.0,END)
    def savefile(self):
        global  filename
        txt = self.t.get(0.0,END)
        f=open(filename,'w')
        f.write(txt)
        f.close()
    def saveAs(self):
        f=asksaveasfile(mode='w',defaultextension='.txt')
        txt = self.t.get(0.0,END)
        f.write(txt.rstrip())

    def openfile(self):
        f= askopenfile(mode='r')
        txt=f.read()
        self.t.delete(0.0,END)
        self.t.insert(0.0,txt)

root=Tk()
k = MyBoard(root)

root.minsize(width=1000,height=570)
root.maxsize(width=1200,height=570)
root.mainloop()
