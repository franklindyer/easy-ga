exec(open("loader.py").read())

POP_SIZE = 50
GENOME_LENGTH = 200
NUM_GENS = 100

colors = ["red","orange","gold","green","blue","indigo","purple"]
segmented_co_probs = [0.001, 0.01, 0.1, 0.9, 0.99, 0.999]
pops = []

plt.clf()

num_probs = len(segmented_co_probs)
for i in range(num_probs):
    seg_prob = segmented_co_probs[i]
    p = Population(GENOME_LENGTH, 2, POP_SIZE)
    p.crossover_op = "SX"
    p.crossover_param = seg_prob
    p.game = TrivialGame()
    p.next_generation(NUM_GENS, True)
    pops.append(p)

for i in range(num_probs):
    color = colors[i]
    p = pops[i]
    seg_str = str(segmented_co_probs[i])
    p.plot_gens(stat="avg",smoothness=3,color=color,linewidth=2,label=seg_str,alpha=0.5)

plt.legend(loc="lower right", title="Segmented CO probability")
plt.show()
