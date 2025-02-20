import numpy as np
import pandas as pd

def calculate_jet_height(diameter_inches, pressure_psi):
    """
    Calculate the maximum height of a water jet for given hole diameters and pressures.
    
    Parameters:
    - diameter_inches: List or array of hole diameters in inches
    - pressure_psi: List or array of pressure values in PSI
    
    Returns:
    - DataFrame with velocity and maximum height results for each diameter and pressure combination
    """
    g = 9.81  # gravity (m/s²)
    psi_to_pa = 6895  # conversion factor from PSI to Pascals
    rho = 1000  # density of water (kg/m³)
    
    # Ensure inputs are NumPy arrays
    diameter_inches = np.array(diameter_inches)
    pressure_psi = np.array(pressure_psi)
    
    results = []
    
    for diameter in diameter_inches:
        # Convert diameter to meters
        diameter_m = diameter * 0.0254
        
        for pressure in pressure_psi:
            # Convert pressure to Pascals
            pressure_pa = pressure * psi_to_pa
            
            # Calculate velocity using Torricelli’s equation: v = sqrt(2P/ρ)
            velocity_mps = np.sqrt(2 * pressure_pa / rho)
            
            # Calculate maximum height using h = v^2 / (2g)
            height_m = (velocity_mps ** 2) / (2 * g)
            height_ft = height_m * 3.281  # Convert meters to feet
            
            results.append({
                "Diameter (in)": diameter,
                "Pressure (PSI)": pressure,
                "Pressure (BAR)": pressure * 0.06895,
                "Velocity (m/s)": velocity_mps,
                "Max Height (m)": height_m,
                "Max Height (ft)": height_ft
            })
    
    return pd.DataFrame(results)

# Example usage:
pressure_values = [40, 50, 60, 80, 100]  # PSI values
diameter_values = [0.5, 1.0, 1.5]  # Different hole diameters in inches

# Calculate and display results
df_results = calculate_jet_height(diameter_values, pressure_values)
print(df_results)
