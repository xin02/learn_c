import re
import requests

req = requests.get(input('输入虎牙直播URL:'))
req.text
pattern = re.compile(r'sStreamName":"(.*?)","sFlvUrl(.*?)sHlsUrl":"(.*?)","sHlsUrlSuffix')   # 查找数字
a = pattern.findall(req.text)[0][0]
b = pattern.findall(req.text)[0][2]
b = re.sub(r'\\',"", b)

print(b + '/' + a + '.m3u8')