import re

value = "d dog dogog 1231 2sdf dog sdgf12341 2sdfsd f2312 dogogog dogogog dogogog"

print(re.findall(r"\bd[og]{,4}\b", value))