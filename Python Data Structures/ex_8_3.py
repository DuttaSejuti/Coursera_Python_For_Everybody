fname=input("Enter the file name:")
fh=open(fname)
count=0
for line in fh:
    line=line.rstrip()
    wrds=line.split()
    if wrds[0]== 'From ':
        count=count+1
        print(wrds[1])
print("There were", count, "lines in the file with From as the first word")
