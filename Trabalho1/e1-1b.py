from main import *

c7 = init_file("sequence.fasta")

b = substring_palindrome(8,c7)
print("Tamanho de itens com palindromo tamanho 8: "+str(len(b))+"\n")
print(b)
