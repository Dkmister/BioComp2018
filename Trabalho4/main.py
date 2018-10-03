from Bio import Phylo
from io import StringIO
def lowest_cell(table):
	min_cell = float("inf")
	x , y = -1, -1 
	
	for i in range(len(table)):
		for j in range(len(table[i])):
			if table[i][j] < min_cell:
				min_cell = table[i][j]
				x,y = i,j
	
	return x,y


def join_labels(labels,a,b):
	if b < a:
		a,b = b,a
		
	labels[a] = "(" + labels[a] + "," + labels[b] + ")"
	
	del labels[b]
	
def join_table(table,a,b):
	if b<a:
		a,b = b,a
		
	row = []
	for i in range(0,a):
		row.append((table[a][i] + table[b][i])/2)
	table[a] = row
	
	for i in range(a+1,b):
		table[i][a] = (table[i][a] + table[b][i]) / 2 
		
	for i in range(b+1,len(table)):
		table[i][a] = (table[i][a] + table[i][b]) / 2 
		del table[i][b]
		
	del table[b]

def UPGMA(table,labels):
	while len(labels) > 1:
		x,y = lowest_cell(table)
		join_table(table,x,y)
		join_labels(labels,x,y)
	return labels[0]
	
def alpha_labels(start,end):
	labels = []
	for i in range(ord(start), ord(end)+1):
		labels.append(chr(i))
	return labels
	
M_labels = alpha_labels("A","E")
M = [
	[],
	[0.189],
	[0.110,0.179],
	[0.113,0.192,0.094],
	[0.215,0.211,0.205,0.214]]
	
u = (UPGMA(M,M_labels))
u = u.replace("A","Gorila")
u = u.replace("B","Oragontango")
u = u.replace("C","Humano")
u = u.replace("D","Chimpanze")
u = u.replace("E","Gibao")
handle = StringIO(u)
tree = Phylo.read(handle,"newick")

Phylo.draw(tree)
