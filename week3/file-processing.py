import os

infile = open(os.path.expanduser("~/Downloads/junk.txt"), "r")

lines = infile.readlines()
lines.append("text file nanalyssis\n")

for line in lines:
  line = line.lower()
  print(line[0:-1])

# number of lines 
print("\nTotal number of lines: ", len(lines))

infile.close()