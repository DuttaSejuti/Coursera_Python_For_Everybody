import re
fi=open('regex_sum_419984.txt')
total=0
numlist=list()
for line in fi:
    line=line.rstrip()
    y=re.findall('([0-9]+)',line)
    if not y:
        continue
    else:
        for num in y:
            print(num)
            total=total+int(num)

print('sum:',total)
