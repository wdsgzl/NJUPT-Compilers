together=[]
judge=[",",";","{","}"," "]
jisuan=["+","-","*","/","=",",",";","{","}","<","(",")"]
try:
    file = open('test.txt',encoding="utf-8")#打开文件
except FileNotFoundError:
    print('File is not found')#若文件不存在则爆错
else:#若文件打开成功则


    element=file.readline().replace('\n',"")
    together.append(element)
    element = element.split()


    while(element):
        #print(element)

        element = file.readline().replace('\n', ' ')

        element = element.split()
        for ele in element:
            if not ele.startswith("/") and not ele.endswith("/"):
                together.append(element)


    # for i in range(len(together)):
    print(together)
    for i in range(len(together)):
        if i ==0:
            print(together[i], end=' ')
        else:
            print(together[i], end='')
    together="".join(together)
    print(together)
    Output=[]
    Temp=[]
    #together = together.split("=")
    for i in range(len(together)):

        if together[i] not in jisuan:
            Temp.append(together[i])
        elif together[i]=="/" and together[i+1]=="/":
                Temp.append(together[i])
        else:
            Temp = "".join(Temp)
            Output.append(Temp)
            Output.append(together[i])
            Temp = []
    print(Output)




