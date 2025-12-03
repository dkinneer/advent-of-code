from day2_part2 import Solver

def test_example():
    solver = Solver()

    assert solver.solve(['11-22']) == 33
    assert solver.solve(['95-115']) == 210
    assert solver.solve(['998-1012']) == 2009
    assert solver.solve(['1188511880-1188511890']) == 1188511885
    assert solver.solve(['222220-222224']) == 222222
    assert solver.solve(['1698522-1698528']) == 0
    assert solver.solve(['446443-446449']) == 446446
    assert solver.solve(['38593856-38593862']) == 38593859
    assert solver.solve(['565653-565659']) == 565656
    assert solver.solve(['824824821-824824827']) == 824824824
    assert solver.solve(['2121212118-2121212124']) == 2121212121