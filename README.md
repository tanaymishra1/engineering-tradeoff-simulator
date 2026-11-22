[README.md](https://github.com/user-attachments/files/35225695/README.md)
# Engineering Trade-Off Simulator

A small Python program that compares engineering design options. You rate each design on speed, torque and cost, decide how much each one matters, and the program scores and ranks them.

I later made a web version with sliders and a live chart: [engineering-tradeoff-visualizer](https://github.com/tanaymishra1/engineering-tradeoff-visualizer).

## Why I made this

In robotics, making one part of a design better usually makes another part worse. A faster design might have less torque or cost more. I wanted to model that in code, and I wanted practice writing classes in Python.

## Running it

You need Python 3.6 or newer. There's nothing to install.

```
python main.py
```

It asks for three weights first (how much speed, torque and cost matter). They don't have to add up to anything, so `2 2 1` and `40 40 20` work the same way. Then it asks how many designs you want to compare, and a name plus a 1-10 rating for speed, torque and cost for each one. A higher cost rating means the design is more expensive.

Here's the end of a run with equal weights and three designs:

```
Design Rankings:
1st Place:
Design: Drivetrain C
 Score: 3.0
 Evaluation: Not optimal trade-off.
 Design Focus: Power-focused (torque-driven)

2nd Place:
Design: Drivetrain B
 Score: 3.0
 Evaluation: Not optimal trade-off.
 Design Focus: Power-focused (torque-driven)

3rd Place:
Design: Drivetrain A
 Score: 1.33
 Evaluation: Fails minimum torque constraint.
 Design Focus: Performance-focused (speed-driven)

Summary Analysis:
 Highest Score: 3.0
 Average Score: 2.44
 Score Range: 1.67
```

## How it works

The weights get scaled so they add up to 1. Each design is a `Design` object, and its score is:

```
score = speed * speed_weight + torque * torque_weight - cost * cost_weight
```

If torque is below 5, the design loses another point and gets marked as failing the torque requirement. Otherwise a score of 6 or more is "well-balanced", 4 to 6 is "acceptable", and anything lower is "not optimal".

The design focus is based on which rating stands out: highest speed, highest torque, lowest cost, or balanced if none of them does.

With more than one design, the program sorts them by score and prints the highest score, the average and the range.

## Problems I know about

The 6-point cutoff for "well-balanced" doesn't change with the weights. With equal weights the best possible score is about 6.3, so almost nothing gets that rating.

Scores are rounded when they're printed, so two designs can show the same score even though one is ranked higher.

## What I learned

This was the first time I combined several ratings into one weighted score, and I had to figure out why the weights need to be normalized so different inputs give the same result. I also learned how to sort a list of objects by one of their attributes using `sort(key=lambda d: d.score, reverse=True)`.

## Next steps

- [ ] Save weighting profiles for different design goals
- [x] Graph the trade-offs (done in the web version)
- [x] Web interface (done in the web version)

## License

MIT, see [LICENSE](LICENSE).
