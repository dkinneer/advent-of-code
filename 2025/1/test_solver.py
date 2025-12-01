from mainpart2 import Solver

def test_example():
    solver = Solver(50)
    
    assert solver.get_between_zeros("L68") == 1
    assert solver.get_between_zeros("L30") == 0
    assert solver.get_between_zeros("R48") == 1 
    assert solver.get_between_zeros("L5") == 0
    assert solver.get_between_zeros("R60") == 1
    assert solver.get_between_zeros("L55") == 1
    assert solver.get_between_zeros("L1") == 0
    assert solver.get_between_zeros("L99") == 1
    assert solver.get_between_zeros("R14") == 0
    assert solver.get_between_zeros("L82") == 1
