'''
正则 --- 使用管道 '|' 匹配多个分组
eg: r'Batman|Tina Fey' 表示 匹配 Batman 或者 Tina Fey,匹配到一个就停止搜索

'''

import re
# 第一种：匹配一次
# heroRegex = re.compile(r'Batman|Tina Fey')
# mo1 = heroRegex.search('Batman and Tina Fey')
# print(mo1.group()) # Batman

# 第二种：匹配 Batman or Batmobile or Batcopter or Batbat
# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
# print(mo.group()) # Batmobile ,匹配整个文本
# print(mo.group(1)) # mobile ,匹配第一个文本

# 第三种：使用 ()? -- 可选分组，?前括号里的 内容 出现 0次 或 1次
# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group()) # Batman
#
# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group()) # Batwoman

# 第四种：使用 ()* -- * 前括号里的 内容 出现 0次 或 多次
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group()) # Batman

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group()) # Batwoman

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group()) # Batwowowowoman