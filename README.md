# Engineering Trade-Off Simulator

A Python program I wrote to compare design options. You rate each design on speed, torque and cost, pick how much each one matters, and it ranks them.

I got the idea from robotics, where making one thing better usually makes something else worse. I also wanted practice writing classes in Python.

## How to run

All you need is Python 3.

```
python main.py
```

Enter a weight for speed, torque and cost (any numbers, like 2, 2, 1), then rate each design from 1 to 10. A higher cost rating means a more expensive design.

## How it works

The weights get scaled so they add up to 1. Each design's score is speed, torque and cost times their weights, with cost subtracted. If torque is under 5, the design loses a point and fails the torque check. Then the designs are sorted by score.

One thing I know about: the cutoff for "well-balanced" is 6, and with equal weights the best possible score is about 6.3, so almost nothing gets that rating.

## What I learned

How to combine several ratings into one weighted score, and how to sort a list of objects by one of their values.

## To do

- Save weight presets for different goals

There's also a web version with sliders and a chart: [engineering-tradeoff-visualizer](https://github.com/tanaymishra1/engineering-tradeoff-visualizer).

MIT license.
