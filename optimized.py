import csv
budget = 500
actions = [
    {"name": "Action-1", "price": 20, "profit": 5},
    {"name": "Action-2", "price": 30, "profit": 10},
    {"name": "Action-3", "price": 50, "profit": 15},
    {"name": "Action-4", "price": 70, "profit": 20},
    {"name": "Action-5", "price": 60, "profit": 17},
    {"name": "Action-6", "price": 80, "profit": 25},
    {"name": "Action-7", "price": 22, "profit": 7},
    {"name": "Action-8", "price": 26, "profit": 11},
    {"name": "Action-9", "price": 48, "profit": 13},
    {"name": "Action-10", "price": 34, "profit": 27},
    {"name": "Action-11", "price": 42, "profit": 17},
    {"name": "Action-12", "price": 110, "profit": 9},
    {"name": "Action-13", "price": 38, "profit": 23},
    {"name": "Action-14", "price": 14, "profit": 1},
    {"name": "Action-15", "price": 18, "profit": 3},
    {"name": "Action-16", "price": 8, "profit": 8},
    {"name": "Action-17", "price": 4, "profit": 12},
    {"name": "Action-18", "price": 10, "profit": 14},
    {"name": "Action-19", "price": 24, "profit": 21},
    {"name": "Action-20", "price": 114, "profit": 18}
]


def read_csv(file):
    with open(f"./data/{file}.csv", 'r') as file:
        data = csv.DictReader(file)
        actions = list(data)
        return actions


def knapsack(actions):
    # remove null or negative profit actions
    filtered_actions = [
        action for action in actions if float(action['profit']) > 0 and float(action["price"]) > 0]

    # sort the actions by highest profit (knapsack method)
    sorted_actions = sorted(
        filtered_actions, key=lambda action: float(action["profit"]), reverse=True)
    return sorted_actions


def select_actions(actions):
    selected_actions = []
    generated_profit = 0
    total_cost = 0

    for action in actions:
        if total_cost + float(action["price"]) <= float(budget):
            selected_actions.append(action)
            generated_profit += float(action["price"]) * \
                (float(action["profit"])/100)
            total_cost += float(action["price"])

    print("Selected Actions:", len(selected_actions))
    print("Total Profits:", generated_profit)
    print("Total Cost:", total_cost)


def main():
    select_actions(knapsack(read_csv("dataset1")))
    # select_actions(knapsack(read_csv("dataset2")))
    # select_actions(knapsack(actions))


if __name__ == '__main__':
    import cProfile
    import pstats
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('ncalls')
    stats.print_stats()
