import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
def read_coefficients(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [tuple(map(float, line.strip().split())) for line in lines]
def plot_temperature(coefficients):
    x = np.linspace(0, 24, 100)
    for idx, (a, b, c) in enumerate(coefficients):
        y = a * x**2 + b * x + c
        noise = np.random.normal(0, 5, size=x.shape)
        y_noisy = y + noise
        plt.scatter(x, y_noisy, label=f'Temperature Model {idx + 1}')
    plt.xlabel('Time (hours)')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()
def open_file():
    filename = filedialog.askopenfilename(title="Select file", filetypes=[("Text files", "*.txt")])
    if filename:
        coefficients = read_coefficients(filename)
        plot_temperature(coefficients)
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Weather Modeling Software")
    open_button = tk.Button(root, text="Open Coefficients File", command=open_file)
    open_button.pack(pady=20)
    root.mainloop()
