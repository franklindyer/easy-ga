# easy-ga

Genetic algorithms are one of my personal favorite topics in complexity science, so I've been working on this framework to streamline the process of building, configuring, and experimenting with a genetic algorithm of your very own. It's definitely still a work in progress, but you can already rn some interesting simulations with it.

I'll assume that you're already familiar with what a genetic algorithm is and how it works. If not, there are all sorts of great resources explaining genetic algorithms. I'd highly recommend Melanie Mitchell's book *Complexity: A Guided Tour* - this is the book that first got me interested in GAs, along with several other topics in complexity science. I've even written a couple [blog](https://franklin.dyer.me/post/119) [posts](https://franklin.dyer.me/post/158) about GAs, as well as a [research paper](https://github.com/franklindyer/AP-Research-Genetic-Algorithm-Project/blob/master/Finished_Research_Paper.pdf) with an introductory section explaining how GAs work. 

## Getting started

This framework is meant to be as easy to use as possible, so you can run some cool experiments just from the Python console. Go ahead and download this repo and fire up the Python console. Start by running `loader.py` to load all of the pre-baked classes:

`exec(open("loader.py").read())`

Yes, I know, this isn't an official Python package yet, so you can't use the more elegant command `import easy-ga`. I'll get that figured out after this project has more features.

Once you've done that, you can start by creating a new population:

`p = Population(100, 2, 50)`

This will create a Population containing `50` individuals with genomes consisting of `100` characters, each of which is chosen randomly from a set of `2` characters (`0` or `1`). You can create different-sized populations with different genome formats by tweaking these parameters, and there are tons of other attributes of the Population object that allow you to configure your GA:

- `p.game` is the game that individuals will play to determine their fitness. The default game is `TrivialGame`, which just scores individuals by the number of zeroes in their gene sequence.
- `p.num_trials` is the number of attempts at a game that each individual gets, and the scores of these attempts are averaged to determine the player's fitness. Default value of `20`.
- `p.selectivity` determines the proportion of players that will be excluded from the gene pool. E.g. a selectivity of `0.7` would mean that only the top 30% of players will comprise the gene pool. Default value of `0.5`.
- `p.num_parents` determines the number of parents whose genomes are combined to create a single child. Default value of `2`.
- `p.mutate_prob` determines the mutation probability of a single character in the child's gene sequence immediately following reproduction. Note that this is not the probability that the character *changes*, but rather the probability that it is assigned a random value (it could, by chance, be assigned the same value as before). Default value of `0.02`.
- `p.crossover_op` is the crossover operation used. Here are the options that exist so far:
    - `"UX"`, or "uniform crossover". Each character in the child's gene sequence is chosen uniformly and at random from the corresponding characters in its parents' gene sequences.
    - `"WHUX"` or "Wright's Heuristic uniform crossover". Same as uniform crossover, but the characters are not chosen uniformly - probabilities are weighted proportionally based on parents' fitness values.
    - `"nPX"` or "n-point crossover". N points along the length of the child's gene sequences are chosen randomly, and the parents' gene sequences are spliced together at these points. Default number of points is `1`.
    - `"SX"` or "segmented crossover". Similar to n-point crossover, but instead of having a fixed number of crossover points, each point in the child gene sequence is chosen as a crossover point with some fixed probability. Default probability is `0.5`.
- `p.crossover_param` is an optional parameter for the chosen crossover operator. For example, `nPX` takes the number of crossover points as a parameter, and `SX` takes the probability of crossover at any point as a parameter.

Once you've configured your GA nach Herzenslust, you're ready to watch your babies evolve! *Yesss my children, go forth into the wild...*


