"""
#切片联系
name='孙昀'
idcard='362323199801071710'
print(name+'的生日为：',idcard[6:10]+'年'+idcard[10:12]+'月'+idcard[12:14]+'日')
"""

#分割字符串:默认为NONE，即所有的空字符（空格、换行'\n'，制表符'\t'等）
#分割字符串把字符串分割为列表，而合并字符串是把列表合并为字符串。
"""
fridends='@俞圣池 @程华飞 @涂慧 @徐志翔'
fridend1=fridends.split()
print(fridend1)
for fridend in fridend1:
    print(fridend[1:])
"""
"""
x='>@花花>@美丽>@哈哈'
print(x.split('>'))
#当一个分隔符出现多个，就会每个分隔一次，没有得到内容的，则产生一个空元素。
"""

#合并字符串 join（）
"""
s='@sun @yun @ni @hao'
print(s.count('@',0,6))
print(s.find("@",2,6))#默认从右边开始
print(s.rfind("@"))
print("#" in s)
print(s.index("sun"))
print(s.startswith('@'))
print(s.endswith("n",1,4))
"""

words='AbcDeFg'
print(words.lower())
print(words.upper())



