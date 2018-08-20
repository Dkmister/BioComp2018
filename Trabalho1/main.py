from init import *
from dna import *
from substring import *

def analyse_dna_seq(subseq,crom):
	d = {}
	for line in crom:
		for s in subseq:
			content = substring_occurence(line,s)
			if content[0]!=1:
				d[s] = d.get(s,0) + 1
	return d

def analyse_dna(subsequence,cromosse):
	i = 1
	for line in cromosse:
		for sub in subsequence:
			content = substring_occurence(line,sub)
			if  content[0]!=-1 and content != None:
				print("Found in line " + str(i))
				print(content[1])
		i+=1

def locate_diabetes(crom,snp):
	sub = create_all_possible_mutations(snp)
	print("Original sequence:\n"+snp)
	analyse_dna(sub,crom)

def calculate_nucleotids(crom):
	dic_nuc = {}
	for line in crom:
		for char in line:
			dic_nuc[char] = dic_nuc.get(char,0) + 1
	return dic_nuc



cromossome7 = init_file("sequence.fasta")
#questao a:
#locate_diabetes(cromossome7,"CAGGAGATCTTCGTGGCCAC")
#questao d
#qt_nuc = calculate_nucleotids(cromossome7)
#print(qt_nuc)
#questao e
seq = sequence_nucleotid_UFRGS("00242276")
lst_s = create_different_sequences_E(seq)
d = analyse_dna_seq(lst_s,cromossome7)
print(d)
