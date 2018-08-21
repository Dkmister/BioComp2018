from init import *

def init_matrix(n,m)
	M = []
	for i in (len(n)+1):
		for j in (len(m)+1):
			M[i][j] = 0
	return M

def main():
	human = init_file("human.fasta")
	deer = init_file("deer.fasta")
	pig = init_file("pig.fasta")
	wolf = init_file("wolf.fasta")
	chicken = init_file("chicken.fasta")
	cow = init_file("cow.fasta")
	trout = init_file("trout.fasta")
	horse = init_file("horse.fasta")

