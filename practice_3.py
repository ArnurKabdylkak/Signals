import numpy as np
from scipy.integrate import odeint, solve_ivp
import matplotlib.pyplot as plt

def system(y, t, x):
    dydt = x(t) - 2 * y
    return dydt

x = lambda t: np.exp(-t) * (t >= 0)

t = np.linspace(0, 10, 1000)

# Initial condition for y
y0 = 0

# Solve the differential equation
y = odeint(system, y0, t, args=(x,))

# Plot the results
plt.plot(t, y, label="y(t)")
plt.plot(t, x(t), label="x(t)", linestyle="--")
plt.legend()
plt.title("Continuous system response")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.show()


N = 50

x = np.zeros(N)
x[0] = 1
x= np.ones(N)
y =  np.zeros(N)

for n in range(1, N):
    y[n] = x[n] + 0.5*y[n-1]

plt.figure(figsize=(10, 6))
plt.stem(range(N), y, basefmt = ' ', label = "y[n] Output")
plt.stem(range(N), x, basefmt = ' ', linefmt= 'r--', markerfmt= 'ro', label= "x[n] Input")
plt.legend()
plt.title("Solution to diff equation")
plt.ylabel("Amplitude")
plt.grid()
plt.show()


def continuous_system(t, y):
    x_t = np.cos(t)  # Input x(t) = cos(t)
    dydt = [y[1], x_t - 3 * y[1] - 2 * y[0]]
    return dydt

# Time range for simulation
t = np.linspace(0, 20, 1000)

# Initial conditions: y(0) = 0, dy/dt(0) = 0
y0 = [0, 0]

# Solve the differential equation
solution = solve_ivp(continuous_system, [t[0], t[-1]], y0, t_eval=t)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(solution.t, solution.y[0], label="y(t) (Output)")
plt.plot(t, np.cos(t), label="x(t) = cos(t) (Input)", linestyle="--")
plt.legend()
plt.title("Response of the Differential Equation")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# 2. Discrete-time system response
N = 50  # Number of samples
x = np.zeros(N)
x[0] = 1  # Impulse input x[n] = delta[n]
y = np.zeros(N)

# Solve the difference equation
y[0] = x[0]
for n in range(1, N):
    y[n] = x[n] + y[n-1] - 0.25 * y[n-2] if n > 1 else x[n] + y[n-1]

plt.figure(figsize=(10, 6))
plt.stem(range(N), y, basefmt=" ", label="y[n] (Output)")
plt.stem(range(N), x, basefmt=" ", linefmt="r--", markerfmt="ro", label="x[n] = delta[n] (Input)")
plt.legend()
plt.title("Discrete-Time System Response")
plt.xlabel("n (Sample Index)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
