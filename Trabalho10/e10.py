import numpy as np

def freq_dict_of_arrays(dna_list):
	n = max([len(dna) for dna in dna_list])
	frequency_matrix = {base:np.zeros(n,dtype=np.int)
						for base in 'ACGT'}
	for dna in dna_list:
		for i, base in enumerate(dna):
			frequency_matrix[base][i]+=1
			
	return frequency_matrix
	

def consensus_string(frequency_matrix):
	base2index = {'A':0,'C':1,'G':2,'T':3}
	consensus = ''
	dna_length = len(frequency_matrix['A'])
	
	for i in range(dna_length):
		max_freq = -1
		max_freq_base = None
		
		for base in 'ATCG':
			if frequency_matrix[base][i] > max_freq:
				max_freq = frequency_matrix[base][i]
				max_freq_base = base
			elif frequency_matrix[base][i] == max_freq:
				max_freq_base = '-'
				
		consensus += max_freq_base
	return consensus
	
#----Receive a string, returns a list of all substring of size n
#_______________________________________________________________
def create_size_n_substrings(str,n):
	lst_n_substrings = []
	for i in range(len(str) - n):
		lst_n_substrings.append(str[i:i+n])
	return lst_n_substrings



lst_sqc = ["cctgatagacgctatctggctatccacgtacataggtcctctgtgcgaatctatgcgtttccaaccat","agtactggtgtacatttgatacgtacgtacaccggcaacctgaaacaaacgctcagaaccagaagtgc","aaaagtccgtgcaccctctttcttcgtggctctggccaacgagggctgatgtataagacgaaaatttt", "agcctccgatgtaagtcatagctgtaactattacctgccacccctattacatcttacgtacgtataca","ctgttatacaacgcgtcatggcggggtatgcgttttggtcgtcgtacgctcgatcgttaacgtaggtc"]

sub3 = []
sub5 = []
sub8 = []
for s in lst_sqc:
	sub3.append(create_size_n_substrings(s,3))
	sub5.append(create_size_n_substrings(s,5))
	sub8.append(create_size_n_substrings(s,8))
	

f3 = []
f5 = []
f8 = []

for l in sub3:
	for s in l:
		f3.append(s.upper())
for l in sub5:
	for s in l:
		f5.append(s.upper())
for l in sub8:
	for s in l:
		f8.append(s.upper())
		
fr3 = freq_dict_of_arrays(f3)
c3 = consensus_string(fr3)
fr5 = freq_dict_of_arrays(f5)
c5 = consensus_string(fr5)
fr8 = freq_dict_of_arrays(f8)
c8 = consensus_string(fr8)

print(c3,c5,c8)
print(fr3,fr5,fr8)
