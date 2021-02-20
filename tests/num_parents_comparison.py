exec(open("loader.py").read())

POP_SIZE = 50
GENOME_LENGTH = 200
NUM_GENS = 100

colors = ["red","orange","gold","green","blue","indigo","purple"]
parent_nums = [1, 2, 3, 4, 5]
pops = []

plt.clf()

num_parent_options = len(parent_nums)
for i in range(num_parent_options):
    num_parents = parent_nums[i]
    p = Population(GENOME_LENGTH, 2, POP_SIZE)
    p.crossover_op = "SX"
    p.crossover_param = 0.1
    p.num_parents = num_parents
    p.game = TrivialGame()
    p.next_generation(NUM_GENS, True)
    pops.append(p)

for i in range(num_parent_options):
    color = colors[i]
    p = pops[i]
    parent_str = str(parent_nums[i])
    p.plot_gens(stat="avg",smoothness=3,color=color,linewidth=2,label=parent_str,alpha=0.5)

plt.legend(loc="lower right", title="Number of parents")

plt.show()
