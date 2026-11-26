# Engineering Trade-Off Simulator

A Python program I wrote to compare design options. You rate each design on speed, torque and cost, pick how much each one matters, and it ranks them with a score out of 100.

I got the idea from robotics, where making one thing better usually makes something else worse. I also wanted practice writing classes in Python.

## How to run

All you need is Python 3.

```
python main.py
```

Enter a weight for speed, torque and cost (any numbers, like 2, 2, 1), then rate each design from 1 to 10. A higher cost rating means a more expensive design.

## How it works

The weights get scaled so they add up to 1. Each design gets a raw score: speed and torque times their weights, minus cost times its weight. If torque is under 5, the design loses a point and fails the torque check.

The raw score then becomes a score out of 100. 0 is the worst design possible with your weights (speed 1, torque 1, cost 10) and 100 is the best (10, 10, 1). 75 or more counts as well-balanced and 50 or more as acceptable.

The first version just used the raw score with a cutoff of 6 for "well-balanced". With equal weights the best possible score was about 6.3, so almost nothing ever got that rating. Switching to a score out of 100 fixed that.

Design focus is based on the ratings. A design is speed-driven if speed is its highest rating, torque-driven if torque is, cost-efficient if speed and torque tie and cost is lower, and balanced otherwise. The web version uses the same rule.

## Tests

```
pip install -r requirements.txt
pytest
```

The tests check the scoring, the torque rule, the design focus and the place names (1st, 2nd, 11th, 21st and so on). GitHub runs them on every push.

## What I learned

How to combine several ratings into one weighted score, and how to sort a list of objects by one of their values.

When I came back to clean it up, I learned why global variables make code hard to test. I moved the weights into a parameter, put the program inside a main() function, and gave names to numbers like the minimum torque so the code says what they mean. I also found out my place names were wrong past 20, since it printed "21th".

## To do

- Save weight presets for different goals

There's also a web version with sliders and a chart: [engineering-tradeoff-visualizer](https://github.com/tanaymishra1/engineering-tradeoff-visualizer).

MIT license.
