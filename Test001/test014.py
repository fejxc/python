def printTable(tables):
    '''list=[]
    for i in tables:
        maxs=max([len(str) for str in i])
        list.append(maxs)
        #print(maxs)
    for i in range(len(tables[0])):
        for j in range(len(tables)):
            print(tables[j][i].rjust(list[j])+' ',end=" ")
        print()'''
    list=[]
    count=0  #用于计数，换行
    maxlens=[]  #存放列表中里面每个列表的字符最大长度
    for i in tables:  #遍历
         lens=max([len(str) for str in i])
         maxlens.append(lens)
    #print(max(maxlens))
    the_maxlen=max(maxlens) #或得该列表中字符串最大的长度
    for i in range(len(tables)+1):
        for j in tables:
             list=j
             print(list[i].rjust(the_maxlen,' ')+' ',end='')
             count=count+1
             if count%3==0:
                 print()

def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    printTable(tableData)

if __name__ == "__main__":
    main()