out = open("out.txt", "w")

last = 40
with open("input.txt", "r") as _input:
    for line in _input:
        for i in range(len(line)):
            if i % 40 == 0:
                outtxt = line[last:i]
                last = i
                out.write(outtxt)
                out.write("\n")

out.close()