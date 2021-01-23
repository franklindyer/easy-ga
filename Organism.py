class Organism:

	def __init__(self, genome, possible_genes):
		self.possible_genes = possible_genes
		self.genome = genome.copy()
		self.num_genes = len(genome)	
		self.fitness = 0

	def clone(self):
		return Organism(self.genome, self.possible_genes)

	def gene_at(self, index):
		return self.genome[index]

	def mutate_gene(self, index, prob, max_delta=0):
		old_gene = self.gene_at(index)
		new_gene = 0
		if random.random() < prob:
			if max_delta == 0:
				new_gene = random.randint(0, self.possible_genes-1)
			else:
				delta = random.randint(-max_delta, max_delta)
				new_gene = max(0, min(self.possible_genes-1, old_gene + delta))
			self.genome[index] = new_gene

	def mutate(self, prob, max_delta=0):
		for i in range(self.num_genes):
			self.mutate_gene(i, prob, max_delta=max_delta)		

	def spawn(genome_length, possible_genes):
		genome = [random.randint(0, possible_genes-1) for i in range(genome_length)]
		return Organism(genome, possible_genes)
