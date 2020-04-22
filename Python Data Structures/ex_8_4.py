#8.4 Open the file romeo.txt and read it line by line.
#For each line, split the line into a list of words using the
#split() method. The program should build a list of words.
#For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
joined_lst2=list()
unique_lst3=list()
for line in fh:
    lst=line.rstrip()
    lsplit=lst.split()
    joined_lst2=lsplit+joined_lst2
#print(joined_lst2)
for word in joined_lst2:
    if word not in unique_lst3:
        unique_lst3.append(word)
#print(unique_lst3)
unique_lst3.sort()
print(unique_lst3)
