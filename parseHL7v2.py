rf = open('.\\raw.hl7v2', 'r')
wf = open('.\\parseOut.hl7v2', 'w')

##linein = line.replace('~',' - ') #rf.readline()
##segments = linein.split("*")
##print(segments.index)


for line in rf: 
     linein = line #line.replace('|','| - ') #rf.readline()
     segments = linein.split("|")
     #print(segments.index)
     wf.write(line)
     for seg in segments:
          wf.write('\t')
          wf.write(seg)
          if len(seg) == 0:
               wf.write('| - (skip) \n')
          else: 
               wf.write('| - \n')

wf.close()
rf.close()
