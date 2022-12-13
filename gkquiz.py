print("\u0330".join('''Hello,welcome to GK quiz '''))
a=input("Press enter to start quiz")
name=input("Type your name here"+"\u27A4")
users=open("user@.txt","r")
read=users.readlines()
users.close()
users=open("user@.txt","a")
if read==[]: #checking if the list is empty
    aa=0
else:
    for c in read:
        if name+"\n"==c:
            aa=1
            break
        else:
            aa=0
print("Hello "+"\u0330".join(name.capitalize()+" ")+"\n welcome to the quiz") #Printing the name
a=input("press enter to continue")
print("\n")
print('''[1] To start quiz type 1.
[2] To see your previous results type 2.
[3] To see someone else result type 3''')
cc=int(input("enter your choice (1, 2 or 3)"+"\u261E"))
print("\n")
if cc==1:
    print("Before begning of the quiz")
    print("read the following instruction"+"\u2BB7")
    print("\n"+"\u0332".join("Instructions:")+"\n")
    print("\u2BA9"+"This quiz contain 20 questions.")
    print("\u2BA9"+"Each question carry 5 points.")
    print("\u2BA9"+"For every correct answer, you will awarded 5 points.")
    print("\u2BA9"+"For every wrong answer, you will awarded -1 points.")
    print("\u2BA9"+"For every skipped question or input other than a,b,c or d, you will awarded 0 points.\n")
    a=input("\u2192"+"press enter to start the quiz"+"\u2190"+"\n")
    cor=inc=ski=0
    b=[]
    x="\u27F7"*49
    txt="\n"+"Type your answer here(a,b,c,d)\nor to skip, just click enter key"+"\u261E"
    print("\u0332".join("Question No 1:")+"\n"+"\u279C"+"Who is the current president of U.S.A ?\n")
    print('''(a)Donald John Trump          (b)Barack Hussein Obama
(c)Joseph Robinette Biden Jr  (d)Hillary Rodham Clinton''')
    ans=input(txt)
    if ans=="c":
        cor+=1
        b.append("c")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print("\n"+"\u0332".join("Question No 2:")+"\n"+"\u279C"+"Who is the father of computer ?\n")
    print('''(a)Blaise Pascal      (b)Nelson Mandela
(c)Charles Babbage    (d)Nikola Tesla''')
    ans=input(txt)
    if ans=="c":
        cor+=1
        b.append("c")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print("\n"+"\u0332".join("Question No 3:")+"\n"+"\u279C"+"In India, which state is largest in area ?\n")
    print('''(a)Uttar Pradesh      (b)Rajasthan
(c)Maharastra         (d)Madhya pradesh''')
    ans=input(txt)
    if ans=="b":
        cor+=1
        b.append("b")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print("\n"+"\u0332".join("Question No 4:")+"\n"+"\u279C"+"What is the name of our galaxy ?\n")
    print('''(a)Andromeda      (b)Milky way
(c)Cygnus         (d)Draco''')
    ans=input(txt)
    if ans=="b":
        cor+=1
        b.append("b")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print("\n"+"\u0332".join("Question No 5:")+"\n"+"\u279C"+"Which is the nearest galaxy to our galaxy ?\n")
    print('''(a)Andromeda galaxy     (b)Cygnus a
(c)Virgo a              (d)Cigar galaxy''')
    ans=input(txt)
    if ans=="a":
        cor+=1
        b.append("a")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print("\n"+"\u0332".join("Question No 6:")+"\n" "\u279C"+"What is full form of 'DC' in Washington DC ?\n")
    print('''(a)Distcrict Central      (b)District Corner
(c)District of Columbia   (d)District of Calafornia''')
    ans=input(txt)
    if ans=="c":
        cor+=1
        b.append("c")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print("\n"+"\u0332".join("Question No 7:")+"\n"+"\u279C"+"Which of the following is a operating system ?\n")
    print('''(a)Google      (b)Edge
(c)Linux       (d)Skype''')
    ans=input(txt)
    if ans=="c":
        cor+=1
        b.append("c")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print("\n"+"\u0332".join("Question No 8:")+"\n"+"\u279C"+"Who was the first person to land on the Moon?\n")
    print('''(a)Rakesh Sharma      (b)Sunita Williams
(c)Yuri Gagarin       (d)Neil Alden Armstrong''')
    ans=input(txt)
    if ans=="d":
        cor+=1
        b.append("d")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print("\n"+"\u0332".join("Question No 9:")+"\n"+"\u279C"+"Who was the first englismen to become President of INC ?\n")
    print('''(a)George Yule      (b)William Wedderburn
(c)Alfred Webb      (d)Henry Cotton''')
    ans=input(txt)
    if ans=="d":
        cor+=1
        b.append("d")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print("\n"+"\u0332".join("Question No 10:")+"\n"+"\u279C"+"When ISRO launched mangalyan into the space ?\n")
    print('''(a)14Nov2014      (b)27Aug2015
(c)2Dec2015       (d)5Nov2015''')
    ans=input(txt)
    if ans=="d":
        cor+=1
        b.append("d")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print("\n"+"\u0332".join("Question No 11:")+"\n"+"\u279C"+"The Indian National congress was formed in the year\n")
    print('''(a)1885      (b)2002
(c)1918      (d)1950''')
    ans=input(txt)
    if ans=="a":
        cor+=1
        b.append("a")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print("\n"+"\u0332".join("Question No 12:")+"\n"+"\u279C"+"What is full form of LPG ?\n")
    print('''(a)Lithium Propane Gas      (b)Liquid Propene Gas
(c)Liquefied Petroleum Gas  (d)Lithium Petroleum Gas''')
    ans=input(txt)
    if ans=="c":
        cor+=1
        b.append("c")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print("\n"+"\u0332".join("Question No 13:")+"\n"+"\u279C"+"Who is the present President of India ?\n")
    print('''(a)Pranab Kumar Mukherjee      (b)Manmohan Singh
(c)Narendra Damodardas Modi    (d)Ram Nath Kovind''')
    ans=input(txt)
    if ans=="d":
        cor+=1
        b.append("d")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print("\n"+"\u0332".join("Question No 14:")+"\n"+"\u279C"+"Who is the C.E.O. of Microsoft?\n")
    print('''(a)Pichai Sundararajan      (b)Satya Narayan Nandela
(c)Tim cook                 (d)Ratan Naval Tata''')
    ans=input(txt)
    if ans=="b":
        cor+=1
        b.append("b")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print("\n"+"\u0332".join("Question No 15:")+"\n"+"\u279C"+"The highest dam in India is \n")
    print('''(a)Tehri Dam      (b)Bhakra Nagal Dam
(c)Hirakud Dam    (d)Tungabhadra Dam''')
    ans=input(txt)
    if ans=="a":
        cor+=1
        b.append("a")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print("\n"+"\u0332".join("Question No 16:")+"\n"+"\u279C"+"When is the World Wild Week? \n")
    print('''(a)First week of September     (b)First week of October
(c)Last week of September      (d)Last week of October''')
    ans=input(txt)
    if ans=="b":
        cor+=1
        b.append("b")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print("\n"+"\u0332".join("Question No 17:")+"\n"+"\u279C"+"Who is the father of Geometry ?\n")
    print('''(a)Aristole      (b)Euclid
(c)Pythagoras    (d)Johannes Kepler''')
    ans=input(txt)
    if ans=="b":
        cor+=1
        b.append("b")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print("\n"+"\u0332".join("Question No 18:")+"\n"+"\u279C"+"The Indian to beat the computers in mathematical wizardry is \n")
    print('''(a)Srinivasa Ramanujan     (b)Shakuntala Devi
(c)Aryabhata               (d)Raja Ramanna''')
    ans=input(txt)
    if ans=="b":
        cor+=1
        b.append("b")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print("\n"+"\u0332".join("Question No 19:")+"\n"+"\u279C"+"What is common between diamond and graphite(pencil lead)\n")
    print('''(a)They both can conduct electricty    (b)Both can produce their own light
(c)Their constituent atom is carbon    (d)Both are edible''')
    ans=input(txt)
    if ans=="c":
        cor+=1
        b.append("c")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print("\n"+"\u0332".join("Question No 20:")+"\n"+"\u279C"+"Nirmala Sitharaman is the \n")
    print('''(a)current Finance Minister of India     (b)governer of Reserve Bank of India
(c)Defence Minister of India             (d)Minister of External Affairs of government of India''')
    ans=input(txt)
    if ans=="a":
        cor+=1
        b.append("a")
    elif ans=="":
        ski+=1
        b.append("skipped")
    else:
        inc+=1
        b.append(ans)
    print(x)
    print("\n"+"Thankyou for attending this quiz"+"\u263A")
    if aa==0:
        users.write(name+"\n")
        users.close()
    a=input("press enter to know your result \n")
    print("Total number of question"+"\u27A4"+"20")
    print("Total number of question answered correctly"+"\u27A4",cor)
    print("Total number of question answered wrong"+"\u27A4",inc)
    print("Total number of question skipped"+"\u27A4",ski,"\n")
    print("Overall total points"+"\u27A4",(cor*5)-(inc))
    b.append(str(cor))
    b.append(str(inc))
    b.append(str(ski))
    nam=name+".txt"
    save=open(nam,"w")
    for g in b:
        save.write(g+"\n")
    save.close()
    a=input("\nWant to know your answer per question,(Y/N)\n")
    ee=['c', 'c', 'b', 'b', 'a', 'c', 'c', 'd', 'd', 'd', 'a', 'c', 'd', 'b', 'a', 'b', 'b', 'b', 'c', 'a']
    if a=="Y" or a=="y":
        for f in range(20):
            m="Question No"+str(f+1)+":"
            print("\u0332".join(m))
            print("your answer :",b[f]," ,correct answer:",ee[f],"\n")
        print("Quiz ended")
    else:
        print("\nQuiz ended")
elif cc==2:
    if name+"\n" in read:
        print("Here is your previous result\n")
        opn=open(name+".txt","r")
        rd=opn.readlines()
        opn.close()
        print("Total number of question"+"\u27A4"+"20\n")
        print("Total number of question answered correctly"+"\u27A4",rd[20])
        print("Total number of question answered wrong"+"\u27A4",rd[21])
        print("Total number of question skipped"+"\u27A4",rd[22],"\n")
        print("Total points"+"\u27A4",int(rd[20])*5-int(rd[21]))
        a=input("\nWant to know your answer per question.(Y/N)")
        ee=['c', 'c', 'b', 'b', 'a', 'c', 'c', 'd', 'd', 'd', 'a', 'c', 'd', 'b', 'a', 'b', 'b', 'b', 'c', 'a'] 
        if a=="Y" or a=="y":
            for f in range(20):
                m="Question No"+str(f+1)+":"
                print("\u0332".join(m))
                print("Your answer :",rd[f],"correct answer :",ee[f],"\n")
            print("Quiz program ended")
        else:
            print("\nQuiz program ended")
    else:
        print("No previous record found \nBecause you have not attended quiz previously\nProgram ended")
elif cc==3:
    a=input("Type password")
    if a=="quizgk":
        print("Names of entry",read)
        bb=input("Type name")
        if bb+"\n" in read:
            print("\n")
            opn=open(bb+".txt","r")
            rd=opn.readlines()
            opn.close()
            print("Total number of question"+"\u27A4"+"20\n")
            print("Total number of question answered correctly"+"\u27A4",rd[20])
            print("Total number of question answered wrong"+"\u27A4",rd[21])
            print("Total number of question skipped"+"\u27A4",rd[22],"\n")
            print("Total points"+"\u27A4",int(rd[20])*5-int(rd[21]))
            a=input("\nWant to know your answer per question.(Y/N)")
            ee=['c', 'c', 'b', 'b', 'a', 'c', 'c', 'd', 'd', 'd', 'a', 'c', 'd', 'b', 'a', 'b', 'b', 'b', 'c', 'a'] 
            if a=="Y" or a=="y":
                for f in range(20):
                    m="Question No"+str(f+1)+":"
                    print("\u0332".join(m))
                    print("Your answer :",rd[f],"correct answer :",ee[f],"\n")
                print("Quiz program ended")
            else:
                print("\nQuiz program ended")
        else:
            print("No such record found \nProgram ended")
    else:
        print("password is wrong \nProgram ended")
else:
    print("wrong choice \nQuiz program ended")
