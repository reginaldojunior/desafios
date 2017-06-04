import re

out = open("out.txt", "w")

last = 40
lineString = ""
with open("input.txt", "r") as _input:
    
    for line in _input:
        words = re.split('\s+', line)

        for word in words:
            if len(lineString) <= 40:
                lineString += word + " "
            else:
                out.write("\n")
                out.write(lineString)
                lineString = ""

        out.write("\n")

out.close()