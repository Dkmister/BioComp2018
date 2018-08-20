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

def is_palindrome(seq):
	if seq == reverse_string(complementary_sequence(seq)):
		return True
	else:
		return False

def reverse_string(s):
	return s[::-1]

def substring_palindrome(l, crom):
	d = {}
	substr = []
	temp_str =""
	for line in crom:
		for i in range(0,len(line) - l):
			temp_str = line[i:i+l]
			substr.append(''.join(temp_str))
	for lin in substr:
		if is_palindrome(lin) == True:
			d[lin] = d.get(lin,0) + 1
	return d

cromossome7 = init_file("sequence.fasta")
#questao a:
#locate_diabetes(cromossome7,"CAGGAGATCTTCGTGGCCAC")
#questao b:
#print(is_palindrome("GC"))
#print(is_palindrome("ATATG"))
b = substring_palindrome(8,cromossome7)
print(b)
#questao d:
#qt_nuc = calculate_nucleotids(cromossome7)
#print(qt_nuc)
#questao e:
#seq = sequence_nucleotid_UFRGS("00242276")
#lst_s = create_different_sequences_E(seq)
#d = analyse_dna_seq(lst_s,cromossome7)

