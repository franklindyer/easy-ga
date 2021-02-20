exec(open("loader.py").read())

MUT_PROB = 0.01
POP_SIZE = 50
GENOME_LENGTH = 100
NUM_GENS = 100

colors = ["red","orange","gold","green","blue","indigo","purple"]
selectivities = [0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
pops = []

plt.clf()

num_sels = len(selectivities)
for i in range(num_sels):
    selectivity = selectivities[i]
    p = Population(GENOME_LENGTH, 2, POP_SIZE)
    p.game = TrivialGame()
    p.mutate_prob = MUT_PROB
    p.selectivity = selectivity
    p.next_generation(NUM_GENS, True)
    pops.append(p)
    
for i in range(num_sels):
    color = colors[i]
    p = pops[i]
    sel_str = str(selectivities[i])
    p.plot_gens(stat="avg",smoothness=3,color=color,linewidth=2,label=sel_str,alpha=0.5)

plt.xlim([0,50])
plt.ylim([80,100])
plt.legend(loc="lower right", title="Selectivity")
plt.show()
