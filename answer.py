fname = input("Enter the file name: ")
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if line.endswith("2008") and '@' in line:
        line = line.split()
        mail = line[1]
        print(mail)
        count += 1
    else:
        continue        
        
print("Count: ", count)