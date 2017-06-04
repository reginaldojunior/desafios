import re

out = open("out.txt", "w")

lineCurrent = ""
i = 0
with open("input.txt", "r") as _input:    
    for line in _input:
        words = re.split('\s+', line)

        for word in words:
            nextInteration = False
           
            stringAfterInteration = lineCurrent

            if len(lineCurrent.rstrip()) <= 40:
                lineCurrent += word + " "
            
            stringNextInteration = lineCurrent + word

            if (len(stringNextInteration) > 40):
                nextInteration = True

            if nextInteration is True:
                if (len(lineCurrent.rstrip()) == 40):
                    outLine = lineCurrent.rstrip()
                    lineCurrent = ""
                
                if (len(stringAfterInteration.rstrip()) <= 40):
                    outLine = stringAfterInteration.rstrip()
                    lineCurrent = word + " "

                out.write(outLine)
                out.write('\n')

out.close()