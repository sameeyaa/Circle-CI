#line fitting unit test

import numpy as np
from line_fitting import make_regression, make_best_fit_line

def test_regression_values():
    months = np.array([5,13,15,20,25,30,32,40,45,50,58,60])
    sales = np.array([50,100,147,200,250,305,350,420,450,500,550,600])

    slope, intercept, r_value, p_value, std_err = make_regression(months, sales)

