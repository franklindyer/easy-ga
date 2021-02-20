exec(open("loader.py").read())

POP_SIZE = 50
GENOME_LENGTH = 200
NUM_GENS = 100

colors = ["red","orange","gold","green","blue","indigo","purple"]
crossover_ops = ["UX","WHUX","nPX","SX"]
pops = []

plt.clf()

num_ops = len(crossover_ops)
for i in range(num_ops):
    co = crossover_ops[i]
    p = Population(GENOME_LENGTH, 2, POP_SIZE)
    p.crossover_op = co
    p.game = TrivialGame()
    p.next_generation(NUM_GENS, True)
    pops.append(p)

for i in range(num_ops):
    color = colors[i]
    p = pops[i]
    co = crossover_ops[i]
    p.plot_gens(stat="avg",smoothness=3,color=color,linewidth=2,label=co,alpha=0.5)

plt.legend(loc="lower right", title="Crossover operation")

plt.show()
