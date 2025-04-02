import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, label="Seno")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.title("Gráfico de una función seno")
plt.legend()
plt.show()
