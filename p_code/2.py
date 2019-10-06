import base64
encodestr = base64.b64encode('沈鑫阿斯顿'.encode('utf-8'))
print(str(encodestr,'utf-8'))
print(encodestr)

encodestr = base64.b64decode('XlNkVmtUI1MgXWBZXCFeKY+AaXNt')
flag = ''
for i in encodestr:
	flag  += chr((i-16)^32)
print(flag)