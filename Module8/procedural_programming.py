# Example of procedural procedural programming
from Module3.Sets import prerja


def calculate_area(length,width):
    return length*width


def calculate_perimimiter(length, width):
    return 2*(length+width)

length = 5
width= 3

area= calculate_area(length,width)
perimiter= calculate_perimimiter(length,width)

print(f"Area:{area}")
print(f"Perimiter: {perimiter}")
