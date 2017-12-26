# base64 编码
将文件中的字符按行进行base64编码并输出到标准输出
## 转换格式
### dos格式（\r\n结尾）转换为unix格式（\n结尾）
dos2unix ./words.txt
### 将编码格式转换为UTF-8
iconv -f GB18030 -t UTF-8 ./words.txt > words_utf.txt
