from shapes.area.functions import calculate_square_area
from shapes.area.functions import calculate_rectangle_area
from shapes.volume.functions import calculate_cube_volume
from shapes.volume.functions import calculate_rectangular_cube

square_area = calculate_square_area(2)
rectangle_area = calculate_rectangle_area(length=3, width=4)
cube = calculate_cube_volume(4)
rectangle_cube = calculate_rectangular_cube(length=3, width=2, height=5)

print(f'Square Area: {square_area}')
print(f'Rectangle Area: {rectangle_area}')
print(f'Cube: {cube}')
print(f'Rectangular Cube: {rectangle_cube}')

