def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")


def user_input(prompt):
    while True:
        value = read_number(prompt)
        if 1 <= value <= 10:
            return value
        print("Please enter a value between 1 and 10.")


def read_design_count():
    while True:
        try:
            count = int(input("How many designs would you like to evaluate? "))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if count >= 1:
            return count
        print("Please enter at least 1.")


def read_weights():
    print("Enter weighting factors for the evaluation (does not need to add to 1):")

    while True:
        speed_weight = read_number("Speed weight: ")
        torque_weight = read_number("Torque weight: ")
        cost_weight = read_number("Cost weight: ")

        total_weight = speed_weight + torque_weight + cost_weight

        if min(speed_weight, torque_weight, cost_weight) < 0:
            print("Weights cannot be negative. Try again.\n")
        elif total_weight == 0:
            print("At least one weight must be greater than 0. Try again.\n")
        else:
            break

    # normalize
    return {
        "speed": speed_weight / total_weight,
        "torque": torque_weight / total_weight,
        "cost": cost_weight / total_weight,
    }


def score_range(weights):
    best = 10 * weights["speed"] + 10 * weights["torque"] - 1 * weights["cost"]
    # includes penalty
    worst = 1 * weights["speed"] + 1 * weights["torque"] - 10 * weights["cost"] - 1
    return best, worst


class Design:
    def __init__(self, name, speed, torque, cost, weights):
        self.name = name
        self.speed = speed
        self.torque = torque
        self.cost = cost
        self.weights = weights
        self.score = 0
        self.evaluation = ""
        self.focus = ""

        self.calculate_score()
        self.evaluate_tradeoff()
        self.find_design_focus()

    def calculate_score(self):
        raw = (
            self.speed * self.weights["speed"] +
            self.torque * self.weights["torque"] -
            self.cost * self.weights["cost"]
        )

        # torque penalty
        if self.torque < 5:
            raw -= 1

        # scale 0-100
        best, worst = score_range(self.weights)
        self.score = (raw - worst) / (best - worst) * 100

    def evaluate_tradeoff(self):
        if self.torque < 5:
            self.evaluation = "Fails minimum torque constraint."
        elif self.score >= 75:
            self.evaluation = "Well-balanced trade-off."
        elif self.score >= 50:
            self.evaluation = "Acceptable trade-off, but with limitations."
        else:
            self.evaluation = "Not optimal trade-off."

    def find_design_focus(self):
        if self.speed > self.torque and self.speed > self.cost:
            self.focus = "Performance-focused (speed-driven)"
        elif self.torque > self.speed and self.torque > self.cost:
            self.focus = "Power-focused (torque-driven)"
        elif self.cost < self.speed and self.cost < self.torque:
            self.focus = "Cost-efficient"
        else:
            self.focus = "Balanced properties"

    def display(self):
        print(f"Design: {self.name}")
        print(f" Score: {round(self.score, 1)} / 100")
        print(f" Evaluation: {self.evaluation}")
        print(f" Design Focus: {self.focus}\n")


def main():
    print("Engineering Trade-Off Simulator")
    print("This tool evaluates design choices using simplified engineering assumptions\n")

    # weights
    weights = read_weights()

    print("\nNormalized Weights Applied:")
    print(f" Speed: {round(weights['speed'], 2)}")
    print(f" Torque: {round(weights['torque'], 2)}")
    print(f" Cost: {round(weights['cost'], 2)}\n")

    # designs
    designs = []
    amount_of_designs = read_design_count()

    for i in range(amount_of_designs):
        print(f"\nDesign {i + 1}")
        name = input("Enter design name: ")

        speed = user_input("Enter speed rating (1-10): ")
        torque = user_input("Enter torque rating (1-10): ")
        cost = user_input("Enter cost rating (1-10): ")

        designs.append(Design(name, speed, torque, cost, weights))

    # results
    if amount_of_designs == 1:
        print("\nDesign Evaluation")
        designs[0].display()
    else:
        designs.sort(key=lambda d: d.score, reverse=True)

        print("\nDesign Rankings:")
        for i, design in enumerate(designs, start=1):
            suffix = "th"
            if i == 1:
                suffix = "st"
            elif i == 2:
                suffix = "nd"
            elif i == 3:
                suffix = "rd"

            print(f"{i}{suffix} Place:")
            design.display()

        scores = [d.score for d in designs]
        print("Summary Analysis:")
        print(f" Highest Score: {round(max(scores), 1)}")
        print(f" Average Score: {round(sum(scores) / len(scores), 1)}")
        print(f" Score Range: {round(max(scores) - min(scores), 1)}")


if __name__ == "__main__":
    main()
