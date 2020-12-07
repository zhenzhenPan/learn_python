'''
不用正则 查找文本模式
str.isdecimal() ---- 检查字符串是否只包含十进制字符
code from automate the boring stuff with python
'''

def isPhoneNumber(text):
    if len(text) != 12:
       return False
    for  i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))


