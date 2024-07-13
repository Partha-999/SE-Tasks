import numpy as np
import matplotlib.pyplot as plt
def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c
a, b, c = 0.5, -5, 20
x = np.linspace(0, 10, 100)
y = quadratic_model(x, a, b, c)
plt.scatter(x, y, label='Initial Weather Data', color='blue')
plt.title('Agile Model: Initial Weather Data')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.show()
sprints = 3  
noise_amplitude = 5
for sprint in range(sprints):
    noise = np.random.normal(0, noise_amplitude, size=x.shape)
    y_noisy = y + noise
    plt.scatter(x, y_noisy, label=f'Sprint {sprint + 1}', alpha=0.6)
plt.title('Agile Model: Weather Data Improvement')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.show()
