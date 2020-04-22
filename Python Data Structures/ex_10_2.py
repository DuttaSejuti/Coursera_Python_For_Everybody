#10.2 Write a program to read through the mbox-short.txt and figure out
#the distribution by hour of the day for each of the messages. You can pull the hour out from the
# 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname=input('Enter file name:')
hand=open(fname)
counts=dict()
for line in hand:
    if line.startswith('From '):
        a=line.split()
        b=a[5].split(':')
        #print(b[0])
        c=b[0].split()
        #print(c)
        for hours in c:
            counts[hours]=counts.get(hours,0)+1
for key,val in sorted(counts.items()):
    print(key,val)
