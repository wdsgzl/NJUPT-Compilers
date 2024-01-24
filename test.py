while r < len(list):
    if now == 0:
        if list[r] in characther:
            print(r + 1, end='\t')
            print(f"{characther[list[r]]}", end='\t')
            print(list[r])
        elif list[r].isdigit():
            print(r + 1, end='\t')
            print(f"17", end='\t')
            print(list[r])
        else:
            print(r + 1, end='\t')
            print(f"16", end='\t')
            print(list[r])
    else:
        if list[r][0].isdigit():
            storen.append(r + 1)
            storec = list[r]
            count = count + 1
            if count != 1:
                now = 1
                i = r
                while list[i] != ";":
                    print("删除" + list[i])
                    list.pop(i)
                    # r=r+1
                    if list[i] == ";":
                        print("删除" + list[i])
                        list.pop(i)
                        break
                    else:
                        i = i + 1
        else:
            print(r + 1, end='\t')
            print(f"16", end='\t')
            print(list[r])
    r = r + 1

print("发现非法标识符：" + storec)
print(f"位于源程序第{storen}个单词")