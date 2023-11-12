import numpy as np

# Given parameters
g = 9.8  # gravitational constant (m/s^2)
m = 68.1  # mass of the parachutist (kg)
c = 12.5  # drag coefficient (kg/s)

# Velocity function
def v(t):
    return g * m / c * (1 - np.exp(-c / m * t))

# Trapezoidal rule for equally spaced segments
def trapezoidal_rule(t, segments):
    dt = t / segments
    time_points = np.linspace(0, t, segments + 1)
    integral = 0.5 * (v(time_points[0]) + v(time_points[-1]))

    for i in range(1, segments):
        integral += v(time_points[i])

    return g * m / c * dt * integral

# Simpson's rule for equally spaced segments
def simpsons_rule(t, segments):
    dt = t / segments
    time_points = np.linspace(0, t, segments + 1)
    integral = v(time_points[0]) + v(time_points[-1])

    for i in range(1, segments, 2):
        integral += 4 * v(time_points[i])

    for i in range(2, segments - 1, 2):
        integral += 2 * v(time_points[i])

    return g * m / (3 * c) * dt * integral

# Trapezoidal rule for unequally spaced segments
def trapezoidal_unequal(t, time_points):
    integral = 0.5 * (v(time_points[0]) + v(time_points[-1]))

    for i in range(1, len(time_points) - 1):
        integral += v(time_points[i])

    return g * m / c * np.diff(time_points).mean() * integral

# Analytical solution
analytical_solution = 289.43515

# Perform integration for different methods and numbers of segments
segment_counts = [2, 5, 10, 100, 1000]
results = {}

for segments in segment_counts:
    # Trapezoidal rule for equally spaced segments
    trapezoidal_result = trapezoidal_rule(10, segments)
    results[("Trapezoidal", segments)] = trapezoidal_result

    # Simpson's rule for equally spaced segments
    simpsons_result = simpsons_rule(10, segments)
    results[("Simpsons", segments)] = simpsons_result

# Unequally spaced segments (for demonstration purposes)
unequal_time_points = np.sort(np.random.uniform(0, 10, 100))
trapezoidal_unequal_result = trapezoidal_unequal(10, unequal_time_points)
results[("Trapezoidal Unequal", len(unequal_time_points))] = trapezoidal_unequal_result

# Output the results
for method, segments in results.keys():
    print(f"Method: {method}, Segments: {segments}, Distance: {results[(method, segments)]}")

# Compare with the analytical solution
print("\nAnalytical Solution:", analytical_solution)
print("Results:", results)