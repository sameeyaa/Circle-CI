#line fitting unit test

import numpy as np
from line_fitting import make_regression, make_best_fit_line

def test_regression_values():
    months = np.array([5,13,15,20,25,30,32,40,45,50,58,60])
    sales = np.array([50,100,147,200,250,305,350,420,450,500,550,600])

    slope, intercept, r_value, p_value, std_err = make_regression(months, sales)

#test if regression features correctly follow typical trends
#check if sales increase over time
    assert slope > 0
    #check if there is a positive correlation
    assert r_value > 0.98
    #check if there are any errors
    assert std_err < 5

#create a line of best fit
def test_line_of_best_fit():
    months = np.array([1,2,3])
    slope = 10
    intercept = 5

    result = make_best_fit_line(months, slope, intercept)
    expected = np.array([15,25,35])

    assert np.allclose(result, expected)

    #run unit test by typing pytest line_fitting_unit_test.py in terminal

