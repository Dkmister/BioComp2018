import numpy as np
#
#
def freq_dict_of_arrays_v2(dna_list):
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

l = ['ATA','GTA','CAG','AAA']
p = freq_dict_of_arrays_v2(l)
print (p)
c = consensus_string(p)
print(c)
