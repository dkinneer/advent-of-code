from main3 import Solver

def test_example():
    solver = Solver()

    assert solver.solve(['987654321111111']) == 98
    assert solver.solve(['811111111111119']) == 89
    assert solver.solve(['234234234234278']) == 78
    assert solver.solve(['818181911112111']) == 92