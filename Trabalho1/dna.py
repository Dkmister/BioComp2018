
def create_dic_nucleotid():
	dic_nuc = {'A':0,'C':0,'T':0,'G':0,'N':0}
	return dic_nuc

def count_nucleotid(char,dic):
	if char == 'A':
		dic['A'] = dic['A'] + 1
	elif char == 'C':
		dic['C'] = dic['C'] + 1
	elif char == 'G':
		dic['G'] = dic['G'] + 1
	elif char == 'T':
		dic['T'] = dic['T'] + 1
	else:
		dic['N'] = dic['N'] + 1
	return dic

def create_nucleotid_UFRGS(number):
	if number == '0' or number == '7' or number == '8' :
		return 'A'
	elif number =='1' or number == '6':
		return 'T'
	elif number == '2' or number == '5':
		return 'G'
	elif number == '3' or number == '4' or number == '9':
		return 'C'
	else:
		return None

def sequence_nucleotid_UFRGS(matricula):
	sequence_nucleotid = ""
	for char in matricula:
		sequence_nucleotid += create_nucleotid_UFRGS(char)
	return sequence_nucleotid

def complementary_sequence(word):
	comp_seq = ""
	for char in word:
		comp_seq += complementary_nucleotid(char)
	return comp_seq



def complementary_nucleotid(char):
	if char == 'T':
		return 'A'
	elif char == 'A':
		return 'T'
	elif char == 'C':
		return 'G'
	elif char == 'G':
		return 'C'
	else:
		return ''

def create_different_sequences_E(sequence):
	lst_diff_seq = []
	tmp_c = ""
	diff_nucs = change_all_nucleotids(sequence[4])
	for n in diff_nucs:
		tmp_dna = list(sequence)
		tmp_dna[4] = n
		lst_diff_seq.append(''.join(tmp_dna))
	for char in sequence:
		tmp_c += complementary_nucleotid(char)
	lst_diff_seq.append(tmp_c)
	lst_diff_seq.append(sequence)
	return (lst_diff_seq)

def change_all_nucleotids(char):
	if char == 'T':
		return ['C','G','A']
	elif char == 'C':
		return ['T','G','A']
	elif char == 'A':
		return ['C','G','T']
	elif char == 'G':
		return ['A','C','G']

def create_all_possible_mutations(dna):
	total_mutations = []
	others_mutations = []
	for i in range(0,len(dna)):
		others_mutations = change_all_nucleotids(dna[i])
		for j in range(0,len(others_mutations)):
			sub_dna = list(dna)
			(sub_dna[i]) = (others_mutations[j])
			total_mutations.append(''.join(sub_dna))
	return (total_mutations)

