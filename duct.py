
def calculate_pressure_drop(Dh, length, velocity, friction_factor=0.02, density=1.184):
    # air density in kg/m^3
    SP = (friction_factor * length *
          (density * velocity ** 2)) / (2 * Dh)
    VP = 0.5 * density * velocity**2
    print(f"{SP=:.3f}\t{VP=:.3f}")
    pressure_drop = VP + SP
    return pressure_drop


def calculate_hydraulic_diameter(width, height):
    perimeter = 2 * (width + height)
    area = width * height
    hydraulic_diameter = (4 * area) / perimeter

    return hydraulic_diameter


duct = (47e-2, 47e-2)  # width , height
Dh = calculate_hydraulic_diameter(*duct)
print(f"{Dh=}")

hydraulic_diameter = Dh  # meters
air_flow_rate = 10200  # cfm
length = 16 + 9  # m
pressure_drop = calculate_pressure_drop(hydraulic_diameter, length, 21.7)
print(f"Pressure Drop: {pressure_drop=:.3f} Pa")
