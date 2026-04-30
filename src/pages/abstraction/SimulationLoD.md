[< back](../homepage.html)

# Notes on _Simulation Level-Of-Detail_

_October 8, 2025_

This page is a summary of my notes on Stephen Chenney's paper [_Simulation Level-Of-Detail_](https://pages.cs.wisc.edu/~schenney/research/culling/chenney-gdc2001.pdf), for the sake of my future self as well as for the chance visitor.

My end goal is to develop a language that allows for level-of-detail (LOD) execution. In the same way that video games have LOD settings for graphics or physics, I'd like to apply the concept to how a program executes. A single program could be executed with a low, medium, or high resolution. 

For example, imagine a pathfinding algorithm that provides driving directions:

* At the highest level of detail, it would provide directions that specify exactly which lane to drive in and exactly with roads and turns to take. 
* At a moderate level of detail, it would output the major freeways, put omits specific. 
* At a low level of detail, the instructions would be as simple as "go north for 30 minutes, then west for 10". 

Each of these sets of instructions represent the same information, but at different degrees of specificity.

## Overview

This paper demonstrates LOD execution applied to simulated vehicle driving in a city. 

There are a number of challenges to a system like this and some of these problems are introduced in this paper without getting bogged down in excess detail and perfectionism.

Briefly, these challenges include:

* Resource contention
* Identifying essential behavior
* Designing proxies


For its wide-but-shallow coverage of the domain, this paper is an excellent introduction to the goal and obstacles around LOD execution.

## Discrete Event Simulation

In order to transform and relate concepts or states across different levels of detail, they must be well defined in code. To define events in this manner, the author uses [Discrete Event Simulation (DES)](https://en.wikipedia.org/wiki/Discrete-event_simulation).

Consider the alternative to discrete behavior as something that is plainly observable, but cannot be concisely defined. For example, in the [Boids algorithm](https://en.wikipedia.org/wiki/Boids), although we can clearly observe flocking, it is not discrete. It would not be possible to define an `IsFlocking` value for the birds (barring some mysterious AI solution). For this reason, we cannot _operate_ with this behavior. We cannot group the birds into flocks, identify those that fly alone, or otherwise rely on this information.

The primary use of DES in this paper is for the management of vehicles's location and movement. Although vehicles within line of sight have traditional continuous movement, all others have their movement modeled with discrete events. These events contain only essential information. There is only the times for entering and exiting cells of a quadtree, which models the city's area. 

## Designing Proxies

The continuous-motion cars have a set of behaviors which are deemed essential. These are behaviors or qualities that the author has decided must be preserved in the lower resolution level of detail. These traits are not emergent or automatically occurring. They are functional requirements of the system. 

The lower resolution behaviors are implemented via a _proxy_, an approximation of an event or behavior. The design process of a proxy for movement needs to ensure that certain desired behaviors are preserved. Anything else can be dropped. The author chose travel time as being the value which best characterizes the base simulation's behavior. And so, the proxy's implementation must ensure that the simplified driving model produces a similar travel time as the base simulation.

## Resource Contention

Two vehicles cannot occupy the same physical space. As vehicles pass through an intersection, they must be mindful to avoid colliding. We would consider this 'resource contention,' since the vehicles must take turns 'using the resource' of the intersection.

In the base simulation, the vehicles have special behavior for real-time collision avoidance. This behavior is not scalable to tens of thousands of vehicles, so an approximation must be made for the proxy. The proxy simulates this by using a collection of queues. The queues allow for the preservation of the time delay caused by waiting, but dropping the specifics of how the vehicles manuever around each other. The essential characteristics are preserved, and computational costs are reduced.

## Final Thoughts and Going Forward

This paper is valuable as a means to encounter the breadth of the concepts required for LOD execution. If and when I step away from this project, I would intend for this to be how I reenter the domain. It can onboard as well as remind what the goal is.