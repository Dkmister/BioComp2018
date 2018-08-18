def change_protein(char):
	if char == 'T':
		return ['C','G','A']
	elif char == 'C':
		return ['T','G','A']
	elif char == 'A':
		return ['C','G','T']
	elif char == 'G':
		return ['A','C','G']
		
def create_mutation(dna):
	total_mutations = []
	others_mutations = []
	for i in range(0,len(dna)):
		others_mutations = change_protein(dna[i])
		for j in range(0,len(others_mutations)):
			sub_dna = list(dna)
			(sub_dna[i]) = (others_mutations[j])
			total_mutations.append(''.join(sub_dna))			
	return (total_mutations)

