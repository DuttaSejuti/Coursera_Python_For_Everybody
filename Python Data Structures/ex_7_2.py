#7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
#looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and
 #compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
fname = input("Enter file name: ")
fh = open(fname)
count=0
tot=0
for line in fh:
    l=line.rstrip()
    if  l.startswith("X-DSPAM-Confidence:") :
        pos=l.find(':')
        num=l[pos+1:]
        data=float(num)
        tot=tot+data
        count=count+1
        avg=float(tot/count)
print('Average spam confidence:',avg)
