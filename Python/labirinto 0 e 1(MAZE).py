from mazelib import Maze
from mazelib.generate.Prims import Prims
m = Maze()
m.generator = Prims(10, 10)
m.generate()

m.generate_entrances()

print("Labirinto:")
print(m.grid)

print("Entrada:", m.start)
print("Saída:", m.end)