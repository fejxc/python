import pandas as pd
# orderDict={1809102021:'孙昀',1809102001:'李志'}
stu = pd.read_csv('stu.csv')
stuDict= dict(stu.values)
print(stuDict)
# print(orderDict.get(1809102021))
dataByName = pd.read_csv('18计算机2班考勤统计byName.csv')
dataById = pd.read_csv('18计算机2班考勤统计byId.csv')
# print(dataById)
resByName = dataByName.values
resById = dataById.values


dictByName = dict(resByName)
dictById = dict(resById)
#print(res)
# print(dictByName)
# count1 = dictByName.get('孙昀')
# print(count1)
# print(dictById)
# count2 =dictById.get(1809102021)
# print(count2)

print('查询单个同学的出勤次数：输入1根据姓名，输入2根据id')

i=int(input())
if i == 1:
    print('请输入你要查询的姓名：')
    name = input()
    count3 = dictByName.get(name)
    print(count3)
if i == 2:
    print('请输入你要查询的学号：')
    id = int(input())
    stuName = stuDict.get(id)
    count4 = dictById.get(id)
    print('姓名:'+stuName+' 学号:'+str(id)+' 共出勤'+str(count4)+'次')
