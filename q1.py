fname = input("Enter the file name:")
fh = open (fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count = count + 1 
        t = line.find('0')
        num = float (line[t:])
        total = total + num
average_spam = total/ count
print ('Average Spam Confidence:', average_spam)