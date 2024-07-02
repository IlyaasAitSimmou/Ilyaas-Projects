from project import *
import pytest
def test_trajectory_angle():
    test_set1 = trajectory_angle(3, 15, 0.44, 0.98)
    assert round(test_set1[0]*(180/pi), 4) == 14.0037
    assert round(test_set1[1]*(180/pi), 4) == 86.2003
    assert round(trajectory_angle(10, 40, 10, 0)[0]*(180/pi), 4) == -43.2950
    with pytest.raises(ZeroDivisionError):
        trajectory_angle(0, 40, 0, 0)[0]*(180/pi)
    with pytest.raises(ValueError):
        trajectory_angle(1000, 40, 10, 0)[0]*(180/pi)

def test_trajectory_function():
    assert round(trajectory_function(trajectory_angle(3, 15, 0.44, 0.98)[0], 3, 15, 0.44), 2) == round(trajectory_function(trajectory_angle(3, 15, 0.44, 0.98)[1], 3, 15, 0.44), 2)



def test_get_plotting_points():
    assert round(get_plotting_points(trajectory_angle(3, 15, 0.44, 0.98)[0], 15, 0.44, trajectory_function)[0][-1], 2) == round(inverse_trajectory_function(trajectory_angle(3, 15, 0.44, 0.98)[0], 0, 15, 0.44)[1], 2)
    assert round(get_plotting_points(trajectory_angle(10, 30, 0, 5)[1], 30, 0, trajectory_function)[1][-1], 3) == round(trajectory_function(trajectory_angle(10, 30, 0, 5)[1], get_plotting_points(trajectory_angle(10, 30, 0, 5)[1], 30, 0, trajectory_function)[0][-1], 30, 0), 3)


