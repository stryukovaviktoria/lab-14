import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# === 1) Програма побудови графіка функції ===

def plot_function():
    # Задаємо значення для X
    x = np.linspace(0.1, 5, 100)  # Від 0.1, щоб уникнути ділення на нуль
    # Функція Y(x)
    y = -5 * np.cos(10 * x) * np.sin(3 * x) / (x ** x)

    # Побудова графіка
    plt.plot(x, y, label='Y(x)')
    plt.title('Графік функції Y(x)')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

# === 2) Програма візуалізації даних з порталу відкритих даних з файлу .csv ===

def plot_csv_data():
    # Читання даних з CSV файлу
    data = pd.read_csv('data.csv')

    # Приклад візуалізації даних
    plt.figure(figsize=(10, 6))

    # Побудова стовпчикової діаграми для стовпців 'Category' та 'Values'
    plt.bar(data['Category'], data['Values'])

    plt.title('Візуалізація даних з CSV')
    plt.xlabel('Категорії')
    plt.ylabel('Значення')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# === 3) Програма побудови кругової діаграми ===

def plot_pie_chart():
    # Дані для побудови кругової діаграми
    labels = ['Category A', 'Category B', 'Category C', 'Category D']
    sizes = [25, 35, 20, 20]

    # Побудова кругової діаграми
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Кругова форма
    plt.title('Кругова діаграма')
    plt.show()

# Виконання всіх завдань по черзі
def main():
    print("1) Побудова графіка функції")
    plot_function()

    print("2) Візуалізація даних з CSV файлу")
    plot_csv_data()

    print("3) Побудова кругової діаграми")
    plot_pie_chart()

if __name__ == "__main__":
    main()
