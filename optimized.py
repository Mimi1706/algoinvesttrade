import csv
budget = 500
actions = []

with open("./data/dataset2.csv", 'r') as file:
    data = csv.DictReader(file)
    actions = list(data)

number_of_actions = len(actions)

filtered_actions = [
    action for action in actions if float(action['profit']) > 0 and float(action["price"]) > 0]

sorted_actions = sorted(
    filtered_actions, key=lambda action: float(action["profit"]), reverse=True)

selected_actions = []
generated_profit = 0
total_cost = 0

for action in sorted_actions:
    if total_cost + float(action["price"]) <= budget:
        selected_actions.append(action)
        generated_profit += float(action["price"]) * \
            (float(action["profit"])/100)
        total_cost += float(action["price"])

print("Selected Actions:", selected_actions)
print("Total Profits:", generated_profit)
print("Total Cost:", total_cost)
