import numpy as np
import matplotlib.pyplot as plt
import math

def plot():
    # User input in Ax + By = C format
    print("Enter the coefficients for two equations in the form Ax + By = C:")

    # First equation
    a1 = float(input("Enter A1: "))
    b1 = float(input("Enter B1: "))
    c1 = float(input("Enter C1: "))

    # Second equation
    a2 = float(input("Enter A2: "))
    b2 = float(input("Enter B2: "))
    c2 = float(input("Enter C2: "))

    # Compute slopes
    slope1 = -a1 / b1
    slope2 = -a2 / b2

    # Calculate angle between the two lines
    angle_rad = math.atan(abs((slope2 - slope1) / (1 + slope1 * slope2)))
    angle_deg = math.degrees(angle_rad)
    print(f"Angle between the lines: {angle_deg:.2f} degrees")

    # Generate x values for the plot
    val = np.linspace(-10, 10, 400)
    
    # Compute y values for the lines
    val1 = (c1 - a1 * val) / b1
    val2 = (c2 - a2 * val) / b2

    # Plot the lines
    plt.plot(val, val1, label=f"{a1}x + {b1}y = {c1}")
    plt.plot(val, val2, label=f"{a2}x + {b2}y = {c2}")

    # Add axis lines, grid, and legend
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()

    # Show the plot
    plt.show()

# Run the function
plot()
