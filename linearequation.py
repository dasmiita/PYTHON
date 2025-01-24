import numpy as np
import matplotlib.pyplot as plt

# Prompt user for coefficients
print("Enter the coefficients for the equations (Ax + By = C):")

# First equation
a1 = float(input("Enter A1: "))
b1 = float(input("Enter B1: "))
c1 = float(input("Enter C1: "))

# Second equation
a2 = float(input("Enter A2: "))
b2 = float(input("Enter B2: "))
c2 = float(input("Enter C2: "))

# Define matrices for solving
coef = np.array([[a1, b1], [a2, b2]])  # Coefficient matrix
const = np.array([c1, c2])             # Constants matrix

try:
    # Solve for x and y
    valx, valy = np.linalg.solve(coef, const)
    print(f"\nSolution: x = {valx:.2f}, y = {valy:.2f}")

    # Generate x values
    x_vals = np.linspace(-10, 10, 400)

    # Compute y values for both lines
    y1_vals = (c1 - a1 * x_vals) / b1
    y2_vals = (c2 - a2 * x_vals) / b2

    # Plot equations
    plt.plot(x_vals, y1_vals, label=f"{a1}x + {b1}y = {c1}")
    plt.plot(x_vals, y2_vals, label=f"{a2}x + {b2}y = {c2}")

    # Plot solution point
    plt.scatter(valx, valy, color='red', zorder=5, label=f"Solution: ({valx:.2f}, {valy:.2f})")

    # Format the graph
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title("Graphical Solution of Linear Equations")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

except np.linalg.LinAlgError:
    print("\nNo unique solution exists (the equations may be inconsistent or dependent).")
