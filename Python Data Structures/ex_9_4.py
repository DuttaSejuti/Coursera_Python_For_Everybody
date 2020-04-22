#9.4 Write a program to read through the mbox-short.txt and
#figure out who has sent the greatest number of mail messages. The program looks for
#'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of
# times they appear in the file. After the dictionary is produced, the program reads through the dictionary
#using a maximum loop to find the most prolific committer.

fname=input('Enter the file name:')
handle=open(fname)
counts=dict()
for line in handle:
    if line.startswith('From '):
        #print(line)
        words=line.split()
        for word in words:
            counts[word]=counts.get(word,0)+1
#print(counts.items())
bigcount=None
bigword=None
for a,b in counts.items():
    if '@' in a:
        if bigcount is None or b>bigcount:
            bigword=a
            bigcount=b
print(bigword,bigcount)
