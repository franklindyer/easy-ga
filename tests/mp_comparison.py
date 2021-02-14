exec(open("loader.py").read())

POP_SIZE = 50
GENOME_LENGTH = 100
NUM_GENS = 100
colors = ["red","orange","gold","green","blue","indigo","purple"]
mut_probs = [0.00001, 0.0002, 0.001, 0.005, 0.01, 0.04, 0.1]
pops = []

plt.clf()

num_mps = len(mut_probs)
for i in range(num_mps):
    mp = mut_probs[i]
    p = Population(GENOME_LENGTH, 2, POP_SIZE)
    p.game = TrivialGame()
    p.mutate_prob = mp
    p.next_generation(NUM_GENS, True)
    pops.append(p)
    
for i in range(num_mps):
    color = colors[i]
    p = pops[i]
    mp_str = str(mut_probs[i])
    p.plot_gens(stat="avg",smoothness=3,color=color,linewidth=2,label=mp_str,alpha=0.5)

plt.xlabel("Number of generations")
plt.ylabel("Average fitness")
plt.legend(loc="lower right", title="Mutation probability")
plt.show()
