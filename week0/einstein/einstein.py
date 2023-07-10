def calculate_energy(mass):
    speed_of_light = 300000000  # meters per second
    calculated_energy = mass * speed_of_light ** 2
    return calculated_energy

mass = int(input("m: "))
energy = calculate_energy(mass)
print(f"E: {energy} ")
