from main import *

c7 = init_file("sequence.fasta")

c = substring_n(37,c7)
with open("questaoc.txt",'w') as f:
	for k,v in c.items():
		f.write("Substring: %s :=> Ocorrencias(s): %d",%(k,v))
	f.close()
