from itertools import combinations

budget = 500
actions = [
    {"name": "Action-1", "cost": 20, "profit": 0.05},
    {"name": "Action-2", "cost": 30, "profit": 0.1},
    {"name": "Action-3", "cost": 50, "profit": 0.15},
    {"name": "Action-4", "cost": 70, "profit": 0.2},
    {"name": "Action-5", "cost": 60, "profit": 0.17},
    {"name": "Action-6", "cost": 80, "profit": 0.25},
    {"name": "Action-7", "cost": 22, "profit": 0.07},
    {"name": "Action-8", "cost": 26, "profit": 0.11},
    {"name": "Action-9", "cost": 48, "profit": 0.13},
    {"name": "Action-10", "cost": 34, "profit": 0.27},
    {"name": "Action-11", "cost": 42, "profit": 0.17},
    {"name": "Action-12", "cost": 110, "profit": 0.09},
    {"name": "Action-13", "cost": 38, "profit": 0.23},
    {"name": "Action-14", "cost": 14, "profit": 0.01},
    {"name": "Action-15", "cost": 18, "profit": 0.03},
    {"name": "Action-16", "cost": 8, "profit": 0.08},
    {"name": "Action-17", "cost": 4, "profit": 0.12},
    {"name": "Action-18", "cost": 10, "profit": 0.14},
    {"name": "Action-19", "cost": 24, "profit": 0.21},
    {"name": "Action-20", "cost": 114, "profit": 0.18}
]


def combine_actions(actions):
    combinations_list = []
    for r in range(1, len(actions) + 1):
        combinations_list.extend(combinations(actions, r))
    return combinations_list


def keep_valid_combinations(combinations):
    valid_combinations = []
    for combination in combinations:
        total_cost = sum(action["cost"] for action in combination)
        if total_cost <= float(budget):
            valid_combinations.append(combination)
    return valid_combinations


def find_best_combination(combinations):
    best_combination = None
    total_cost = 0
    best_benefits = 0

    for combination in combinations:
        total_cost = sum(action["cost"] for action in combination)
        total_benefits = sum(
            action["cost"] * action["profit"] for action in combination)
        if total_benefits > best_benefits:
            best_benefits = total_benefits
            best_combination = combination

    print("Best Combination:", best_combination)
    print("Total Cost:", total_cost)
    print("Total Benefits:", best_benefits)


def main():
    find_best_combination(
        keep_valid_combinations(combine_actions(actions)))


if __name__ == '__main__':
    import cProfile
    import pstats
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('ncalls')
    stats.print_stats()
