class Population:

    def __init__(self, genome_length, possible_genes, size):

        self.genome_length = genome_length
        self.possible_genes = possible_genes
        self.size = size

        self.genomes = [Genome.random(genome_length, possible_genes) for i in range(size)]
        self.gene_pool = []
        self.generation = 0

        ## Default settings:
        self.game = TrivialGame()
        self.num_trials = 20
        self.selectivity = 0.5
        self.num_parents = 2
        self.mutate_prob = 0.02
        self.crossover_op = "UX"
        self.crossover_param = 0

        ## Data collection settings:
        self.log = True
        self.past_gens = []

    def get(self, index):

        return self.genomes[index]

    def test_fitness(self):

        for g in self.genomes:
            scores = [self.game.play(g) for i in range(self.num_trials)]
            g.fitness = sum(scores) / self.num_trials

    def select_parents(self):

        self.genomes.sort(key = lambda x: x.fitness)
        if self.log: self.past_gens.append(self.genomes)
        cutoff = int(np.floor(self.size * self.selectivity))
        self.gene_pool = self.genomes[cutoff:]

    def reproduce(self):

        new_genomes = []
        for i in range(self.size):
            parents = np.random.choice(self.gene_pool, size=self.num_parents, replace=False)
            child_genome = Genome.reproduce(parents, crossover_op=self.crossover_op, param=self.crossover_param)
            child_genome.mutate(self.mutate_prob)
            new_genomes.append(child_genome)

        return new_genomes

    def next_generation(self, num_gens=1, report_progress=False):

        final_gen = self.generation + num_gens

        for i in range(num_gens):
            self.test_fitness()
            self.select_parents()
            self.genomes = self.reproduce()
            self.generation += 1
            if report_progress:
                print("Generation " + str(self.generation) + " complete (" + str(i+1) + "/" + str(num_gens) + ")")

    def plot_gens(self, stat="max", smoothness=0, **kwargs):

        gens = range(self.generation)
        
        data = []
        if stat == "max":
            data = [self.past_gens[i][-1].fitness for i in gens]
        elif stat == "avg":
            data = [sum([g.fitness for g in self.past_gens[i]])/self.size for i in gens]

        gens_smooth = range(self.generation - 2*smoothness)
        data_smooth = [sum(data[i:i+2*smoothness+1])/(2*smoothness+1) for i in gens_smooth]

        plt.plot(gens_smooth, data_smooth, **kwargs)
        plt.xlabel("Number of generations")
        plt.ylabel("Average fitness")
