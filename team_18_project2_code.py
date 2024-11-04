# Equipment data and parameters
ETHANOL_DENSITY = 789  # kg/m^3
GALLONS_PER_CUBIC_METER = 264.172  # gallons/m^3
equipment_data = {
    "fermenter": {
        "Scrap": {"efficiency": 0.5, "cost_per_m3_sec": 320000, "energy_kWh_per_day": 46600},
        "Average": {"efficiency": 0.75, "cost_per_m3_sec": 380000, "energy_kWh_per_day": 47200},
        "Premium": {"efficiency": 0.9, "cost_per_m3_sec": 460000, "energy_kWh_per_day": 47500},
        "World-class": {"efficiency": 0.95, "cost_per_m3_sec": 1100000, "energy_kWh_per_day": 48000}
    },
    "distillation": {
        "Scrap": {"efficiency": 0.81, "cost_per_m3_sec": 390000, "energy_kWh_per_day": 47004},
        "Average": {"efficiency": 0.9, "cost_per_m3_sec": 460000, "energy_kWh_per_day": 47812},
        "Premium": {"efficiency": 0.915, "cost_per_m3_sec": 560000, "energy_kWh_per_day": 48200},
        "World-class": {"efficiency": 0.98, "cost_per_m3_sec": 1370000, "energy_kWh_per_day": 49500}
    },
    "material_removal": {
        "Scrap": {"efficiency": 0.5, "cost_per_m3_sec": 200000, "energy_kWh_per_day": 48800},
        "Average": {"efficiency": 0.75, "cost_per_m3_sec": 240000, "energy_kWh_per_day": 49536},
        "Premium": {"efficiency": 0.9, "cost_per_m3_sec": 280000, "energy_kWh_per_day": 50350},
        "World-class": {"efficiency": 0.98, "cost_per_m3_sec": 480000, "energy_kWh_per_day": 51000}
    },
    "pump": {
        "Cheap": {"efficiency": 0.8, "cost_per_m3_sec_height": 200000},
        "Value": {"efficiency": 0.83, "cost_per_m3_sec_height": 240000},
        "Standard": {"efficiency": 0.86, "cost_per_m3_sec_height": 280000},
        "High-Grade": {"efficiency": 0.89, "cost_per_m3_sec_height": 340000},
        "Premium": {"efficiency": 0.92, "cost_per_m3_sec_height": 415000}
    },
    "pipe": {
        "diameter_costs": {
            0.10: {"Salvage": {"cost": 1000, "friction_factor": 0.05},
                    "Questionable": {"cost": 1200, "friction_factor": 0.03},
                    "Better": {"cost": 1440, "friction_factor": 0.02},
                    "Nice": {"cost": 2160, "friction_factor": 0.01},
                    "Outstanding": {"cost": 2700, "friction_factor": 0.005},
                    "Glorious": {"cost": 2970, "friction_factor": 0.002}},
            0.11: {"Salvage": {"cost": 1200, "friction_factor": 0.05},
                    "Questionable": {"cost": 1440, "friction_factor": 0.03},
                    "Better": {"cost": 1720, "friction_factor": 0.02},
                    "Nice": {"cost": 2580, "friction_factor": 0.01},
                    "Outstanding": {"cost": 3230, "friction_factor": 0.005},
                    "Glorious": {"cost": 3550, "friction_factor": 0.002}},
            0.12: {"Salvage": {"cost": 2570, "friction_factor": 0.05},
                    "Questionable": {"cost": 3080, "friction_factor": 0.03},
                    "Better": {"cost": 3700, "friction_factor": 0.02},
                    "Nice": {"cost": 5550, "friction_factor": 0.01},
                    "Outstanding": {"cost": 6940, "friction_factor": 0.005},
                    "Glorious": {"cost": 7640, "friction_factor": 0.002}},
            0.13: {"Salvage": {"cost": 14000, "friction_factor": 0.05},
                    "Questionable": {"cost": 16000, "friction_factor": 0.03},
                    "Better": {"cost": 20000, "friction_factor": 0.02},
                    "Nice": {"cost": 29000, "friction_factor": 0.01},
                    "Outstanding": {"cost": 37000, "friction_factor": 0.005},
                    "Glorious": {"cost": 40000, "friction_factor": 0.002}},
            0.14: {"Salvage": {"cost": 26000, "friction_factor": 0.05},
                    "Questionable": {"cost": 31000, "friction_factor": 0.03},
                    "Better": {"cost": 37000, "friction_factor": 0.02},
                    "Nice": {"cost": 55000, "friction_factor": 0.01},
                    "Outstanding": {"cost": 69000, "friction_factor": 0.005},
                    "Glorious": {"cost": 76000, "friction_factor": 0.002}},
            0.15: {"Salvage": {"cost": 40000, "friction_factor": 0.05},
                    "Questionable": {"cost": 45000, "friction_factor": 0.03},
                    "Better": {"cost": 52000, "friction_factor": 0.02},
                    "Nice": {"cost": 60000, "friction_factor": 0.01},
                    "Outstanding": {"cost": 70000, "friction_factor": 0.005},
                    "Glorious": {"cost": 80000, "friction_factor": 0.002}}
        },
        "ductwork_costs": {
            1.0: 228,  
            1.25: 414,  
            1.5: 700 
        }
    },
    "bend": {
        "cost": {
            0.1: {20: 100, 30: 105, 45: 110, 60: 116, 75: 122, 90: 128},
            0.11: {20: 149, 30: 157, 45: 164, 60: 173, 75: 181, 90: 190},
            0.12: {20: 493, 30: 517, 45: 543, 60: 570, 75: 599, 90: 700},
            0.13: {20: 1400, 30: 1500, 45: 1600, 60: 1600, 75: 1700, 90: 1800},
            0.14: {20: 3200, 30: 3400, 45: 3600, 60: 3800, 75: 3900, 90: 4100},
            0.15: {20: 6200, 30: 6500, 45: 6900, 60: 7200, 75: 7600, 90: 8000}
        }
    },
    "valve": {
        "cost": {
            0.10: {"Salvage": 100, "Questionable": 120, "Outstanding": 270, "Glorious": 297},
            0.11: {"Salvage": 120, "Questionable": 144, "Outstanding": 323, "Glorious": 355},
            0.12: {"Salvage": 257, "Questionable": 308, "Outstanding": 694, "Glorious": 764},
            0.13: {"Salvage": 630, "Questionable": 756, "Outstanding": 1700, "Glorious": 1900},
            0.14: {"Salvage": 1400, "Questionable": 1600, "Outstanding": 3700, "Glorious": 4000},
            0.15: {"Salvage": 2600, "Questionable": 3100, "Outstanding": 6900, "Glorious": 7600}
        }
    }
}

def calculate_ethanol_output(
    M_in,
    fermenter_tier,
    distillation_tier,
    material_removal_tier,
):
    """
    Calculate the ethanol output by weight, purity, and volume.

    Parameters:
    - M_in (float): Total mass of input corn solution (kg/day)
    - fermenter_tier (str): Tier of fermenter (e.g., "Premium")
    - distillation_tier (str): Tier of distillation unit (e.g., "Premium")
    - material_removal_tier (str): Tier of material removal unit (e.g., "Premium")

    Returns:
    - dict: Contains ethanol mass (kg/day), purity (%), and volume (gallons/day)
    """
    eta_filtration = equipment_data["material_removal"][material_removal_tier]["efficiency"]
    eta_fermenter = equipment_data["fermenter"][fermenter_tier]["efficiency"]
    eta_distillation = equipment_data["distillation"][distillation_tier]["efficiency"]
    eta_dehydration = (equipment_data["material_removal"][material_removal_tier]["efficiency"])
    # Step 1: Initial Masses
    sugar_fraction = 0.20
    water_fraction = 0.60
    fiber_fraction = 0.20

    M_sugar_in = sugar_fraction * M_in
    M_water_in = water_fraction * M_in
    M_fiber_in = fiber_fraction * M_in

    # Step 2: Fermentation
    eta_fermenter = equipment_data["fermenter"][fermenter_tier]["efficiency"]
    M_ethanol_final = eta_fermenter * M_sugar_in #ethanol fermented is equal to final ethanol mass

    # Step 3: Filtration
    # Fiber is fully removed; ethanol and water remain unchanged
    eta_filtration = equipment_data["material_removal"][material_removal_tier]["efficiency"]
    M_fiber_final = M_fiber_in * (1- eta_filtration)*(1 - eta_distillation) # fiber filtered should be fiber in * efficiency of filter, final fiber will be initial fiber - fiber filtered

    # Step 4: Distillation
    M_sugar_final = M_sugar_in * (1 - eta_fermenter) * (1 - eta_distillation) # sugar left after fermentation and distillation

    # Step 5: Dehydration
    # Dehydration removes water to reach desired purity
    M_water_final = M_water_in* (1 - eta_dehydration) * (1 - eta_distillation)

    # Calculate Purity
    purity = ((M_ethanol_final) / (M_ethanol_final + M_water_final + M_fiber_final + M_sugar_final)) * 100  # in percentage

    # Convert Ethanol Mass to Volume
    ethanol_volume = (M_ethanol_final / ETHANOL_DENSITY) * GALLONS_PER_CUBIC_METER  # gallons/day

    return {
        "Ethanol Mass (kg/day)": round(M_ethanol_final, 2),
        "Ethanol Purity (%)": round(purity, 2),
        "Ethanol Volume (gallons/day)": round(ethanol_volume, 2),
        "Ethanol mass left (kg)": round(M_ethanol_final, 2),
        "Total mass left (kg)": round(M_ethanol_final + M_water_final + M_fiber_final + M_sugar_final, 2)
    }

def find_cheapest_configuration(M_in, target_purity=98.0):
    best_cost = float('inf')
    best_config = None

    # Assume a fixed pipe diameter and bend angle
    fixed_pipe_diameter = 0.12
    fixed_bend_angle = 90

    for fermenter_tier in equipment_data["fermenter"]:
        for distillation_tier in equipment_data["distillation"]:
            for material_removal_tier in equipment_data["material_removal"]:
                for pipe_tier, pipe_data in equipment_data["pipe"]["diameter_costs"][fixed_pipe_diameter].items():
                    for valve_tier, valve_cost in equipment_data["valve"]["cost"][fixed_pipe_diameter].items():
                        output = calculate_ethanol_output(
                            M_in,
                            fermenter_tier,
                            distillation_tier,
                            material_removal_tier,
                        )
                        if output["Ethanol Purity (%)"] >= target_purity:
                            cost = (
                                equipment_data["fermenter"][fermenter_tier]["cost_per_m3_sec"] +
                                equipment_data["distillation"][distillation_tier]["cost_per_m3_sec"] +
                                equipment_data["material_removal"][material_removal_tier]["cost_per_m3_sec"] +
                                (pipe_data["cost"] * 90) +  # 90 meters of pipe
                                (equipment_data["bend"]["cost"][fixed_pipe_diameter][fixed_bend_angle] * 2) +  # 2 bends
                                (valve_cost * 8)  # 8 valves
                            )
                            if cost < best_cost:
                                best_cost = cost
                                best_config = {
                                    "fermenter_tier": fermenter_tier,
                                    "distillation_tier": distillation_tier,
                                    "material_removal_tier": material_removal_tier,
                                    "pipe_diameter": fixed_pipe_diameter,
                                    "pipe_tier": pipe_tier,
                                    "bend_angle": fixed_bend_angle,
                                    "valve_tier": valve_tier,
                                    "cost": cost,
                                    "output": output
                                }

    return best_config
def main():
    # Example Input Parameters

    M_in = 2000000 # kg/day, example initial mass of corn solution

    # Select equipment tiers
    fermenter_tier = "World-class"          # Options: "Scrap", "Average", "Premium", "World-class"
    distillation_tier = "World-class"       # Options: "Scrap", "Average", "Premium", "World-class"
    material_removal_tier = "World-class"  # Options: "Scrap", "Average", "Premium", "World-class"

    # Calculate Ethanol Output
    output = calculate_ethanol_output(
        M_in,
        fermenter_tier,
        distillation_tier,
        material_removal_tier,
    )

    # Display Results
    print("=== Ethanol Production Output ===")
    print(f"Initial Corn Solution Mass: {M_in} kg/day")
    print(f"Fermenter Tier: {fermenter_tier} (Efficiency: {equipment_data['fermenter'][fermenter_tier]['efficiency']})")
    print(f"Distillation Tier: {distillation_tier} (Efficiency: {equipment_data['distillation'][distillation_tier]['efficiency']})")
    print(f"Material Removal Tier: {material_removal_tier} (Efficiency: {equipment_data['material_removal'][material_removal_tier]['efficiency']})")
    print("-----------------------------------")
    print(f"Ethanol Output Mass: {output['Ethanol Mass (kg/day)']} kg/day")
    print(f"Ethanol Purity: {output['Ethanol Purity (%)']}%")
    print(f"Ethanol Output Volume: {output['Ethanol Volume (gallons/day)']} gallons/day")
    print(f"Ethanol mass left: {output['Ethanol mass left (kg)']} kg/day")
    print(f"Total mass left: {output['Total mass left (kg)']} kg/day")
    print("-----------------------------------")

    # Check Against Target
    target_volume = 100000  # gallons/day
    target_purity = 98.0     # percent

    meets_volume = output["Ethanol Volume (gallons/day)"] >= target_volume
    meets_purity = output["Ethanol Purity (%)"] >= target_purity

    print(f"Meets Target Volume (100,000 gallons/day): {'Yes' if meets_volume else 'No'}")
    print(f"Meets Target Purity (98%): {'Yes' if meets_purity else 'No'}")

    # Find the cheapest configuration to achieve the target purity
    best_config = find_cheapest_configuration(M_in)

    if best_config:
        # Display Results
        print("=== Cheapest Configuration to Achieve 98% Purity ===")
        print(f"Fermenter Tier: {best_config['fermenter_tier']}")
        print(f"Distillation Tier: {best_config['distillation_tier']}")
        print(f"Material Removal Tier: {best_config['material_removal_tier']}")
        print(f"Pipe Diameter: {best_config['pipe_diameter']} meters")
        print(f"Pipe Tier: {best_config['pipe_tier']}")
        print(f"Bend Angle: {best_config['bend_angle']} degrees")
        print(f"Valve Tier: {best_config['valve_tier']}")
        print(f"Total Cost: ${best_config['cost']}")
        print(f"Ethanol Output Mass: {best_config['output']['Ethanol Mass (kg/day)']} kg/day")
        print(f"Ethanol Purity: {best_config['output']['Ethanol Purity (%)']}%")
        print(f"Ethanol Output Volume: {best_config['output']['Ethanol Volume (gallons/day)']} gallons/day")
    else:
        print("No suitable configuration found to achieve the target purity.")

if __name__ == "__main__":
    main()