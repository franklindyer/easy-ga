class Genome:

        def __init__(self, sequence, possible_genes):
                self.possible_genes = possible_genes
                self.sequence = sequence
                self.length = len(sequence)

        def copy(self):
                return Genome(self.sequence.copy())

        def get(self, index):
                return self.sequence[index]

        def mutate_gene(self, index, max_delta=0):
                old_gene = self.get(index)
                new_gene = 0
                if max_delta == 0:
                        new_gene = random.randint(0, self.possible_genes-1)
                else:
                        delta = random.randint(-max_delta, max_delta)
                        new_gene = max(0, min(self.possible_genes-1, old_gene + delta))
                self.sequence[index] = new_gene

        def mutate(self, prob, max_delta=0):
                for i in range(self.length):
                        if random.random() < prob:
                                self.mutate_gene(i, max_delta=max_delta)

        def random(length, possible_genes):
                sequence = [random.randint(0, possible_genes-1) for i in range(length)]
                return Genome(sequence, possible_genes)

        def reproduce(parents, crossover_op="UX"):

                length = parents[0].length
                possible_genes = parents[0].possible_genes
                new_genome = []

                if crossover_op == "UX":
                        new_genome = [random.choice(parents).get(i) for i in range(length)]
                
                return Genome(new_genome, possible_genes)
