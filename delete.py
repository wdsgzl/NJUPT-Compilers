together=[]
skip=0
word=[]
list=[]
storen=[]
now=0
ntogether=""
judge1=0
judge2=0
judge=[",",";","{","}"]
jisuan=["+","-","*","/","=",",",";","{","}","<","(",")","<"]
count=0
characther={
    "void":1,
    "main":2,
    "int":3,
    "cout":4,
    "return":5,
    "(":6,
    ")":7,
    "{":8,
    "}":9,
    "<<":10,
    ";":11,
    ",":12,
    "=":13,
    "*":14,
    "/":15
}
try:
    file = open("test.txt",encoding="utf-8")
except FileNotFoundError:
    print('File is not found')
else:
    element=file.readline().replace("\n","")
    together.append(element)
    while(element):
        element = file.readline().replace("\n","")
        # element = element.split(";")
        for i in range(len(element)-1):
            if element[i]=="/" and element[i+1]=="/":
                element=element[:i-1]
                break
        together.append(element)
    Temp1 = "".join(together)
    Temp2 = "".join(together)
    together = "".join(together)
    #rint(together)
    for i in range(len(together)-1):
        if together[i]=="/" and together[i+1]=="*":
            judge1=i
            Temp1 = Temp1[:judge1]
            break
    for i in range(len(together) - 1):
        if together[i]=="*" and together[i+1]=="/":
            judge2=i+2
            Temp2 = Temp2[judge2:]
            break
    together=Temp1+""+Temp2
    i = 0
    while i < len(together) - 1:
        if together[i] in jisuan and together[i+1] ==" ":
            ntogether += together[i]
            i += 2
        else:
            ntogether += together[i]
            i+=1
    if i == len(together) - 1:
        ntogether += together[i]
    print(ntogether)
    for r in ntogether:
        if skip:
            skip=0
            continue
        else:
            if r not in jisuan and r != " ":
                word.append(r)
            else:
                if word:
                    word="".join(word)
                    #print(word)
                    list.append(word)
                #print(list)
                if r != " " :
                    if r=="<":
                        word = []
                        word.append("<<")
                        word = "".join(word)
                        list.append(word)
                        skip=1
                    else:
                        word = []
                        word.append(r)
                        word = "".join(word)
                        list.append(word)
                word = []
    #print(list)
    storen = []
    storec = ""
    count = 0
    i = 0
    r = 0
    while r < len(list):
        if list[r] in characther:
                    print(r + 1, end='\t')
                    print(f"{characther[list[r]]}", end='\t')
                    print(list[r])
        elif list[r].isdigit():
                    print(r + 1, end='\t')
                    print(f"17", end='\t')
                    print(list[r])
        else:
            if list[r][0].isdigit() or list[r][0] in jisuan:
                m=r
                now=1
                count=0
                if list[r]==storec:
                    skip
                else:
                    storec=list[r]
                    storen.append(r+1)
                while list[m] !=";":
                    #print(count)
                    count=count+1
                    m=m+1
                count+=1
            else:
                print(r + 1, end='\t')
                print(f"16", end='\t')
                print(list[r])
        if now ==0:
            r = r + 1
        else:
            r=r+count
            now=0
    print("发现非法标识符：" + storec)
    print(f"位于源程序第{storen}个单词")




