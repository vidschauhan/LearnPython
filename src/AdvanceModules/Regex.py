# Created by vidit.singh at 10-03-2022

string1 = "My zip code is (323)-23-2332"
pattern = r"(\d{3})-\d{2}-\d{4}"

import re

print(re.findall(pattern, string1))
op = re.search(pattern, string1)
print(op)

match = re.search("code", string1)
print(match)

print(match.span())  # return index
print(re.findall("zip", string1))

for m in re.finditer("code", string1):
    print(m.group())
