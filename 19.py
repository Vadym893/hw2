a = float(input("write the length of the side of the cube: "))

volume = a ** 3
surface_area = 6 * (a ** 2)

print("Cube side:", a)
print("Cube volume:", round(volume),2)
print("Cube surface area:", round(surface_area,2))