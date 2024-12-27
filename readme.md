Sure, here is the structured explanation in English:

---

### 1. **Continuous System using `odeint`**

#### Code:
```python
def system(y, t, x):
    dydt = x(t) - 2 * y
    return dydt

x = lambda t: np.exp(-t) * (t >= 0)
t = np.linspace(0, 10, 1000)
y0 = 0
y = odeint(system, y0, t, args=(x,))
```

#### Explanation:
- The **`system`** function defines the differential equation \(\frac{dy(t)}{dt} + 2y(t) = x(t)\), where \(x(t)\) is the input function.
- **`x`** is the function \(x(t) = e^{-t} \cdot u(t)\), representing an exponentially decaying signal active for \(t \geq 0\).
- **`odeint`** numerically solves the differential equation using the Runge-Kutta method.
- **`y0`** is the initial condition \(y(0) = 0\).

---

### 2. **Plot for Continuous System**
```python
plt.plot(t, y, label="y(t)")
plt.plot(t, x(t), label="x(t)", linestyle="--")
```

#### Explanation:
- Two plots are displayed:
  - \(y(t)\) — the output response of the system.
  - \(x(t)\) — the input signal (dashed line for visual distinction).
- This demonstrates how the system reacts to the input signal \(x(t)\), confirming causality (dependence on current and past time values).

---

### 3. **Discrete System**

#### Code:
```python
x = np.zeros(N)
x[0] = 1
y = np.zeros(N)
for n in range(1, N):
    y[n] = x[n] + 0.5 * y[n - 1]
```

#### Explanation:
- The difference equation \(y[n] - 0.5y[n-1] = x[n]\) is solved with \(x[n] = 1\) for all \(n\).
- The **`for` loop**:
  - At each step \(n\), the value of \(y[n]\) is calculated, depending on the current \(x[n]\) and the previous value \(y[n-1]\).
- \(x[n]\) is the input signal, which is constant at 1.

---

### 4. **Plot for Discrete System**
```python
plt.stem(range(N), y, basefmt=" ", label="y[n] Output")
plt.stem(range(N), x, basefmt=" ", linefmt="r--", markerfmt="ro", label="x[n] Input")
```

#### Explanation:
- The **`stem` plot** visualizes the impulse response:
  - \(y[n]\) — output signal.
  - \(x[n]\) — input signal.

---

### 5. **Continuous System using `solve_ivp`**

#### Code:
```python
def continuous_system(t, y):
    x_t = np.cos(t)
    dydt = [y[1], x_t - 3 * y[1] - 2 * y[0]]
    return dydt
```

#### Explanation:
- The second-order differential equation \(\frac{d^2y(t)}{dt^2} + 3\frac{dy(t)}{dt} + 2y(t) = x(t)\), where \(x(t) = \cos(t)\), is solved.
- The `solve_ivp` method is used to numerically solve this equation.

---

### 6. **Plot for Second Continuous Equation**
```python
plt.plot(solution.t, solution.y[0], label="y(t) (Output)")
plt.plot(t, np.cos(t), label="x(t) = cos(t) (Input)", linestyle="--")
```

#### Explanation:
- The output signal \(y(t)\) demonstrates the system's response to the harmonic input \(x(t) = \cos(t)\).

---

### 7. **Discrete System with Impulse Input**

#### Code:
```python
y[0] = x[0]
for n in range(1, N):
    y[n] = x[n] + y[n-1] - 0.25 * y[n-2] if n > 1 else x[n] + y[n-1]
```

#### Explanation:
- The equation \(y[n] - y[n-1] + 0.25y[n-2] = x[n]\) with an impulse input \(x[n] = \delta[n]\) is solved.
- The **`if n > 1`**: For \(n = 1\), the equation simplifies as \(y[n-2]\) does not exist.

---

### 8. **Plot for Discrete System with Impulse**
```python
plt.stem(range(N), y, basefmt=" ", label="y[n] (Output)")
plt.stem(range(N), x, basefmt=" ", linefmt="r--", markerfmt="ro", label="x[n] = delta[n] (Input)")
```

#### Explanation:
- The impulse response \(y[n]\) is visualized for the input signal \(x[n]\), showing the system’s behavior based on its memory.

---