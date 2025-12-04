from day3_part1 import Solver as Solver1
from day3_part2 import Solver as Solver2

def test_example_part1():
    solver = Solver1()

    assert solver.solve('987654321111111') == 98
    assert solver.solve('811111111111119') == 89
    assert solver.solve('234234234234278') == 78
    assert solver.solve('818181911112111') == 92

def test_example_part2():
    solver = Solver2()

    assert solver.solve('987654321111111') == 987654321111
    assert solver.solve('811111111111119') == 811111111119
    assert solver.solve('234234234234278') == 434234234278
    assert solver.solve('818181911112111') == 888911112111
