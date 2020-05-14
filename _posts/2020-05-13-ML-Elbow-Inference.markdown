---
layout: post
title: "VR Elbow Inference"
date: 2020-05-11 16:23:42 -0700
permalink: /research/VR-Elbow-Inference
---

## If you only know where your head and hands are, where are your elbows?

During my senior year of college, I undertook an undergraduate thesis project to answer this question. Or, more accurately, whether a neural network can outperform existing solutions like inverse kinematics.

### Context

Virtual Reality is a rapidly growing technology. While most applications manifest the user simply as a pair of floating hands, but some applications try to recreate the user's entire body. But if your eyes tell you that your arms are in a different location than where you [_know_](https://en.wikipedia.org/wiki/Proprioception) they are, the user will feel uncomfortable.

Existing solutions generally use some form of inverse kinematics to solve where the user's elbow is. It works, but it's better for procedural animations or robotic arms than it is for recreating the a real person's real arm.

So the best solution to the problem right now is one that isn't good enough to be widely used.

I want to change that.

### Tools

This project used:

- Python, for making the data processor
- Jupyter Notebooks, for writing and running the models
- Keras, for building the models
- Processing, for making the visualizations
- Git/GitHub, for version control

The original data was sourced from the [Carnegie Mellon University Graphics Lab Motion Capture Database](http://mocap.cs.cmu.edu/).

Check out the repo [here](https://github.com/k-davis/VR-Elbow-Inference).

### Work

Between August 2019 and May 2020, my work was overseen by faculty advisor Dr. Katherine Schroeder, whose assistance, insight, and ecouragement was invaluable.

Over the course of the year, I built an overly complex data processor, a visualization tool to check if my processor worked, and a second visualization tool to see whether I had gaps in my data or to uncovered any unknown patterns in the data.

#### Data Processor Verification Tool

This tool simultaneously plays for comparison the unprocessed and processed motion capture data. With this tool I can ensure that the processor correctly normalized the data.
![image](/images/data-proc-tester.jpg "Data Processor Verification Tool")

#### Coverage Visualization Tool

This visualization tool allows me to see all the available training data, and the relationship between joints within a region, and their correlated elbow/hand joints. A joint is represented by a single black point. We can see, in the visualization, that there are regions of low sampling and regions of high sampling. The joint type shown in each window can be switched so that hand joints are selected and their relationship with elbow joints can be seen on the right.

Shown below, a region of elbow joints are selected and we can view the forearms defined by the selected joints and their correlated hand joints.

![image](/images/coverage-viz-tool.jpg "Coverage Visualization Tool")
_Here, a region of elbows can be selected in the Controller Window (left) and the hands/forearm locations are seen in the Viewer Window(right)._

### Results & Future Work

Well... my results weren't great. In fact, you would be better off randomly guessing where the elbow is than using even my most accurate neural network model.

So that's not too great, is it? I learned a lot along the way, but not the stuff I was expecting. I plan on effectively heading back to the drawing board and reworking my process to try to get better results.

Here's my goal right now:

- Collect my own data (I originally used motion capture data from Carnegie Mellon University)
- Rewrite my data processor - maybe Excel would be better than a massive Python script?
- Have better data coverage
- Treat the data as time-series data when training
- Build a visualization tool to analyze the model's outputs
- Create inverse kinematics solutions that use the same data input for direct comparison

---

_Expect more to come._
