rf = open('.\\raw.837', 'r')
wf = open('.\\parseOut.837', 'w')

##linein = line.replace('~',' - ') #rf.readline()
##segments = linein.split("*")
##print(segments.index)


for line in rf: 
     linein = line.replace('~',' - ') #rf.readline()
     segments = linein.split("*")
     print(segments.index)
     wf.write(line)
     for seg in segments:
          wf.write('\t')
          wf.write(seg)
          wf.write(' - \n')

wf.close()
rf.close()
