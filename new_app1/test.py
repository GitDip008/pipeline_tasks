import re

l = 'Jul 18 17:33:36 elk-anis-test kernel: Decoding supported only on Scalable MCA processors.'

p1 = r'[a-zA-Z]{1,3}\s[0-9]{1,2}\s[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}'

p2 = r't[\s][a-zA-Z-]+\[|t[\s][a-zA-Z-]+:'
# x = re.findall(p2, l)
# print(x[0][0:-1])
p_msg = r':\s[a-zA-z\s]*'
message = re.findall(p_msg, l)[0][2:]
print(message)