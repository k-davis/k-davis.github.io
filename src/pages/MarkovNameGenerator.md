[< back](./homepage.html)

# Markov Chain Name Generator
_May 28, 2020_


This program generates names that, although original, look and sound like they could be real names. By learning from over 4,000 names, the program recognizes common sequences of letters, then uses those patterns to generate the new names.

### Tools

This project was written in C++.
The names were gathered from US Census data.

Check out the repo [here](https://github.com/k-davis/markov-chain-name-generator).

### What are Markov Chains?

Markov chains are a suprisingly simple form of unsupervised machine learning. A Markov chain is a collection of states which can be transitioned between probabilistically. A Markov chain can be represented by a directed graph, where each vertex is a state and each edge stores the probability of moving to the indicated state from the current state.

If we wanted to predict the weather (let's limit it to sunny, overcast, and rainy), we could use the probability of each state occuring to guess a day's weather. Let's say that there is a 50% chance for overcast, 30% for sunny, and 20% for rainy weather. We could pick a random number every day for our guess, but we could easily end up flipping back and forth between sunny and rainy. Sure, that _could_ be accurate, but there is a relationship between yesterday's weather and today's. If we could incorporate today's weather in our guess of tomorrow's, we would get better results. Markov chains allow us to do that. Instead of knowing the chance of the weather on a day by day basis, we could record the weather one day, then what it changed to (if at all) on the next day. Markov chains store the probability of what happens next.

Take a look [here](https://setosa.io/ev/markov-chains/), for a more detailed explanation.

### Ok, But How Do We Make Names

But before we get there, I'll need to explain the idea of "orders". With our weather predictor, what's stopping us from using only today's weather to predict tomorrow's? Why can't we use yesterday's and today's? Oh, but we can. We can look backwards as many states as we'd like. The number of states we look back is the order number. If have a model order of zero, we are just guessing each day. With a model order one, we use the previous state, and we can use the two most recent states with a model order of two.

Back to the names. Instead of our states being weather, they are letters. Just as rain is likely to follow overcast weather, so too does a 'u' follow a 'q'. But instead of picking the most likely next state given our previous states, as we might with our weather predictor, we can pick the next state according to how often that transition occurs in our data.

If you take a peek at the second table down below, you may see the generated name "Mathewaldomanrickor". Let's try to figure out what names allowed this silly name to happen in the first place. One feature of the program allows the user to start with a specific string, in this case "Mathew". And it's built from a second order Markov model. So, to pick the next letter, we always look back exactly two letters. What names contain the sequence "ewa"? At least one must. [Through the power of Ctrl+F](https://github.com/k-davis/markov-chain-name-generator/blob/master/names.dat), I can say that "Dewayne", "Steward", and "Stewart" made the 'a' possible.

Now let's go a bit quicker:

**MATHEW**

st**EWA**rt

**WAL**lace

don**ALD**

she**LDO**n

**DOM**enic

That gives us "Mathewaldom" so far. Now this example doesn't mean that, for example, only "Sheldon" has the sequence "LDO". Many did, in fact. But since we are dealing with chance, all it takes is one instance of the sequence to make it possible.

### Example Names

#### Outputs From Model Orders

| Order 1    | Order 2      | Order 3       | Order 4   | Order 5    |
| ---------- | ------------ | ------------- | --------- | ---------- |
| Cheshe     | Doustacey    | Mart          | Darion    | Christofer |
| Lert       | Seph         | Ole           | Cristan   | Florenzo   |
| Je         | Gradon       | Barth         | Landolph  | Hoberto    |
| Magr       | Wighnno      | Normando      | Howardo   | Teodore    |
| Cquite     | Jareif       | Donner        | Bernandon | Kristoper  |
| H          | Trosephirvin | Feltonelliseo | Gustin    | Errold     |
| Ryamian    | Chew         | Than          | Thur      | Quentino   |
| Krdrooccks | Ne           | Lawren        | Rudolfo   | Brandell   |
| Bavera     | Fau          | Scoe          | Darrett   | Sterlin    |
| Lde        | Laineldo     | Arlannon      | Bennis    | Christobal |

As we increase the model order, names start to make more sense. Names generated from a first order model only look back one letter, so only two character sequences are pulled from real names. For a fifth order model, on the other hand, every sequence of five letters comes from a real name.

#### Output From a Starting String

| Starter String | Order 2                           | Order 3                 | Order 4           | Order 5                |
| -------------- | --------------------------------- | ----------------------- | ----------------- | ---------------------- |
| "E"            | Elmans <br> Ez                    | Emilard <br> Earnollina | Emers <br> Emiley | Emmanuela <br> Evangel |
| "Lar"          | Lard <br> Larfid                  | Lario <br> Larey        | Larryl            | -                      |
| "Mathew"       | Mathewil <br> Mathewaldomanrickor | -                       | -                 | -                      |

At some point, we don't have enough names to generate something new. A fifth order name that starts with "Mathew" needs at least one name that contains the sequence "athew" plus one more letter. No name in the data set besides "Mathew" has such a sequence, so no name can be generated with those settings.
