exec(open("loader.py").read())

MUT_PROB = 0.01
GENOME_LENGTH = 100
NUM_GENS = 100
colors = ["red","orange","gold","green","blue","indigo","purple"]
pop_sizes = [5, 10, 25, 50, 100]
pops = []

plt.clf()

num_sizes = len(pop_sizes)
for i in range(num_sizes):
    size = pop_sizes[i]
    p = Population(GENOME_LENGTH, 2, size)
    p.game = TrivialGame()
    p.mutate_prob = MUT_PROB
    p.next_generation(NUM_GENS, True)
    pops.append(p)

for i in range(num_sizes):
    color = colors[i]
    p = pops[i]
    size_str = str(pop_sizes[i])
    p.plot_gens(stat="avg",smoothness=3,color=color,linewidth=2,label=size_str,alpha=0.5)
    
plt.legend(loc="lower right", title="Population size")

plt.show()
