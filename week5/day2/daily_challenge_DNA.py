import random

class Gene():
    def __init__(self,value):
        self.value = 1

    def flip_gene(self):
        if self.value == 1:
            self.value = 0
            return 0
        else:
            self.value = 1
            return 1

class Chromosome(Gene):
    def __init__(self,*ten_genes):
        self.ten_genes = ten_genes

    def mute(self, ten_genes):
        values= [1,0]
        ten_genes = []
        for gene in ten_genes:
            self.gene.random.choice(values)
            ten_genes.append(gene)
        print(ten_genes)


class DNA(Chromosome, Gene):
    def __init__(self, *ten_chromosomes):
        self.ten_chromosomes = ten_chromosomes

gene_1 = Gene(1)
print(gene_1.flip_gene())
chromosome_1 = Chromosome(1,1, 1, 1, 1, 1, 1, 1, 1, 1)







