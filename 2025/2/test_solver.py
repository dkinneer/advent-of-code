from main2part2 import Solver

def test_example():
    solver = Solver()

    #assert solver.solve(['11-22']) == 33
    #assert solver.solve(['95-115']) == 210
    assert solver.solve(['1000-1000']) == 0
    