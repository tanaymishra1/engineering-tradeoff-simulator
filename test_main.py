import pytest

from main import Design, ordinal, rank, score_range

EQUAL = {"speed": 1 / 3, "torque": 1 / 3, "cost": 1 / 3}
WEIGHTS = {"speed": 0.4, "torque": 0.4, "cost": 0.2}


def test_range_is_ten():
    for weights in [EQUAL, WEIGHTS, {"speed": 1, "torque": 0, "cost": 0}]:
        best, worst = score_range(weights)
        assert best - worst == pytest.approx(10)


def test_best_and_worst():
    assert Design("best", 10, 10, 1, WEIGHTS).score == pytest.approx(100)
    assert Design("worst", 1, 1, 10, WEIGHTS).score == pytest.approx(0)


def test_example_designs():
    a = Design("A", 8, 6, 3, WEIGHTS)
    b = Design("B", 5, 9, 7, WEIGHTS)
    assert a.score == pytest.approx(72)
    assert b.score == pytest.approx(64)
    assert a.evaluation == "Acceptable trade-off, but with limitations."


def test_low_torque():
    # penalty case
    weak = Design("weak", 8, 4, 3, WEIGHTS)
    strong = Design("strong", 8, 5, 3, WEIGHTS)
    assert weak.evaluation == "Fails minimum torque constraint."
    assert strong.score - weak.score == pytest.approx(14)


def test_cutoffs():
    assert Design("great", 10, 9, 2, WEIGHTS).evaluation == "Well-balanced trade-off."
    assert Design("poor", 5, 5, 9, WEIGHTS).evaluation == "Not optimal trade-off."


def test_focus():
    assert Design("x", 10, 9, 5, EQUAL).focus == "Performance-focused (speed-driven)"
    assert Design("x", 5, 8, 3, EQUAL).focus == "Power-focused (torque-driven)"
    assert Design("x", 6, 6, 2, EQUAL).focus == "Cost-efficient"
    assert Design("x", 5, 5, 5, EQUAL).focus == "Balanced properties"


def test_ordinal():
    assert [ordinal(n) for n in [1, 2, 3, 4, 11, 12, 13, 21, 22, 23, 111, 112]] == [
        "1st", "2nd", "3rd", "4th", "11th", "12th", "13th",
        "21st", "22nd", "23rd", "111th", "112th",
    ]


def test_failing_ranks_last():
    # higher score
    fails = Design("fails", 10, 4, 1, WEIGHTS)
    passes = Design("B", 5, 9, 7, WEIGHTS)
    assert fails.score == pytest.approx(66)
    assert [d.name for d in rank([fails, passes])] == ["B", "fails"]
