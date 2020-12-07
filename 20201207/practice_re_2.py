'''
正则的步骤:
1、导入 re 模块
2、用 re.compile() 创建 匹配规则
3、使用 .search() 需要匹配的字符串,返回match对象
4、使用 .group() 返回匹配的字符串
'''

import re
'电话号码格式：415-555-4242'
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print('phone number found: ' + mo.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
# print(mo.group(1)) # 匹配括号第一组 415
# print(mo.group(2)) # 匹配括号第二组 555-4242
# print(mo.group(0)) # 匹配整个文本 415-555-4242
# print(mo.group()) # 匹配整个文本 415-555-4242
print(mo.groups()) # 获取所有分组，记得 group 后面' s ' ,('415', '555-4242')
areaCode,mainNumber = mo.groups()
print(areaCode,mainNumber)