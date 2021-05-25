import pandas as pd


#file_name = '0{}.csv'
file_name = '18-3_20210512_0{}.csv'
df_list = []
for i in range(1, 3):
    #data = pd.read_csv(file_name.format(i))
    df_list.append(pd.read_csv(file_name.format(i)))
df = pd.concat(df_list)

#print(df_list)
print(df)
#print(type(df))
print(df.value_counts())
all_date_count = df.value_counts()
#f = df.loc[df.duplicated(subset=['学号'], keep=False), :]
#print(type(all_date_count))

d4 = df.groupby('姓名')['学号'].count().reset_index(name='出勤次数')
d5 = df.groupby('学号')['姓名'].count().reset_index(name='出勤次数')
print(d4)
print(d5)
# ascending=True 升序排列
d1 = df['学号'].value_counts(ascending=True)
d2 = df['姓名'].value_counts(ascending=True)
#print(d1)
#print(type(d2))
#print(d2)


# d4.to_csv("18计算机2班考勤统计byName.csv", index=False, header=True, encoding='utf-8')
# d5.to_csv("18计算机2班考勤统计byId.csv", index=False, header=True, encoding='utf-8')
df.to_csv("18计算机3班考勤统计表汇总.csv", index=False, header=True, encoding='utf-8')

d4.to_csv("18计算机3班考勤统计byName.csv", index=False, header=True, encoding='utf-8')
d5.to_csv("18计算机3班考勤统计byId.csv", index=False, header=True, encoding='utf-8')



