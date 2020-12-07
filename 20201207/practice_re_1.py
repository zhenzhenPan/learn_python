'''
不用正则 查找文本模式2
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

message = 'call me at 415-555-1011 tomorrow.415-555-9999 is my offic.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found:' + chunk)
print('done')