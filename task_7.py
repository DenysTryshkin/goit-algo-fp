import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    # Ініціалізуємо словник для підрахунку кожної можливої суми
    outcomes = {i: 0 for i in range(2, 13)}

    # Виконуємо симуляцію кидків кубиків
    for _ in range(num_rolls):
        roll = random.randint(1, 6) + random.randint(1, 6)
        outcomes[roll] += 1

    # Обчислюємо ймовірності
    for key in outcomes:
        outcomes[key] /= num_rolls

    return outcomes

def plot_probabilities(outcomes):
    # Витягуємо суми та ймовірності для графіка
    sums = list(outcomes.keys())
    probabilities = list(outcomes.values())

    # Побудова гістограми
    plt.bar(sums, probabilities, tick_label=sums, color='skyblue')
    plt.xlabel('Sum')
    plt.ylabel('Probability')
    plt.title('Probabilities of Sums of Two Dice Rolls')
    plt.show()

# Кількість кидків
num_rolls = 10000
# Отримуємо результати симуляції
outcomes = simulate_dice_rolls(num_rolls)
# Виводимо результати
print(outcomes)
# Побудова графіка
plot_probabilities(outcomes)
