# FireHydrant-Calculation
Calculating pip flow metrics
# Water Jet Height Calculation

## Overview
This script calculates the **maximum height** that a water jet can reach when exiting a hole of varying **diameters** and under different **pressures**. It uses **Torricelli's Theorem** to determine the velocity of the water and subsequently compute the height.

## Formulae Used
### 1. **Velocity Calculation (Torricelli’s Theorem)**
The velocity of the water exiting the hole is calculated using:

$\[ v = \sqrt{\frac{2 P}{\rho}} \]$

Where:
- $\( v \)$ = velocity of the water (m/s)
- $\( P \)$ = pressure (Pa)
- $\( \rho \)$ = density of water (1000 kg/m³)

### 2. **Height Calculation**
The height the water jet reaches is given by:

$\[ h = \frac{v^2}{2g} \]$

Where:
- $\( h \)$ = maximum height (m)
- $\( g \)$ = acceleration due to gravity (9.81 m/s²)

## Code Explanation
The function `calculate_jet_height(diameter_inches, pressure_psi)` takes **multiple diameters** and **multiple pressure values** as inputs. It iterates through all combinations and calculates:
- Velocity of water exiting the hole
- Maximum height in meters and feet

### **Inputs**
- `diameter_inches`: List of hole diameters (in inches)
- `pressure_psi`: List of water pressures (in PSI)

### **Outputs**
A **DataFrame** with the following columns:
- `Diameter (in)`: Diameter of the hole in inches
- `Pressure (PSI)`: Pressure in PSI
- `Pressure (BAR)`: Pressure converted to BAR
- `Velocity (m/s)`: Velocity of the water exiting the hole
- `Max Height (m)`: Maximum height in meters
- `Max Height (ft)`: Maximum height in feet

## Example Usage
### Input
```python
pressure_values = [40, 50, 60, 80, 100]  # PSI values
diameter_values = [0.5, 1.0, 1.5]  # Hole diameters in inches

df_results = calculate_jet_height(diameter_values, pressure_values)
print(df_results)
```

### Expected Output
A DataFrame showing calculated velocities and heights for different **diameters** and **pressures**.

| Diameter (in) | Pressure (PSI) | Pressure (BAR) | Velocity (m/s) | Max Height (m) | Max Height (ft) |
|--------------|--------------|--------------|--------------|--------------|--------------|
| 0.5          | 40           | 2.76         | 8.37         | 3.57         | 11.7         |
| 1.0          | 40           | 2.76         | 8.37         | 3.57         | 11.7         |
| 1.5          | 40           | 2.76         | 8.37         | 3.57         | 11.7         |
| 0.5          | 100          | 6.90         | 13.27        | 8.98         | 29.4         |
| 1.0          | 100          | 6.90         | 13.27        | 8.98         | 29.4         |
| 1.5          | 100          | 6.90         | 13.27        | 8.98         | 29.4         |

## Notes
- Higher **pressure** results in a greater **velocity** and **higher water spray**.
- Larger **hole diameters** do not affect height but can affect **flow rate**.

## Applications
This calculation is useful for:
- **Fire hydrant leakage analysis** (e.g., unauthorized openings)
- **Municipal water system analysis**
- **Hydraulic engineering and plumbing design**

