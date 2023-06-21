budget = 500
actions = [
    {"name": "Action-1", "cost": 20, "rate": 0.05},
    {"name": "Action-2", "cost": 30, "rate": 0.1},
    {"name": "Action-3", "cost": 50, "rate": 0.15},
    {"name": "Action-4", "cost": 70, "rate": 0.2},
    {"name": "Action-5", "cost": 60, "rate": 0.17},
    {"name": "Action-6", "cost": 80, "rate": 0.25},
    {"name": "Action-7", "cost": 22, "rate": 0.07},
    {"name": "Action-8", "cost": 26, "rate": 0.11},
    {"name": "Action-9", "cost": 48, "rate": 0.13},
    {"name": "Action-10", "cost": 34, "rate": 0.27},
    {"name": "Action-11", "cost": 42, "rate": 0.17},
    {"name": "Action-12", "cost": 110, "rate": 0.09},
    {"name": "Action-13", "cost": 38, "rate": 0.23},
    {"name": "Action-14", "cost": 14, "rate": 0.01},
    {"name": "Action-15", "cost": 18, "rate": 0.03},
    {"name": "Action-16", "cost": 8, "rate": 0.08},
    {"name": "Action-17", "cost": 4, "rate": 0.12},
    {"name": "Action-18", "cost": 10, "rate": 0.14},
    {"name": "Action-19", "cost": 24, "rate": 0.21},
    {"name": "Action-20", "cost": 114, "rate": 0.18}
]

number_of_actions = len(actions)
for action in actions:
    action["profit"] = action["cost"] * action["rate"]

sorted_actions = sorted(
    actions, key=lambda action: action["profit"], reverse=True)

selected_actions = []
total_cost = 0

for action in sorted_actions:
    if total_cost + action["cost"] <= budget:
        selected_actions.append(action)
        total_cost += action["cost"]

print("Selected Actions:", selected_actions)
print("Total Profits:", sum(action["profit"] for action in selected_actions))
print("Total Cost:", total_cost)
