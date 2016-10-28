import csv
from Queue import * 

f=open('four.csv','rb')
reader=csv.reader(f)
lst=[]
lst=list(reader)

dic= open('four.csv','rb')
reader=csv.reader(dic)
d=list(reader)

out=open('4ladders.csv','wb')
writer=csv.writer(out)

master=open('analysis.csv','ab')
masterwriter=csv.writer(master)
#source=0
#target=1




alpha=['A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num_words=len(d)  #number of words in the dictionary
#while source != num_words:  #while source index has not reached the end of the list
for source in range(0, len(lst)-1):
	for target in range(source+1,len(lst)): 
		q=Queue(maxsize=0)
		used=[]
		src_word=lst[source]
		trgt_word=lst[target]
		q.put(src_word)
		findword="".join(trgt_word)
		while not q.empty():
			ladder=q.get()
			lastword=ladder[-1]
			if not (lastword in used):
				used.append(lastword)

				if lastword == findword:
					
					writer.writerow(ladder)
					ladderlength=len(ladder)
					masterwriter.writerow([ladderlength])
					break
				else:
					letters=list(lastword)
					for ch in range(len(lastword)):
						for l in alpha:
							letters[ch]=l
							word="".join(letters)
							if [word] in d and not(word in used):
								newladder=list(ladder)
								print ladder
								newladder.append(word)
								q.put(newladder)


							






			
