def greedy_algorithm(items, budget):

    sorted_list = sorted(
        items.items(), key=lambda i: i[1]["calories"] / i[1]["cost"], reverse=True
    )

    total_cost = 0
    total_calories = 0
    selected_items = []

    for key, value in sorted_list:
        if total_cost + value["cost"] <= budget:
            total_cost += value["cost"]
            total_calories += value["calories"]
            selected_items.append(key)

    return (
        total_cost,
        total_calories,
        selected_items,
    )


def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    item_keys = list(items.keys())

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            item_cost = items[item_keys[i - 1]]["cost"]
            item_calories = items[item_keys[i - 1]]["calories"]
            if item_cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_cost] + item_calories)
            else:
                dp[i][w] = dp[i - 1][w]

    total_calories = dp[n][budget]
    w = budget
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_keys[i - 1])
            w -= items[item_keys[i - 1]]["cost"]

    total_cost = sum(items[item]["cost"] for item in selected_items)

    return total_cost, total_calories, selected_items


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    budget = 100
    greedy_result = greedy_algorithm(items, budget)
    dynamic_result = dynamic_programming(items, budget)

    table_data = [
        ["Algorithm", "Total Cost", "Total Calories", "Items"],
        ["greedy", *greedy_result],
        ["dynamic programming", *dynamic_result],
    ]

    table_str = "\n{:<20} | {:<12} | {:<17} | {}\n".format(*table_data[0])
    for row in table_data[1:]:
        items_str = ", ".join(row[3])
        table_str += "{:<20} | {:<12} | {:<17} | {}\n".format(
            row[0], row[1], row[2], items_str
        )

    print(table_str)