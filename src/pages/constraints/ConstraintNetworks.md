[< back](../../index.html)

# Notes on Sussman and Steele's [_Constraints - A Language for Expressing Almost-Hierarchical Descriptions_](https://dspace.mit.edu/bitstream/handle/1721.1/6312/AIM-502a.pdf)

_February 6, 2026_

I was surprised at how pleasant this paper was to read. Yes, I may have skipped some sections about circuits, but the presentation of multi-directional computation was compelling and piqued my curiosity.

If I may attempt to summarize, the paper claims this:

> A programmer may see the relation `y = 5x + z` and write a statement which computes `y` from the variables `x` and `z`. A mathematician, however, could say "I have the values of `y` and `x`, therefore I can derive `z`". The programmer would have to do extra work to perform the same behavior. This restriction, however, is a product of the language the programmer is using, rather than the nature of computing itself. A better language would let us specify relations among values and provide a sufficient combination of inputs to arrive at an output.

The paper continues to explore some edge cases, limitations, and partial solutions to those limitations. It also provides a mechanism for a means of abstraction. I hope to explore this aspect more. What complex ideas can be eloquently expressed as a bundle of constraints?

This paper builds constraint networks using primitive operators and then abstract operations made with these operators. I would like to explore how operations which are more imperative in flavor would change when viewed from a multi-directional perspective. For example, in the [monkey and banana problem](https://en.wikipedia.org/wiki/Monkey_and_banana_problem), what would it mean to think of something like `newState = monkey.grab(banana)` multi-directionally? Perhaps expressed as: `grab(?, banana, newState)`. Is there any meaning in the latter expression? Is the simple act of changing state over time coupling us with directional computation? Have I lost my marbles?

Anyway, I've not read many real papers but I think this one will be a highlight for it's accessibility, though I hope to be wrong.

I understand that these ideas are developed further in theses by [Steele](https://dspace.mit.edu/handle/1721.1/15890) and [Radul](https://dspace.mit.edu/handle/1721.1/44215). I hope, in time, to learn more about their ideas. I've gleaned bits and pieces, and am particularly curious about the implications of considering all values to be ranges.

Some other miscellaneous thoughts:

* The paper presents some ways of turning constraint networks (including circular networks) into expression trees. I think this could be useful for another project I have been thinking about. Basically, if we imagine a word as a node with edges to the words used in its definition, what kind of graph do we get? If this graph is cyclic, I wonder if the paper's transformation of networks into trees could help turn this graph into a tree.
* Algebraic solvers are referenced as an inferior means of expressing multi-directional computation. However, they help address some edge cases when propagating information across the network doesn't resolve all of the constraints.