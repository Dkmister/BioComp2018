def init_file(filename):
	with open(filename) as f:
		content = f.read().splitlines()
	return content
dna = init_file("dna_teste.txt")
print(dna)

