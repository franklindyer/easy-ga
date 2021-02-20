# easy-ga

Genetic algorithms are one of my personal favorite topics in complexity science, so I've been working on this framework to streamline the process of building, configuring, and experimenting with a genetic algorithm of your very own. It's definitely still a work in progress, but you can already rn some interesting simulations with it.

I'll assume that you're already familiar with what a genetic algorithm is and how it works. If not, there are all sorts of great resources explaining genetic algorithms. I'd highly recommend Melanie Mitchell's book *Complexity: A Guided Tour* - this is the book that first got me interested in GAs, along with several other topics in complexity science. I've even written a couple [blog](https://franklin.dyer.me/post/119) [posts](https://franklin.dyer.me/post/158) about GAs, as well as a [research paper](https://github.com/franklindyer/AP-Research-Genetic-Algorithm-Project/blob/master/Finished_Research_Paper.pdf) with an introductory section explaining how GAs work. 

## Quickstart

If you just want to get something running and you don't care about the details of what's going on under the hood yet, fine! Here are a few lines of code that will have your GA running in a jiffy, and even display a pretty graph of its progress over time:

```
exec(open("loader.py").read())
p = Population(200, 2, 100)
p.next_generation(100, True)
p.plot_gens(stat="avg",linewidth=2)
plt.show()

```

Beautiful! Now if you *really* want to know what's going on, and how to configure your GA, read the following sections.

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

## Running your Genetic Algorithm

You can use the following command to run your genetic algorithm for `100` generations (or however many generations you want):

`p.next_generation(100)`

This might take a while, from a few seconds to a few minutes depending on how large your population is or how computationally intensive the game you've chosen is. If you want it to report its progress as it runs, letting you know how many generations it's completed, run the following command:

`p.next_generation(100, report_progress=True)`

or just

`p.next_generation(100, True)`

That's all there is to it! Each of the steps required for a single iteration of the genetic algorithm - fitness evaluation, selection, reproduction, mutation - are implemented as methods of the `Population` class, and bundled into the single method `next_generation`. If you want to see what these specific functions look like, feel free to go digging around in the code of `Population.py`.

Note that if you run the command `p.next_generation(100)` *again*, the GA will pick up where it left off, not start over from scratch. This is nice for manual observation, because it allows you to run your GA for a while, check out the results, maybe run it for a while longer (and maybe even change up the parameters before doing so), and so on.

## Parsing the results

This is all fine and good, you say, but how do I actually *see what's going on* in my genetic algorithm?

Your GA has another parameter called `p.log` which has the default value of `True` and determines whether the GA saves information about its populations from past generations. So long as you didn't set `p.log = False`, all of the populations from past generations will be stored in the array `p.past_gens`, which is an array of arrays of Genome objects (each Genome represents an individual, each array of Genomes represents the population of a single generation).

If you want, you can dig through this log array manually. Each Genome in the log contains not only its gene sequence, but also the fitness value it was assigned during evaluation, and the population arrays for each generation are actually sorted by fitness. This makes it easy to pick out, say, the best player from any generation and have a look at their gene sequence.

However, if you don't want to get your hands dirty, there's already a built-in function that draws a nice, pretty graph tracking the progress of your virtual spawn over time:

`p.plot_gens(stat="avg")`

Running this command graphs the average fitness of each population (on the y-axis) for each generation (on the x-axis).

Of course, this is customizable as well. Here's a complete list of population statistics that you can plot:
- `stat="avg"`: plots the average fitness of individuals in each population.
- `stat="max"`: plots the maximum fitness, or the fitness of the most-fit individual in each population.
- *More coming soon!*

But wait, there's more! Because of the element of randomness in GAs, the generational fitness often jitters randomly up and down from one generation to the next. This can make the graph jagged and trends difficult to detect. However, there's another optional parameter that you can pass to `plot_gens` that will "smooth out" the data by plotting a [moving average](https://en.wikipedia.org/wiki/Moving_average). Here's an example command:

`p.plot_gens(stat="avg", smoothness=5)`

The larger the value of `smoothness`, the more values will be included in each moving average, and the smoother the graph will be, making it easier to track any increase (or decrease!) in your population's performance.

But wait, there's *even more*! The `plot_gens` function uses `matplotlib`'s [plot function](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html), which has a ton of keyword arguments that can be used to control the color, transparency, and width of lines, add labels, and do all kinds of other cool stuff. Any additional keyword arguments passed to `plot_gens` will be passed along to the `plot` function, so anything that `matplotlib`'s `plot` can do, `plot_gens` can do! 
