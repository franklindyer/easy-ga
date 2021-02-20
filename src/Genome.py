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

        def reproduce(parents, crossover_op="UX", param=0):

                num_parents = len(parents)
                length = parents[0].length
                possible_genes = parents[0].possible_genes
                new_genome = []

                if crossover_op == "UX":
                        parent_choices = random.choices(parents, k=length)
                        new_genome = [parent_choices[i].get(i) for i in range(length)]
                elif crossover_op == "WHUX":
                        total_fitness = sum([p.fitness for p in parents])
                        parent_weights = [p.fitness/total_fitness for p in parents]
                        parent_choices = random.choices(parents, weights=parent_weights, k=length)
                        new_genome = [parent_choices[i].get(i) for i in range(length)]
                elif crossover_op == "nPX":
                        if param == 0: param = 1
                        cut_pts = random.sample(range(length), param)
                        which_parent = 0
                        for i in range(length):
                            if i in cut_pts:
                                which_parent = (which_parent + 1) % num_parents
                            new_genome.append(parents[which_parent].get(i))
                elif crossover_op == "SX":
                        if param == 0: param = 0.5
                        which_parent = 0
                        for i in range(length):
                            if random.random() < param:
                                which_parent = (which_parent + 1) % num_parents
                            new_genome.append(parents[which_parent].get(i)) 

                return Genome(new_genome, possible_genes)
