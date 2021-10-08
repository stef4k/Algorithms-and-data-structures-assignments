# Broken Telephone
Everyone has played the game broken telephone, where one player starts whispering a word to another and then that player to another and so on. The last player calls out the word and it is usually completely different to the starting word.

Based on that principle, we want to build a script that showcases how words can be altered in order to start from one word move on to new words and finally reach a target word, with the least number of steps. At each step, we want the current word to differ to the next one by just one letter:
* Either deleting one letter
* Or inserting one letter
* Or changing one letter

For example, let's say we want to go from the word spring to the word summer. The modifications would be:  

    spring -> string -> sting -> ting -> tine -> time -> timer -> dimer -> dimmer -> simmer -> summer

To solve the problem, we can visualize it as a huge graph, where each word is node. Two words are connected if they vary by one letter, as explained in the above rule. The solution would be to find the quickest path between two words of the graph.

However, we do not need to construct the whole graph in order to solve the problem. We only need a way to detect the neighbors of a word, meaning other words that differ by one letter only

## Levenshtein Distance
The first step in this approach is to find a way of measuring how different two words are, so that we can know if two words are different by one insertion, deletion, or spelling. The metric that gives us exactly the number of insertions, deletions, or letter changes required to convert one word to another is called [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance).

## BK trees
The second step in solving our problem is to find an effective way to dynamically locate the neighbors of each word. One such way is the data structure called the [BK-tree](https://en.wikipedia.org/wiki/BK-tree). A BK tree is defined as follows:
* We select any element as a root.
* Each node of the tree can have as many children, even `n`, corresponding to `n` subtrees. The `k` subtree of a node contains elements that have a distance from the node equal to `k`.

The process is decribed by the following algorithm:  

<p align="center">
<img src="https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-2/images/bk_tree_insertion_algorithm.png" width="500" height="300" />
</p>

Also, the search process is described by the following algorithm:

<p align="center">
<img src="https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-2/images/bk_tree_search_algorithm.png" width="500" height="450" />
</p>

## Finding the path
The third step in the approach is to find the path in the graph. This can be done with a modification of the Dijkstra algorithm. As with the normal algorithm, we maintain a priority queue that we use to see which node we will visit. But instead of the priority of the nodes in the queue arising from the distance from the node we started, it will result from the sum of the distance from the node we started and the distance to the destination node. Then we actually get another search algorithm, the [algorithm A *](https://en.wikipedia.org/wiki/A*_search_algorithm).

## Installation requirements
Install the necessary library:  

    pip install Levenshtein

## Running the script:
Run the script from the command line:  

    python word_morph.py <dictionary_file> <start_word> <target_word>

In the command, <dictionary_file> is the dictionary we want to use. The parameter <start_word> is the word we want to start and <target_word> is the word we want to reach.

If there is a way to reach the <target_word> from the <start_word>, the output should be:

    start_word, word_1, word_2, ..., target_word

If there is no way to reach the <target_word> from the <start_word>, the output should be:

    start_word

## Examples
### Example 1
If the user runs the script in the following way:  

    python word_morph.py dictionary.txt life death

The output could be:

    life, lift, left, heft, heat, heath, death

### Example 2
If the user runs the script in the following way:  

    python word_morph.py dictionary.txt day night

The output could be:

    day, dam, dim, din, sin, sign, sigh, nigh, night

### Example 3
If the user runs the script in the following way:  

    python word_morph.py dictionary.txt reject ratify

The output could be:

    reject, resect, reset, rest, pest, past, pasty, party, parity, rarity, rarify, ratify


##
[Complete Greek Assignment Description](https://github.com/dmst-algorithms-course/assignment-2019-2/blob/master/assignment_2019_2.ipynb)
