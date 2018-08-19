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
		return None

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

